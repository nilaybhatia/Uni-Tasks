#API practice + Experimental file using Requests module in python
import requests, datetime
r = requests.get('http://api.open-notify.org/astros.json')
print (r.json())
for p in r.json()['people']:
	print (p['name'] + "\t" + p['craft'])

flight_numbers_only = requests.get('https://api.spacexdata.com/v3/launches/?filter=flight_number')
flight_numbers_json = flight_numbers_only.json()
list_of_flight_numbers = [dic['flight_number'] for dic in flight_numbers_json] # list comprehension created from dictionaries
#Now if the maximum flight number returned is greater than the one stored in our database, re-fetch
max_flight_number = max(list_of_flight_numbers)
print(max_flight_number)

queries = {'filter': 'flight_number,launch_date_utc,rocket/rocket_name,links/mission_patch'}
r = requests.get('https://api.spacexdata.com/v3/launches/', params = queries)
print(r.url)
print(r.json())
copy = r.json()
for data in copy:
	#print(data['launch_date_utc'])
	launch_date_pretty = datetime.datetime.strptime('2017-10-09T12:37:00.000Z', "%Y-%m-%dT%H:%M:%S.%fZ").date()
	launch_time = datetime.datetime.strptime('2017-10-09T12:37:00.000Z', "%Y-%m-%dT%H:%M:%S.%fZ").time()
	print (launch_time)
	data['launch_date_utc'] = launch_date_pretty.strftime('%d %b, %Y')
print(copy)

file = open('last_flight_number.txt', 'r')
last_flight_number = int(file.read())
file.close()

file = open('last_flight_number.txt', 'w')
file.write(str(103))
file.close()