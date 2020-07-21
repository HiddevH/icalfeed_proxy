from flask import Flask, send_file
from flask_restful import Resource, Api
import os

app = Flask(__name__)
api = Api(app)

# iCal feed needs to be passed from env (e.g. via docker-compose) for security
ical_feed = os.getenv('ICAL_FEED', 'test')

class GetICalFeed(Resource):
    def get(self):        
        import urllib.request
        url = ical_feed
        hdr = {'User-Agent':'Mozilla/5.0'}
        try:
            req = urllib.request.Request(url, headers=hdr)
            data = urllib.request.urlopen(req)      # a `bytes` object
            return send_file(data, as_attachment=True, attachment_filename='ical_feed.ics')
        except Exception as e:
            print(f'exception: {e}')

api.add_resource(GetICalFeed, '/icalfeed') # Route
