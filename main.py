import requests
import json
import pyttsx3

try:
    city=input("Enter Your City Name:")
    result=requests.get(f"https://api.weatherapi.com/v1/current.json?key=8bbf9a0480ec4e5dbde65406240905 &q={city}&aqi=yes")
    #print(result.text)
    dict=json.loads(result.text)
    engine=pyttsx3.init()
    engine.setProperty('rate',150)
    engine.setProperty('volume',0.9)
    print(f"The Temperature in {city} is :{dict["current"]["temp_c"]}")
    engine.say(f"The Temperature in {city} is :{dict["current"]["temp_c"]}")
    engine.runAndWait()
    engine.say("Thank You")
    print("Thank You!!")
    engine.runAndWait()

except Exception as e:
    print("The Exception occured",e)
