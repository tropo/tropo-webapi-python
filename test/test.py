#!/usr/bin/env python


try:
    import cjson as jsonlib
    jsonlib.dumps = jsonlib.encode
    jsonlib.loads = jsonlib.decode
except ImportError:
    try:
        from django.utils import simplejson as jsonlib
    except ImportError:
        try:
            import simplejson as jsonlib
        except ImportError:
            import json as jsonlib

import unittest 
import sys
sys.path = ['..'] + sys.path
from tropo import Choices, Say, Tropo


class TestTropoPython(unittest.TestCase):        
    """
    Class implementing a set of unit tests for TropoPython.
    """
    TO = "8005551212"
    MY_PHONE = "6021234567"
    RECORDING_URL = "/receive_recording.py"
    ID = "foo"
    S3_URL = "http://s3.amazonaws.com/xxx_s3_bucket/hello.wav"


    def test_ask(self):
        """
        Test the "ask" Tropo class method.
        """
        tropo = Tropo()
        tropo.ask("[5 digits]",
                  say = Say("Please enter a 5 digit zip code").json)
        rendered = tropo.RenderJson()
        pretty_rendered = tropo.RenderJson(pretty=True)
        print "===============test_ask================="
        print "render json: %s" % pretty_rendered
        rendered_obj = jsonlib.loads(rendered)
        wanted_json = '{"tropo": [{"ask": {"say": {"value": "Please enter a 5 digit zip code"}, "choices": {"value": "[5 digits]"}}}]}'
        wanted_obj = jsonlib.loads(wanted_json)
        # print "test_ask: %s" % tropo.RenderJson()
        self.assertEqual(rendered_obj, wanted_obj)

    def test_call(self):
        """
        Test the "call" Tropo class method.
        """

        tropo = Tropo()
        tropo.call(self.MY_PHONE, channel='TEXT', network='SMS')
        tropo.say ("Wish you were here")
        rendered = tropo.RenderJson()
        pretty_rendered = tropo.RenderJson(pretty=True)
        print ("============test_call=============")
        print "render json: %s" % pretty_rendered

        rendered_obj = jsonlib.loads(rendered)
        wanted_json = '{"tropo": [{"call": {"to": "%s", "network": "SMS", "channel": "TEXT"}}, {"say": {"value": "Wish you were here"}}]}' % self.MY_PHONE
        wanted_obj = jsonlib.loads(wanted_json)
        # print "test_call: %s" % tropo.RenderJson()
        self.assertEqual(rendered_obj, wanted_obj)

    def test_conference(self):
        """
        Test the "conference" Tropo class method.
        """

        tropo = Tropo()
        tropo.conference(self.ID, playTones=True, mute=False,
                   name="Staff Meeting")
        rendered = tropo.RenderJson()
        pretty_rendered = tropo.RenderJson(pretty=True)
        print "===============test_conference================="
        print "render json: %s" % pretty_rendered

        rendered_obj = jsonlib.loads(rendered)
        wanted_json = '{"tropo": [{"conference": {"playTones": true, "mute": false, "name": "Staff Meeting", "id": "foo"}}]}'
        print "wanted_json: %s" % wanted_json
        wanted_obj = jsonlib.loads(wanted_json)
        # print "test_conference: %s" % tropo.RenderJson()
        self.assertEqual(rendered_obj, wanted_obj)

    def test_hangup(self):
        """
        Test the "hangup" Tropo class method.
        """

        tropo = Tropo()
        tropo.hangup()
        rendered = tropo.RenderJson()
        pretty_rendered = tropo.RenderJson(pretty=True)
        print "===============test_hangup================="
        print "render json: %s" % pretty_rendered

        # print "test_hangup: %s" % tropo.RenderJson()
        rendered_obj = jsonlib.loads(rendered)
        wanted_json = '{"tropo": [{"hangup": {}}]}'
        wanted_obj = jsonlib.loads(wanted_json)
        self.assertEqual(rendered_obj, wanted_obj)

    def test_message(self):
        """
        Test the "message" Tropo class method.
        """

        tropo = Tropo()
        tropo.message("Hello World", self.MY_PHONE, channel='TEXT', network='SMS', timeout=5)
        rendered = tropo.RenderJson()
        pretty_rendered = tropo.RenderJson(pretty=True)
        print "===============test_message================="
        print "render json: %s" % pretty_rendered

        # print "test_message: %s" % tropo.RenderJson()
        rendered_obj = jsonlib.loads(rendered)
        wanted_json = ' {"tropo": [{"message": {"to": "%s", "say": {"value": "Hello World"}, "network": "SMS", "timeout": 5, "channel": "TEXT"}}]}' % self.MY_PHONE
        wanted_obj = jsonlib.loads(wanted_json)
        self.assertEqual(rendered_obj, wanted_obj)

    def test_on(self):
        """
        Test the "on" Tropo class method.
        """

        tropo = Tropo()

        tropo.on(event="continue", 
             next="/weather.py?uri=end",
             say="Please hold.")
        rendered = tropo.RenderJson()
        pretty_rendered = tropo.RenderJson(pretty=True)
        print "===============test_on================="
        print "render json: %s" % pretty_rendered

        # print "test_on: %s" % tropo.RenderJson()
        rendered_obj = jsonlib.loads(rendered)
        wanted_json = ' {"tropo": [{"on": {"say": {"value": "Please hold."}, "event": "continue", "next": "/weather.py?uri=end"}}]}'
        wanted_obj = jsonlib.loads(wanted_json)
        self.assertEqual(rendered_obj, wanted_obj)

    def test_record(self):
        """
        Test the "record" Tropo class method.
        """

        tropo = Tropo()
        url = "/receive_recording.py"
        choices_obj = Choices("", terminator="#").json
        tropo.record(say="Tell us about yourself", url=url, 
                     choices=choices_obj)
        rendered = tropo.RenderJson()
        pretty_rendered = tropo.RenderJson(pretty=True)
        print "===============test_record================="
        print "render json: %s" % pretty_rendered

        # print "test_record: %s" % tropo.RenderJson()
        rendered_obj = jsonlib.loads(rendered)
        wanted_json = ' {"tropo": [{"record": {"url": "/receive_recording.py", "say": {"value": "Tell us about yourself"}, "choices": {"terminator": "#", "value": ""}}}]}'
        wanted_obj = jsonlib.loads(wanted_json)
        self.assertEqual(rendered_obj, wanted_obj)

    def test_redirect(self):
        """
        Test the "redirect" Tropo class method.
        """

        tropo = Tropo()
        tropo.redirect(self.MY_PHONE)
        rendered = tropo.RenderJson()
        pretty_rendered = tropo.RenderJson(pretty=True)
        print "===============test_redirect================="
        print "render json: %s" % pretty_rendered

        print "Wanted_Json %s" % tropo.RenderJson()
        rendered_obj = jsonlib.loads(rendered)
        wanted_json = '{"tropo": [{"redirect": {"to": "%s"}}]}' % self.MY_PHONE
        wanted_obj = jsonlib.loads(wanted_json)
        # print "test_redirect: %s" % tropo.RenderJson()
        self.assertEqual(rendered_obj, wanted_obj)

    def test_reject(self):
        """
        Test the "reject" Tropo class method.
        """

        tropo = Tropo()
        tropo.reject()
        rendered = tropo.RenderJson()
        pretty_rendered = tropo.RenderJson(pretty=True)
        print "===============test_reject================="
        print "render json: %s" % pretty_rendered

        print "Want %s" % tropo.RenderJson()
        rendered_obj = jsonlib.loads(rendered)
        wanted_json = '{"tropo": [{"reject": {}}]}'
        wanted_obj = jsonlib.loads(wanted_json)
        # print "test_reject: %s" % tropo.RenderJson()
        self.assertEqual(rendered_obj, wanted_obj)

    def test_say(self):
        """
        Test the "say" Tropo class method.
        """

        tropo = Tropo()
        tropo.say("Hello, World")
        rendered = tropo.RenderJson()
        pretty_rendered = tropo.RenderJson(pretty=True)
        print "===============test_say================="
        print "render json: %s" % pretty_rendered

        # print "test_say: %s" % tropo.RenderJson()
        rendered_obj = jsonlib.loads(rendered)
        wanted_json = '{"tropo": [{"say": {"value": "Hello, World"}}]}'
        wanted_obj = jsonlib.loads(wanted_json)
        self.assertEqual(rendered_obj, wanted_obj)

    def test_list_say(self):
        """
        Test the "say" Tropo class method, when a list of Strings is passed to it.
        """

        tropo = Tropo()
        tropo.say(["Hello, World", "How ya doing?"])
        rendered = tropo.RenderJson()
        pretty_rendered = tropo.RenderJson(pretty=True)
        print "===============test_list_say================="
        print "render json: %s" % pretty_rendered

        # print "test_say: %s" % tropo.RenderJson()
        rendered_obj = jsonlib.loads(rendered)
        wanted_json = '{"tropo": [{"say": [{"value": "Hello, World"}, {"value": "How ya doing?"}]}]}'
        wanted_obj = jsonlib.loads(wanted_json)
        self.assertEqual(rendered_obj, wanted_obj)

    def test_startRecording(self):
        """
        Test the "startRecording" Tropo class method.
        """

        tropo = Tropo()
        tropo.startRecording(self.RECORDING_URL)
        rendered = tropo.RenderJson()
        pretty_rendered = tropo.RenderJson(pretty=True)
        print "===============test_startRecording================="
        print "render json: %s" % pretty_rendered

        # print "test_startRecording: %s" % tropo.RenderJson()
        rendered_obj = jsonlib.loads(rendered)
        wanted_json = '{"tropo": [{"startRecording": {"url": "/receive_recording.py"}}]}'
        wanted_obj = jsonlib.loads(wanted_json)
        self.assertEqual(rendered_obj, wanted_obj)

    def test_stopRecording(self):
        """
        Test the "stopRecording" Tropo class method.
        """

        tropo = Tropo()
        tropo.stopRecording()
        rendered = tropo.RenderJson()
        pretty_rendered = tropo.RenderJson(pretty=True)
        print "===============test_stopRecording================="
        print "render json: %s" % pretty_rendered

        # print "test_stopRecording: %s" % tropo.RenderJson()
        rendered_obj = jsonlib.loads(rendered)
        wanted_json = ' {"tropo": [{"stopRecording": {}}]}'
        wanted_obj = jsonlib.loads(wanted_json)
        self.assertEqual(rendered_obj, wanted_obj)

    def test_transfer(self):
        """
        Test the "transfer" Tropo class method.
        """

        tropo = Tropo()
        tropo.say ("One moment please.")
        tropo.transfer(self.MY_PHONE)
        tropo.say("Hi. I am a robot")
        rendered = tropo.RenderJson()
        pretty_rendered = tropo.RenderJson(pretty=True)
        print "===============test_transfer================="
        print "render json: %s" % pretty_rendered

        # print "test_transfer: %s" % tropo.RenderJson()
        rendered_obj = jsonlib.loads(rendered)
        wanted_json = '{"tropo": [{"say": {"value": "One moment please."}}, {"transfer": {"to": "6021234567"}}, {"say": {"value": "Hi. I am a robot"}}]}'
        wanted_obj = jsonlib.loads(wanted_json)
        self.assertEqual(rendered_obj, wanted_obj)


if __name__ == '__main__':
    """
    Unit tests.
    """
    if (0):
        TO = "8005551212"

        ID = "foo"
        URL = "http://s3.amazonaws.com/xxx_s3_bucket/hello.wav"



        tropo = Tropo()

        tropo.ask("[5 digits]",
                  say = Say("Please enter a 5 digit zip code").json)

        tropo.call (TO)
        tropo.conference(ID)
        tropo.hangup()
        tropo.message ("Hello, World", TO)
        tropo.on(event="continue", 
             next="http://example.com/weather.py",
             say="Please hold.")

        tropo.record(say="Please say something for posterity", 
                     url=URL, 
                     choices = Choices("", terminator="#").json)
        tropo.redirect(ID)
        tropo.reject(ID)
        tropo.startRecording(URL)
        tropo.stopRecording()
        tropo.transfer(TO)

        tropo.message("Hello, World",
                      TO, 
                      channel='TEXT', 
                      network='SMS')

    else:
        unittest.main()


