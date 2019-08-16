from django.shortcuts import render
from django.http import HttpResponse
from .models import LaunchData
from django.template.loader import render_to_string
import requests, datetime
# Create your views here
def returnResponse(request):
	queries = {'filter': 'flight_number,launch_date_utc,rocket/rocket_name,links/mission_patch'}
	#flight_number, launch_date_utc, rocket_name, mission_patch

	response = requests.get('https://api.spacexdata.com/v3/launches', params = queries)
	copy = response.json()
	for data in copy:
		launch_date_pretty = datetime.datetime.strptime(data['launch_date_utc'], "%Y-%m-%dT%H:%M:%S.%fZ").date()
		LaunchData.objects.create(
			flight_number = data['flight_number'], 
			launch_date = launch_date_pretty, 
			rocket_name = data['rocket']['rocket_name'], 
			mission_patch_link = data['links']['mission_patch'] if (data['links']['mission_patch'] is not None) else 'https://spaceflightnow.com/launch-schedule/')

	launch_data =  	LaunchData.objects.all()
	rendered = render_to_string('launches/launches_list.html', {'data': launch_data})
	return HttpResponse(rendered)
	#Or we can simply use the render function. But the task explicitly mentions HttpResponse object 
	#return render(request, 'launches/launches_list.html', {'data' : copy})
	
