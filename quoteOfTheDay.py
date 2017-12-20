import requests
import gi
gi.require_version("Notify", "0.7")
from gi.repository import Notify,GdkPixbuf

getRequestUrl='https://quotes.rest/qod'
getRequestAction=requests.get(getRequestUrl)
jsonRequestData=getRequestAction.json()

qoute=jsonRequestData['contents']['quotes'][0]['quote']
author=jsonRequestData['contents']['quotes'][0]['author']

# Use GdkPixbuf to create the proper image type
image = GdkPixbuf.Pixbuf.new_from_file("big-G.png")


Notify.init ("Quote of the Day")
quoteOfTheDay=Notify.Notification.new ("Quote of the Day",
                               qoute+" '"+author+"'",)
# Use the GdkPixbuf image
quoteOfTheDay.set_icon_from_pixbuf(image)
quoteOfTheDay.set_image_from_pixbuf(image)

quoteOfTheDay.show()
