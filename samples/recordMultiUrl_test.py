import sys
sys.path = ['..'] + sys.path
from itty import *
from tropo import Tropo, Session, Result, Transcription, RecordUrlTuple

@post('/index')
def index(request):

    t = Tropo()
    VOICE = 'Grace' 
    
    transcriptionobj = Transcription(id = "tropo-12123", url = "http://192.168.26.88:8080/FileUpload/uploadFile", language = "English").json
    recordURLobj1 = RecordUrlTuple(url = "http://192.168.26.88:8080/FileUpload/uploadFile1", username = "fakename1", password="fakepassword", method="POST").json
    recordURLobj2 = RecordUrlTuple(url = "http://192.168.26.88:8080/FileUpload/uploadFile", username = "fakename2", password="fakepassword", method="POST").json
    recordURLobj3 = RecordUrlTuple(url = "http://192.168.26.88:8080/FileUpload/uploadFile3", username = "fakename3", password="fakepassword", method="POST").json
    recordURLobj4 = RecordUrlTuple(url = "http://192.168.26.88:8080/FileUpload/uploadFile4", username = "fakename4", password="fakepassword", method="POST").json

    t.record(url = [recordURLobj1, recordURLobj2, recordURLobj3, recordURLobj4],transcription = transcriptionobj, name='voicemail.wav', say='Your call is important. Please leave a short message after the tone: ', beep = True, formamt = 'audio/wav', sensitivity = 5.3) 

    return t.RenderJson()
	
run_itty(server='wsgiref', host='192.168.26.1', port=8888)
