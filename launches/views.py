from django.shortcuts import render
from django.http import HttpResponse
from .models import LaunchData
from django.template.loader import render_to_string
from django.utils import timezone
import requests, datetime
# Create your views here
def returnResponse(request):
	
	#This is intended as a major performance improvement. If the SpaceX API adds more launches in the future, only then we re-fetch the data from the API
	#Else we just display data from out database.

	#First we just request for flight numbers
	flight_numbers_only = requests.get('https://api.spacexdata.com/v3/launches/?filter=flight_number')
	flight_numbers_json = flight_numbers_only.json()
	list_of_flight_numbers = [dic['flight_number'] for dic in flight_numbers_json] # list comprehension created from dictionaries
	#Now if the maximum flight number returned is greater than the one stored in our database, re-fetch
	max_flight_number = max(list_of_flight_numbers)
	if max_flight_number > LaunchData.last_flight_number:
		
		#delete data from database to load new data
		LaunchData.objects.all().delete()
		queries = {'filter': 'flight_number,launch_date_utc,rocket/rocket_name,links/mission_patch'}
		#Queries:- flight_number, launch_date_utc, rocket_name, mission_patch
		
		response = requests.get('https://api.spacexdata.com/v3/launches', params = queries)
		copy = response.json()
		
		for data in copy:
			launch_date_pretty = datetime.datetime.strptime(data['launch_date_utc'], "%Y-%m-%dT%H:%M:%S.%fZ").date()
			LaunchData.objects.create(
				flight_number = data['flight_number'], 
				launch_date = launch_date_pretty, 
				rocket_name = data['rocket']['rocket_name'], 
				mission_patch_link = data['links']['mission_patch'] if (data['links']['mission_patch'] is not None) else 'https://spaceflightnow.com/launch-schedule/')
				#for missions which are yet to launch, no link is availaible so we redirect to launch-schedule instead
		LaunchData.last_flight_number = max_flight_number



	#Now we're also printing some recent questions about spaceX asked on space.stackexchange.com
	response = requests.get('https://api.stackexchange.com/2.2/questions?order=desc&sort=creation&tagged=spacex&site=space')
	questions = []
	for data in response.json()['items']:
		data_dic = {}
		data_dic['title'] = data['title']
		data_dic['link'] = data['link']
		questions.append(data_dic)

	#Now we send data from our database to the template
	launch_data = LaunchData.objects.all() #our queryset object
	launch_count = LaunchData.objects.filter(launch_date__lte = timezone.now()).count()
	# if one is nit-picky, this is not entirely correct since launch location and timezones will come into play
	rendered = render_to_string('launches/launches_list.html', {'data': launch_data, 'questions': questions, 'launch_count' : launch_count, 'scheduled_count' : launch_data.count()-launch_count})
	return HttpResponse(rendered)
	#Or we can simply use the render function. But the task explicitly mentions HttpResponse object 
	#return render(request, 'launches/launches_list.html', {'data' : copy})
	
