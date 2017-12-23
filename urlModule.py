import requests

class requestURL(object):
    """docstring for requestURL."""
    def __init__(self, arg):
        super(requestURL, self).__init__()
        self.arg = arg

    def getRequest():
        getRequestUrl='https://quotes.rest/qod'
        getRequestAction=requests.get(getRequestUrl)
        jsonRequestData=getRequestAction.json()

        qoute=jsonRequestData['contents']['quotes'][0]['quote']
        author=jsonRequestData['contents']['quotes'][0]['author']
