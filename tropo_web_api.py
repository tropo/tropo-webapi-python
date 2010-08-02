#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# from google.appengine.ext import webapp
# from google.appengine.ext.webapp import util
from django.utils import simplejson
import cgi
import logging
import pprint
 


class Choices():
    def __init__(self, value, **options):
        dict = {}
        options_array = ['terminator']

        for opt in options_array:
            if opt in options:
                dict[opt] = options[opt]

        dict['value'] = value

        self.obj = {'choices': dict}
        self.json = dict

class Ask():
    """
    Python class that corresponds to "ask" json object. 
    (See https://www.tropo.com/docs/webapi/ask.htm)

        { "ask": {
            "attempts": Integer,
            "bargein": Boolean,
            "choices": Object, #Required
            "minConfidence": Integer,
            "name": String,
            "recognizer": String,
            "required": Boolean,
            "say": Object,
            "timeout": Float,
            "voice": String } } 

    """
    def __init__(self, choices, **options):

        dict = {}
        options_array = ['attempts', 'bargein', 'choices', 'minConfidence', 'name', 'recognizer', 'required', 'say', 'timeout', 'voice']
        
        if (isinstance(choices, str)):
            choices1 = Choices(choices).json
            dict['choices'] = choices1
        else:
            dict['choices'] = choices['choices']
        for opt in options_array:
            if opt in options:
                if ((opt == 'say') and (isinstance(options['say'], str))):
                    say_obj = options['say']
                    say_obj1 = Say(say_obj).json
                    dict['say'] = say_obj1
                else:
                    dict[opt] = options[opt]
        self.obj = {'ask' : dict}
        self.json = dict

class Call():
    """
    Python class that corresponds to "call" json object. 
    (See https://www.tropo.com/docs/webapi/call.htm)

    { "call": {
        "to": String or Array,#Required
        "answerOnMedia": Boolean,
        "channel": string,
        "from": string,
        "headers": Object,
        "name": String,
        "network": String,
        "recording": Array or Object,
        "required": Boolean,
        "timeout": Float } } 
    """
    def __init__(self, to, **options):
        dict = {}
        dict['to'] = to
        options_array = ['answerOnMedia', 'channel', 'from', 'headers', 'name', 'network', 'recording', 'required', 'timeout']
        for opt in options_array:
            if opt in options:
                dict[opt] = options[opt]
        self.obj = {'call' : dict}
        self.json = dict

class Conference():
    """
    Python class that corresponds to "conference" json object. 
    (See https://www.tropo.com/docs/webapi/conference.htm)

    { "conference": {
        "id": String,#Required
        "mute": Boolean,
        "name": String,
        "playTones": Boolean,
        "required": Boolean,
        "terminator": String } } 
    """

    def __init__(self, to, **options):
        dict = {}

        options_array = ['id', 'mute', 'name', 'playTones', 'required', 'terminator']

        for opt in options_array:
            if opt in options:
                dict[opt] = options[opt]
        self.obj = {'conference' : dict}
        self.json = dict

class Hangup ():
    """
    Python class that corresponds to "hangug" json object. 
    (See https://www.tropo.com/docs/webapi/hangup.htm)

    { "hangup": { } } 
    """
    def __init__(self):
        dict = {}
        self.obj = {'hangup' : dict}
        self.json = dict

class Message():
    """
        { "message": {
            "say": Object,#Required
            "to": String or Array,#Required
            "answerOnMedia": Boolean,
            "channel": string,
            "from": Object,
            "name": String,
            "network": String,
            "required": Boolean,
            "timeout": Float,
            "voice": String } } 
    """
    def __init__(self, say_obj, to, **options):

        dict = {}

        # say_obj = Say(message).obj
        say_payload = say_obj['say']
        dict['say'] = say_payload
        dict['to'] = to

        options_array = ['answerOnMedia', 'channel', 'from', 'name', 'network', 'required', 'timeout', 'voice']

        logging.info ("options: %s" % options)
        for opt in options_array:
            if opt in options:
                dict[opt] = options[opt]
        self.obj = {'message' : dict}
        self.json = dict

class On():
    """
    Python class that corresponds to "on" json object. 
    (See https://www.tropo.com/docs/webapi/on.htm)

    { "on": {
        "event": String,#Required
        "name": String,
        "next": String,
        "required": Boolean,
        "say": Object } } 
    """
    def __init__(self, event, **options):
        dict = {}
        dict['event'] = event
        options_array = ['name','next','required','say']
        for opt in options_array:
            if opt in options:
                if ((opt == 'say') and (isinstance(options['say'], str))):
                    say_obj = options['say']
                    say_obj1 = Say(say_obj).json
                    dict['say'] = say_obj1
                else:
                    dict[opt] = options[opt]

        self.obj = {'on' : dict}
        self.json = dict


