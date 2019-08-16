from django.shortcuts import render
#from django.http import HttpResponse
import requests, datetime
# Create your views here
def returnResponse(request):
	queries = {'filter': 'flight_number,launch_date_utc,rocket/rocket_name,links/mission_patch'}
	#flight_number, launch_date_utc, rocket_name, mission_patch

	response = requests.get('https://api.spacexdata.com/v3/launches', params = queries)
	copy = response.json()

	for data in copy:
		launch_date_pretty = datetime.datetime.strptime(data['launch_date_utc'], "%Y-%m-%dT%H:%M:%S.%fZ").date()
		#strptime parses a string representing a time according to a format

		data['launch_date_utc'] = launch_date_pretty.strftime('%d %b, %Y')
		#strftime formats a tuple representing a date/time to a string
		
		#Now we've to remove the nesting present in rocket and links keys
		data['rocket_name'] = data['rocket']['rocket_name']
		del data['rocket']
		data['mission_patch'] = data['links']['mission_patch']
		del data['links']

	#return HttpResponse(copy)
	print(len(copy))
	return render(request, 'launches/launches_list.html', {'data' : copy})
