from django.shortcuts import render
from django.http import HttpResponse
import requests, datetime
# Create your views here
def returnResponse(request):
	r = requests.get('https://api.spacexdata.com/v3/launches/?filter=flight_number,rocket_name,launch_date_local,land_success,mission_patch&pretty=true')
	return HttpResponse(r.json())
