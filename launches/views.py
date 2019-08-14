from django.shortcuts import render
from django.http import HttpResponse
import requests, datetime
# Create your views here
def returnResponse(request):
	queries = {'filter': 'flight_number,launch_date_utc,rocket/rocket_name,links/mission_patch'}
	r = requests.get('https://api.spacexdata.com/v3/launches', params = queries)
	#print(r.url)
	return HttpResponse(r.json())
#flight_number, launch_date_utc, rocket_name, mission_patch
