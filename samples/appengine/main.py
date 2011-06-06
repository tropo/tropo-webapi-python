"""
This script is intended to be used with Google Appengine. It contains
a number of demos that illustrate the Tropo Web API for Python.
"""

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
import cgi
import logging
import tropo
import GoogleS3
from xml.dom import minidom
from google.appengine.api import urlfetch
from xml.etree import ElementTree
from setup import *



def HelloWorld(handler, t):
    """
    This is the traditional "Hello, World" function. The idiom is used throughout the API. We construct a Tropo object, and then flesh out that object by calling "action" functions (in this case, tropo.say). Then call tropo.Render, which translates the Tropo object into JSON format. Finally, we write the JSON object to the standard output, so that it will get POSTed back to the API.
    """
    t.say (["Hello, World", "How ya doing?"])
    json = t.RenderJson()
    logging.info ("HelloWorld json: %s" % json)
    handler.response.out.write(json)

def WeatherDemo(handler, t):
    """
    """
    choices = tropo.Choices("[5 digits]")

    t.ask(choices, 
              say="Please enter your 5 digit zip code.", 
              attempts=3, bargein=True, name="zip", timeout=5, voice="dave")

    t.on(event="continue", 
             next="/weather.py?uri=end",
             say="Please hold.")

    t.on(event="error",
             next="/weather.py?uri=error",
             say="Ann error occurred.")

    json = t.RenderJson()
    logging.info ("Json result: %s " % json)
    logging.info ("WeatherDemo json: %s" % json)

    handler.response.out.write(json)

def RecordDemo(handler, t):

    url = "%s/receive_recording.py" % THIS_URL
    choices_obj = tropo.Choices("", terminator="#").json
    t.record(say="Tell us about yourself", url=url, 
                 choices=choices_obj)
    json = t.RenderJson()
    logging.info ("Json result: %s " % json)
    handler.response.out.write(json)

def SMSDemo(handler, t):

    t.message("Hello World", MY_PHONE, channel='TEXT', network='SMS', timeout=5)
    json = t.RenderJson()
    logging.info ("Json result: %s " % json)
    handler.response.out.write(json)


def RecordHelloWorld(handler, t):
    """
    Demonstration of recording a message.
    """
    url = "%s/receive_recording.py" % THIS_URL
    t.startRecording(url)
    t.say ("Hello, World.")
    t.stopRecording()
    json = t.RenderJson()
    logging.info ("RecordHelloWorld json: %s" % json)
    handler.response.out.write(json)

def RedirectDemo(handler, t):
    """
    Demonstration of redirecting to another number.
    """
    # t.say ("One moment please.")
    t.redirect(SIP_PHONE)
    json = t.RenderJson()
    logging.info ("RedirectDemo json: %s" % json)
    handler.response.out.write(json)

def TransferDemo(handler, t):
    """
    Demonstration of transfering to another number
    """
    t.say ("One moment please.")
    t.transfer(MY_PHONE)
    t.say("Hi. I am a robot")
    json = t.RenderJson()
    logging.info ("TransferDemo json: %s" % json)
    handler.response.out.write(json)



def CallDemo(handler, t):
    t.call(THEIR_PHONE)
    json = t.RenderJson()
    logging.info ("CallDemo json: %s " % json)
    handler.response.out.write(json)

def ConferenceDemo(handler, t):
    t.say ("Have some of your friends launch this demo. You'll be on the world's simplest conference call.")
    t.conference("partyline", terminator="#", name="Family Meeting")
    json = t.RenderJson()
    logging.info ("ConferenceDemo json: %s " % json)
    handler.response.out.write(json)




# List of Demos
DEMOS = {
 '1' : ('Hello World', HelloWorld),
 '2' : ('Weather Demo', WeatherDemo),
 '3' : ('Record Demo', RecordDemo),
 '4' : ('SMS Demo', SMSDemo),
 '5' : ('Record Conversation Demo', RecordHelloWorld),
 '6' : ('Redirect Demo', RedirectDemo),
 '7' : ('Transfer Demo', TransferDemo),
 '8' : ('Call Demo', CallDemo),
 '9' : ('Conference Demo', ConferenceDemo)
}

class TropoDemo(webapp.RequestHandler):
    """
    This class is the entry point to the Tropo Web API for Python demos. Note that it's only method is a POST method, since this is how Tropo kicks off.
        
    A bundle of information about the call, such as who is calling, is passed in via the POST data.
    """
    def post(self):
        t = tropo.Tropo()
        t.say ("Welcome to the Tropo web API demo")

        request = "Please press"
        choices_string = ""
        choices_counter = 1
        for key in sorted(DEMOS.iterkeys()):
            if (len(choices_string) > 0):
                choices_string = "%s,%s" % (choices_string, choices_counter)
            else:
                choices_string = "%s" % (choices_counter)
            demo_name = DEMOS[key][0]
            demo = DEMOS[key][1]
            request = "%s %s for %s," % (request, key, demo_name)
            choices_counter += 1
        choices = tropo.Choices(choices_string)

        t.ask(choices, say=request, attempts=3, bargein=True, name="zip", timeout=5, voice="dave")

        t.on(event="continue", 
                     next="/demo_continue.py",
                     say="Please hold.")

        t.on(event="error",
                     next="/demo_continue.py",
                     say="An error occurred.")

        json = t.RenderJson()
        logging.info ("Json result: %s " % json)
        self.response.out.write(json)