class Record():
    """
    Python class that corresponds to "record" json object. 
    (See https://www.tropo.com/docs/webapi/record.htm)

        { "record": {
            "attempts": Integer,
            "bargein": Boolean,
            "beep": Boolean,
            "choices": Object,
            "format": String,
            "maxSilence": Float,
            "maxTime": Float,
            "method": String,
            "minConfidence": Integer,
            "name": String,
            "password": String,
            "required": Boolean,
            "say": Object,
            "timeout": Float,
            "transcription": Array or Object,
            "url": String,#Required ?????
            "username": String } } 
    """

    def __init__(self, **options):
        dict = {}
        options_array = ['attempts', 'bargein', 'beep', 'choices', 'format', 'maxSilence', 'maxTime', 'method', 'minConfidence', 'name', 'password', 'required', 'say', 'timeout', 'transcription', 'url', 'username']
        for opt in options_array:
            if opt in options:
                if ((opt == 'say') and (isinstance(options['say'], str))):
                    say_obj = options['say']
                    say_obj1 = Say(say_obj).json
                    dict['say'] = say_obj1
                else:
                    dict[opt] = options[opt]
        self.obj = {'record' : dict}
        self.json = dict


class Redirect():
    """
    Python class that corresponds to "redirect" json object. 
    (See https://www.tropo.com/docs/webapi/redirect.htm)

    { "redirect": {
        "to": Object,#Required
        "name": String,
        "required": Boolean } } 
    """
    def __init__(self, to, **options):
        dict = {}
        dict['to'] = to

        options_array = ['name', 'required']

        for opt in options_array:
            if opt in options:
                dict[opt] = options[opt]
        self.obj = {'redirect' : dict}
        self.json = dict


class Reject():
    """
    Python class that corresponds to "reject" json object. 
    (See https://www.tropo.com/docs/webapi/reject.htm)

    { "reject": { } } 
    """
    def __init__(self):
        dict = {}
        self.obj = {'reject' : dict}


class Result():

    """
    Python class that corresponds to "result" json object. 
    (See https://www.tropo.com/docs/webapi/result.htm)

        { "result": {
            "actions": Array or Object,
            "complete": Boolean,
            "error": String,
            "sequence": Integer,
            "sessionDuration": Integer,
            "sessionId": String,
            "state": String } }
    """ 
            
    def initOld(self, result_json):
        logging.info ("result POST data: %s" % result_json)
        result_data = simplejson.loads(result_json)
        result_dict = result_data['result']

        options_array = ['actions','complete','error','sequence', 'sessionDuration', 'sessionId', 'state']
        for opt in options_array:
            logging.info ("Result setting %s to %s" % (opt, result_dict[opt]))
            self.opt = result_dict[opt]

    def __init__(self, result_json):
        logging.info ("result POST data: %s" % result_json)
        result_data = simplejson.loads(result_json)
        result_dict = result_data['result']

        options_array = ['actions','complete','error','sequence', 'sessionDuration', 'sessionId', 'state']
        self._actions = result_dict['actions']
        self._complete = result_dict['complete']
        self._error = result_dict['error']
        self._actions = result_dict['actions']
        self._sequence = result_dict['sequence']
        self._sessionDuration = result_dict['sessionDuration']
        self._sessionId = result_dict['sessionId']
        self._state = result_dict['state']

    def getValue(self):
        # Enhance this to handle actions being an array
        actions = self._actions

#        for item in self.__dict__.(keys):
#            logging.info ("dict value: %s" % item)

#        actions = self.actions
        if (type (actions) is list):
            logging.info ("Actions is a list")
            dict = actions[0]
        else:
            logging.info ("Actions is a dict")
            dict = actions
        logging.info ("Actions is: %s" % actions)
        return dict['interpretation']

# ??? can we initialize this with an array?
class Say():
    """
    Python class that corresponds to "csay" json object. 
    (See https://www.tropo.com/docs/webapi/csay.htm)

    { "say": {
        "as": String,
        "name": String,
        "required": Boolean,
        "value": String #Required
        } } 
    """
    def __init__(self, message, **options):
        dict = {}
        options_array = ['as', 'name', 'required']
        for opt in options_array:
            if opt in options:
                dict[opt] = options[opt]
        dict['value'] = message
        self.obj = {'say' : dict}
        self.json = dict


