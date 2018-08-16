# tests fix of gh-14 for "from" parameter in the "call" function. 
# Proposed convention is to use "_from" as the parameter
# so as not to conflict with "from" Python reserved word.

# _from arg works

# Invoke using a token

# Sample application using the itty-bitty python web framework from:
#  http://github.com/toastdriven/itty

import sys
sys.path = ['..'] + sys.path

from itty import *
from tropo import Tropo, Session

TO_NUMBER = '13072238293'
FROM_NUMBER = '14076021088'


@post('/index.json')
def index(request):
    #s = Session(request.body)
    t = Tropo()
    t.call(to=' ' + TO_NUMBER, _from=' ' + FROM_NUMBER, label='xiangwyujianghu', network = 'MMS')
    mediaa = ['http://www.gstatic.com/webp/gallery/1.jpg', 'macbook eclipse', 'http://artifacts.voxeolabs.net.s3.amazonaws.com/test/test.png', 1234567890, '0987654321', 'https://www.travelchinaguide.com/images/photogallery/2012/beijing-tiananmen-tower.jpg']
    t.say('This is your mother. Did you brush your teeth today?', media = mediaa)
    json = t.RenderJson() 
    print json
    return json


run_itty(server='wsgiref', host='127.0.0.1', port=8083)

