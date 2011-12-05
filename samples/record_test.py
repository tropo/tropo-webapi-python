from itty import *
from tropo import Tropo, Session, Result

@post('/index')
def index(request):

    t = Tropo()
    VOICE = 'Grace' 

    t.record(name='voicemail.mp3', say='Your call is important. Please leave a short message after the tone: ', url = 'http://www.example.com', beep = True, format = 'audio/mp3', voice = VOICE) 

    return t.RenderJson()
	
run_itty(server='wsgiref', port=8888)