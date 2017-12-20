import requests
import gi
gi.require_version("Notify", "0.7")
from gi.repository import Notify

getRequestUrl='https://quotes.rest/qod'
getRequestAction=requests.get(getRequestUrl)
jsonRequestData=getRequestAction.json()

qoute=jsonRequestData['contents']['quotes'][0]['quote']
author=jsonRequestData['contents']['quotes'][0]['author']
Notify.init ("Quote of the Day")
quoteOfTheDay=Notify.Notification.new ("Quote of the Day",
                               qoute+" '"+author+"'",
                               "dialog-information")
quoteOfTheDay.show ()