class TropoDemoContinue(webapp.RequestHandler):
    """
    This class implements all the top-level demo functions. Data is POSTed to the application, to start tings off. After retrieving the result value, which is a digit indicating the user's choice of demo function, the POST method dispatches to the chosen demo.
    """
    def post (self):
        json = self.request.body
        logging.info ("json: %s" % json)
        t = tropo.Tropo()
        result = tropo.Result(json)
        choice = result.getValue()
        logging.info ("Choice of demo is: %s" % choice)

        for key in DEMOS:
            if (choice == key):
                demo_name = DEMOS[key][0]
                demo = DEMOS[key][1]
                demo(self, t)
                break
    
class Weather(webapp.RequestHandler):
    def post (self):
        json = self.request.body
        logging.info ("json: %s" % json)

        uri = self.request.get ('uri')
        logging.info ("uri: %s" % uri)

        t = tropo.Tropo()

	if (uri == "error"):
	   t.say ("Oops. There was some kind of error")
           json = t.RenderJson()
           self.response.out.write(json)
	   return

        result = tropo.Result(json);
        zip = result.getValue()
        google_weather_url = "%s?weather=%s&hl=en" % (GOOGLE_WEATHER_API_URL, zip)
        resp = urlfetch.fetch(google_weather_url)

        logging.info ("weather url: %s " % google_weather_url)
        if (resp.status_code == 200):
            xml = resp.content
            logging.info ("weather xml: %s " % xml)
            doc = ElementTree.fromstring(xml)            
            logging.info ("doc: %s " % doc)
            condition = doc.find("weather/current_conditions/condition").attrib['data']
            temp_f  = doc.find("weather/current_conditions/temp_f").attrib['data']
            wind_condition = doc.find("weather/current_conditions/wind_condition").attrib['data']
            city = doc.find("weather/forecast_information/city").attrib['data']
            logging.info ("condition: %s temp_f: %s wind_condition: %s city: %s" % (condition, temp_f, wind_condition, city))
            t = tropo.Tropo()
            # condition: Partly Cloudy temp_f: 73 wind_condition: Wind: NW at 10 mph city: Portsmouth, NH
            temp = "%s degrees" % temp_f
            wind = self.english_expand (wind_condition)
            t.say("Current city is %s . Weather conditions are %s. Temperature is %s. %s ." % (city, condition, temp, wind))        
            json = t.RenderJson()

            self.response.out.write(json)


# Wind: N at 0 mph

    def english_expand(self, expr):
        logging.info ("expr is : %s" % expr)
        expr = expr.replace("Wind: NW", "Wind is from the North West")
        expr = expr.replace("Wind: NE", "Wind is from the North East")
        expr = expr.replace("Wind: N", "Wind is from the North")
        expr = expr.replace("Wind: SW", "Wind is from the South West")
        expr = expr.replace("Wind: SE", "Wind is from the South East")
        expr = expr.replace("Wind: S", "Wind is from the South")
        expr = expr.replace("mph", "miles per hour")
        return expr


class ReceiveRecording(webapp.RequestHandler):
    def post(self):
        logging.info ("I just received a post recording")
#        wav = self.request.body
        wav = self.request.get ('filename')
        logging.info ("Just got the wav as %s" % wav)
        self.put_in_s3(wav)
        logging.info ("I just put the wav in s3")

    def put_in_s3 (self, wav):

        conn = GoogleS3.AWSAuthConnection(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
        key_name = "testing.wav"
        logging.info ("Putting content in %s in %s bucket" % (key_name, S3_BUCKET_NAME))
        responsedict={}
        logging.info ("really putting stuff in %s %s" % (S3_BUCKET_NAME, key_name))
        audio_type = 'audio/wav'
        
        response = conn.put(
            S3_BUCKET_NAME,
            key_name,
            GoogleS3.S3Object(wav),
        {'Content-Type' : audio_type, 
         'x-amz-acl' : 'public-read'})
        responsedict["response"] = response
        responsedict["url"] = "%s/%s/%s" % (AMAZON_S3_URL, S3_BUCKET_NAME, key_name)
        return responsedict



class CallWorld(webapp.RequestHandler):
    def post(self):
        t = tropo.Tropo()
        t.call(MY_PHONE, channel='TEXT', network='SMS', answerOnMedia='True')
        t.say ("Wish you were here")
        json = t.RenderJson()
        logging.info ("Json result: %s " % json)
        self.response.out.write(json)



class MainHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write('Hello world!')


def main():
    application = webapp.WSGIApplication([('/', MainHandler),
                                          ('/hello_tropo.py', TropoDemo),
                                          ('/weather.py', Weather),
                                          ('/receive_recording.py', ReceiveRecording),
                                          ('/demo_continue.py', TropoDemoContinue),
#                                          ('/tropo_web_api.html', ShowDoc)

  ],
                                         debug=True)
    util.run_wsgi_app(application)

if __name__ == '__main__':
    main()
