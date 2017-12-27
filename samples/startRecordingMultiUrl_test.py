import sys
sys.path = ['..'] + sys.path
from itty import *
from tropo import Tropo, Session, Result, RecordUrlTuple

@post('/index')
def index(request):

    t = Tropo()
    t.say("A B C song")
    recordURLobj1 = RecordUrlTuple(url = "http://192.168.26.88:8080/FileUpload/uploadFile1", username = "fakename1", password="fakepassword", method="POST").json
    recordURLobj2 = RecordUrlTuple(url = "http://192.168.26.88:8080/FileUpload/uploadFile", username = "fakename2", password="fakepassword", method="POST").json
    recordURLobj3 = RecordUrlTuple(url = "http://192.168.26.88:8080/FileUpload/uploadFile3", username = "fakename3", password="fakepassword", method="POST").json
    recordURLobj4 = RecordUrlTuple(url = "http://192.168.26.88:8080/FileUpload/uploadFile4", username = "fakename4", password="fakepassword", method="POST").json
    
    t.startRecording([recordURLobj1, recordURLobj2, recordURLobj3, recordURLobj4], formamt = 'audio/wav', transcriptionID = "20170601startRecording", transcriptionEmailFormat = "plain", transcriptionLanguage = "en-usa", transcriptionOutURI = "http://12b12d1b.ngrok.io/FileUpload/receiveJson") 
    t.say("a b c d e f g h i j k l m n o p q r s t u v w x y z now you know your a b c start sing with me ")
    t.say("Merry Christmas and happy new year")
    t.say("1 2 3 4 5 6 7 8 9 0 A B C D E F G")
    t.say("today is Thursday 2017-12-25")
    t.stopRecording()
    t.hangup()
    return t.RenderJson()
	
run_itty(server='wsgiref', host='192.168.26.1', port=8085)