class Session():
    def __init__(self, session_json):
        logging.info ("POST data: %s" % session_json)
        session_data = simplejson.loads(session_json)
        session_dict = session_data['session']
        for key in session_dict:
            val = session_dict[key]
            logging.info ("key: %s val: %s" % (key, val))

        for key in session_dict:
            val = session_dict[key]
            self.key = val



class StartRecording ():
    """
    { "startRecording": {
        "format": String,
        "method": String,
        "url": String,#Required
        "username": String,
        "password": String } } 
    """
    def __init__(self, url, **options):
        dict = {}
        dict['url'] = url
        options_array = ['format', 'method', 'username', 'password']

        for opt in options_array:
            if opt in options:
                dict[opt] = options[opt]
        self.obj = {'startRecording' : dict}
        self.json = dict

class StopRecording ():
   """
      { "stopRecording": { } } 
   """
   def __init__(self):
       dict = {}
       self.obj = {'stopRecording' : dict}
       self.json = dict



class Transfer():
    """
    { "transfer": {
        "to": String or Array,#Required
        "answerOnMedia": Boolean,
        "choices": Object,
        "from": Object,
        "name": String,
        "required": Boolean,
        "terminator": String,
        "timeout": Float } } 
    """
    def __init__(self, to, **options):
        dict = {}
        dict['to'] = to

        options_array = ['answerOnMedia', 'choices', 'from', 'name', 'required', 'terminator']

        for opt in options_array:
            if opt in options:
                if (opt == 'from'):
                    dict['from'] = options['from']
                elif(opt == 'choices'):
                    dict['choices'] = {'value' : options['choices']}
                else:
                    dict[opt] = options[opt]
        self.obj = {'transfer' : dict}
        self.json = dict


class Tropo():
    """
      This is the top level class for all the Tropo web api actions.
      Individual actions are each methods on this class.

      They each take one or more required arguments, followed by optional
      arguments expressed as key=value pairs.
    """
    def  __init__(self):
        self._steps = []


    def ask(self, choices, **options):
        """
	 * Sends a prompt to the user and optionally waits for a response.
	 *
	 * Argument: "message" is a String
	 *
	 * See https://www.tropo.com/docs/webapi/ask.htm
        """
        steps = self._steps
        ask_obj = Ask(choices, **options)
        piece = ask_obj.obj
        steps.append(piece)
        self._steps = steps

    def call (self, to, **options):
        """
	 * Places a call or sends an an IM, Twitter, or SMS message. To start a call, use the Session API to tell Tropo to launch your code. 
	 *
	 * @param string|Call $call
	 * @param array $params
	 * See https://www.tropo.com/docs/webapi/call.htm
        """
        steps = self._steps
        call_obj = Call (to, **options)
        piece = call_obj.obj
#        steps.append({'message' : piece})
        steps.append(piece)
        self._steps = steps

    def conference(self, id, **options):
        """
	 * This object allows multiple lines in separate sessions to be conferenced together so that the parties on each line can talk to each other simultaneously. 
	 * This is a voice channel only feature. 
	 *
 	 * Argument: "id" is a String

	 * See https://www.tropo.com/docs/webapi/conference.htm
        """
        steps = self._steps
        conference_obj = Conference(id, **options)
        piece = conference_obj.obj
        steps.append(piece)
        self._steps = steps

    def hangup(self):
        """
	 * This function instructs Tropo to "hang-up" or disconnect the session associated with the current session.
	 * See https://www.tropo.com/docs/webapi/hangup.htm
        """
        steps = self._steps
        hangup_obj = Hangup()
        piece = hangup_obj.obj
        steps.append(piece)
        self._steps = steps

    def message (self, say_obj, to, **options):
        """
	 * A shortcut method to create a session, say something, and hang up, all in one step. This is particularly useful for sending out a quick SMS or IM. 
	 *
 	 * Argument: "id" is a String
         * Argument: "to" is a String

	 * See https://www.tropo.com/docs/webapi/message.htm
        """
        steps = self._steps
        if isinstance(say_obj, str):
           say_obj1 = Say(say_obj).obj
           message_obj = Message(say_obj1, to, **options)
        else:
           message_obj = Message(say_obj, to, **options)
        piece = message_obj.obj
#        steps.append({'message' : piece})
        steps.append(piece)
        self._steps = steps


    def on(self, event, **options):
        """
	 * Adds an event callback so that your application may be notified when a particular event occurs. 
	 * Possible events are: "continue", "error", "incomplete" and "hangup". 
	 *
	 * @param array $params
	 * See https://www.tropo.com/docs/webapi/on.htm
        """
        on_obj = On(event, **options)
        steps = self._steps
        piece = on_obj.obj
