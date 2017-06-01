import sys
sys.path = ['..'] + sys.path
from itty import *
from tropo import Tropo, Session, Result

@post('/index')
def index(request):

    t = Tropo()
    t.call("+8613466549249")
    t.startRecording('http://12b12d1b.ngrok.io/FileUpload/uploadFile', formamt = 'audio/wav', transcriptionID = "20170601startRecording", transcriptionEmailFormat = "plain", transcriptionOutURI = "http://12b12d1b.ngrok.io/FileUpload/receiveJson") 
    t.say("a b c d e f g h i j k l m n o p q r s t u v w x y z @  # $ % & ")
    t.say(" I love my daughter")
    t.say("1 2 3 4 5 6 7 8 9 0 A B C D E F G")
    t.say("today is Thursday 2017-06-01")
    t.stopRecording()
    return t.RenderJson()
	
run_itty(server='wsgiref', host='192.168.26.1', port=8085)
