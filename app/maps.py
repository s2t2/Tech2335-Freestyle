import os
import json
import requests
from dotenv import load_dotenv
import datetime
from datetime import timedelta

# from app.flights import flight_details

load_dotenv()
APP_ENV = os.environ.get('APP_ENV', 'Dev')
MAPS_KEY = os.environ.get("MAPQUEST_API")
#user address
ADDRESS = os.environ.get("ADDRESS")
CITY = os.environ.get("CITY")
STATE = os.environ.get("STATE")
ZIP_CODE = os.environ.get("ZIP_CODE")
#TODO: pull airport address from aviation stack
TADDRESS = os.environ.get("TADDRESS")
TCITY = os.environ.get("TCITY")
TSTATE = os.environ.get("TSTATE")
TZIP_CODE = os.environ.get("TZIP_CODE")
#TODO: Pull flight arrival from aviationstack
flight_arrival = "2020-06-30T08:00"

def get_departure_time(f_street=ADDRESS,f_city=CITY,f_state=STATE,f_zip=ZIP_CODE,t_street=TADDRESS,t_city=TCITY,t_state=TSTATE,t_zip=TZIP_CODE,flight_arrival=flight_arrival):
    request_url = f"http://www.mapquestapi.com/directions/v2/optimizedroute?key={MAPS_KEY}&from={f_street},+{f_city},+{f_state},+{f_zip}&to={t_street},+{t_city},+{t_state},+{t_zip}&timeType=3&isoLocal={flight_arrival}"
    response = requests.get(request_url)
    response_data = json.loads(response.text)
    print(response.status_code)
    # print(response_data)
    travel_time = (response_data['route']['realTime'])
    departure_time = (datetime.datetime.fromisoformat(flight_arrival)-datetime.timedelta(seconds=travel_time))
    d_time = (departure_time.strftime("%B %d, %I:%M:%S %p"))
    return d_time
    
# print(get_departure_time())

if __name__ == "__main__":

    if APP_ENV == "development":
        f_street = input("PLEASE INPUT YOUR STREET ADDRESS:")
        f_city = input("PLEASE INPUT YOUR CITY:")
        f_state = input("PLEASE INPUT YOUR STATE (e.g. NY):")
        f_zip = input("PLEASE INPUT YOUR ZIP CODE (e.g. 10012):")
        results = get_departure_time(f_street=f_street,f_city=f_city,f_state=f_state,f_zip=f_zip)
    else:
        results = get_departure_time()
    print(f"LEAVE AT: {results}")    