#        steps.append({'on' : piece})
        steps.append(piece)
        self._steps = steps

    def record(self, **options):
        """
	 * Plays a prompt (audio file or text to speech) and optionally waits for a response from the caller that is recorded. 
	 * If collected, responses may be in the form of DTMF or speech recognition using a simple grammar format defined below. 
	 * The record funtion is really an alias of the prompt function, but one which forces the record option to true regardless of how it is (or is not) initially set. 
	 * At the conclusion of the recording, the audio file may be automatically sent to an external server via FTP or an HTTP POST/Multipart Form. 
	 * If specified, the audio file may also be transcribed and the text returned to you via an email address or HTTP POST/Multipart Form.
	 *
	 * @param array|Record $record
	 * See https://www.tropo.com/docs/webapi/record.htm
        """
        steps = self._steps
        record_obj = Record(**options)
        piece = record_obj.obj
        steps.append(piece)
        self._steps = steps


    def redirect(self, id, **options):
        """
	 * The redirect function forwards an incoming call to another destination / phone number before answering it. 
	 * The redirect function must be called before answer is called; redirect expects that a call be in the ringing or answering state. 
	 * Use transfer when working with active answered calls. 
	 *
	 * @param string|Redirect $redirect
	 * @param array $params
	 * See https://www.tropo.com/docs/webapi/redirect.htm
        """
        steps = self._steps
        redirect_obj = Redirect(id, **options)
        piece = redirect_obj.obj
        steps.append(piece)
        self._steps = steps

    def reject(self, id, **options):
        """
	 * Allows Tropo applications to reject incoming sessions before they are answered. 
	 * For example, an application could inspect the callerID variable to determine if the user is known, and then use the reject call accordingly. 
	 * 
	 * See https://www.tropo.com/docs/webapi/reject.htm
        """
        steps = self._steps
        reject_obj = Reject()
        piece = reject_obj.obj
        steps.append(piece)
        self._steps = steps

# ??? say may take an array of values
    def say(self, message, **options):
        """
	 * When the current session is a voice channel this key will either play a message or an audio file from a URL. 
	 * In the case of an text channel it will send the text back to the user via i nstant messaging or SMS. 
	 *
	 * @param string|Say $say
	 * @param array $params
	 * See https://www.tropo.com/docs/webapi/say.htm
        """
        steps = self._steps
        say_obj = Say(message, **options)
        piece = say_obj.obj
#        steps.append({'say' : piece})
        steps.append(piece)
        self._steps = steps
        return say_obj.json

    def startRecording(self, url, **options):
        """
	 * Allows Tropo applications to begin recording the current session. 
	 * The resulting recording may then be sent via FTP or an HTTP POST/Multipart Form. 
	 *
	 * @param string|StartRecording $startRecording
	 * @param array $params
	 * See https://www.tropo.com/docs/webapi/startrecording.htm
        """
        steps = self._steps
        startRecording_obj = StartRecording(url, **options)
        piece = startRecording_obj.obj
        steps.append(piece)
        self._steps = steps

    def stopRecording(self):
        """
	 * Stops a previously started recording.
	 * 
        """
        steps = self._steps
        stopRecording_obj = StopRecording()
        piece = stopRecording_obj.obj
        steps.append(piece)
        self._steps = steps

    def transfer(self, to, **options):
        """
	 * Transfers an already answered call to another destination / phone number. 
	 * Call may be transferred to another phone number or SIP address, which is set through the "to" parameter and is in URL format.
	 *
	 * @param string|Transfer $transfer
	 * @param array $params
	 * See https://www.tropo.com/docs/webapi/transfer.htm
        """
        steps = self._steps
        transfer_obj = Transfer(to, **options)
        piece = transfer_obj.obj
        steps.append(piece)
        self._steps = steps

    def RenderJson(self):
        steps = self._steps
        topdict = {}
        topdict['tropo'] = steps
        logging.info ("topdict: %s" % topdict)
        # {"tropo": [{"say": "Hello World"}]}
        json = simplejson.dumps(topdict)
        return json

    def PrettyJson(self):
        json = self.RenderJson()
        l = simplejson.loads(json)
        pretty = simplejson.dumps(l, indent=4, sort_keys=False)
        return pretty


if __name__ == '__main__':
    """
    Unit tests.
    """
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

    print tropo.PrettyJson()

