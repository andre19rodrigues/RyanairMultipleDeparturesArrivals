import json
import datetime
import requests
from operator import itemgetter
from time import gmtime, strftime

flightslist = []

def printFlights(departure, arrival, datein, dateout):
    global flightslist

    url = "https://api.ryanair.com/farefinder/3/oneWayFares?&departureAirportIataCode=" \
          + departure +"&arrivalAirportIataCode="\
          + arrival + "&language=en&limit=5000&market=en-gb&offset=0&outboundDepartureDateFrom=" \
          + datein + "&outboundDepartureDateTo=" + dateout

    r = requests.get(url)
    j = json.loads(r.content)

    for fare in j['fares']:
        flightslist.append(["Origin: " + fare['outbound']['departureAirport']['iataCode']
                            + " | Destination: " + fare['outbound']['arrivalAirport']['iataCode']
                            + " | Departure: " + fare['outbound']['departureDate']
                            + " | Arrival: " + fare['outbound']['arrivalDate']
                            + " | Price: " + str(fare['outbound']['price']['value'])
                            + fare['outbound']['price']['currencyCode'], fare['outbound']['price']['value']])


print("How many departure airports?")
ndeparture = int(input())

print("IATA codes for the departure airports (1 per line)")
departureairports = []

for i in range(0, int(ndeparture)):
    departureairports.append(raw_input())

print("How many arrival airports?")
narrival = int(input())

print("IATA codes for the arrival airports (1 per line)")
arrivalairports = []

for i in range(0, int(narrival)):
    arrivalairports.append(raw_input())

print ("What is the date from which you want to travel?")
print("Day?")
minimumday = raw_input()

print("Month?")
minimummonth = raw_input()

print("Year?")
minimumyear = raw_input()

print("How many range days?")
rangedays = int(input())


date = datetime.datetime(int(minimumyear), int(minimummonth), int(minimumday))
firstdate = date
for i in range(rangedays):

    month = ''
    day = ''
    for i in range(0, ndeparture):
        for j in range(0, narrival):
            if(date.month == 1 or date.month == 2 or date.month == 3 or date.month == 4 or date.month == 5 or date.month == 6
                    or date.month == 7 or date.month == 8 or date.month == 9):
                month='0'+str(date.month)
            else:
                month=str(date.month)

            if (date.day == 1 or date.day == 2 or date.day == 3 or date.day == 4 or date.day == 5 or date.day == 6
                    or date.day == 7 or date.day == 8 or date.day == 9):
                day = '0' + str(date.day)
            else:
                day=str(date.day)

            printFlights(departureairports[i], arrivalairports[j], str(date.year) + "-" + month + "-" + day, str(date.year) + "-" + month + "-" + day)
    date += datetime.timedelta(days=1)


flightslist.sort(key=itemgetter(1))


#Output result to file
file = 'ticketsfare.txt'
f = open(file, 'a+')

f.write(strftime("%Y-%m-%d %H:%M:%S", gmtime())+'\n')
f.write('Departure: '+str(departureairports)+'  Arrival: '+str(arrivalairports)+'     FirstDay: '+str(firstdate.strftime('%Y-%m-%d'))+'  LastDay: '+str(date.strftime('%Y-%m-%d'))+'\n')
for i in range(0, len(flightslist)):
    f.write(str(flightslist[i][0]) +'\n')

f.write('\n\n\n')
f.close()

with open(file, 'r') as fd:
    content = fd.read()

with open(file, 'w') as fd:
    fd.write(content.replace('T', ' '))