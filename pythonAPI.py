#API practice using Requests module in python
import requests, datetime
r = requests.get('http://api.open-notify.org/astros.json')
print (r.json())
for p in r.json()['people']:
	print (p['name'] + "\t" + p['craft'])

queries = {'filter': 'flight_number,launch_date_utc,rocket/rocket_name,links/mission_patch'}
r = requests.get('https://api.spacexdata.com/v3/launches/', params = queries)
print(r.url)
print(r.json())
copy = r.json()
for data in copy:
	print(data['launch_date_utc'])
	launch_date_pretty = datetime.datetime.strptime('2017-10-09T12:37:00.000Z', "%Y-%m-%dT%H:%M:%S.%fZ").date()
	data['launch_date_utc'] = launch_date_pretty.strftime('%d %b, %Y')
print(copy)
	
	