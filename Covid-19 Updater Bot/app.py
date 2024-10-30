import requests
from win10toast import ToastNotifier
import time

def update():
    toast = ToastNotifier()  

    while True:
        try:
            
            r = requests.get('http://coronavirus-19-api.herokuapp.com/all')
            data = r.json()
            text = f'Confirmed Cases: {data["cases"]} \nDeaths: {data["deaths"]} \nRecovered: {data["recovered"]}'
            
            
            toast.show_toast("Covid-19 Updates", text, duration=20)
            
        except requests.exceptions.RequestException as e:
            print("Error fetching data:", e)
        
        
        time.sleep(60)
        
update()
