# tests example clarifying gh-23 . How to use timeout, and nomatch parameters
# in "say" within "ask"


from itty import *
from tropo import Tropo, Session, Result


@post("/index.json")
def index (request):
    t = Tropo()
    t.ask(choices = "[4 DIGITs]", 
          timeout=5,
          bargein="true",
          name="year",
          attempts=3,
          required="true",
          say = [{'event':'timeout',
                  'value':"Sorry, I did not hear anything"},
                 {'event':'nomatch:1',
                  'value':"Don't think that was a year."},
                 {'event':'nomatch:2',
                  'value':"Nope, still not a year."},
                 {'value': "What is your birth year?"}
                 ])   

    json = t.RenderJson()
    print json
    return json



# @post("/index.json")
def index_straight_json (request):
    json = """{
    "tropo":[
      {
         "ask":{
            "attempts":3,
            "say":[
               {
                  "value":"Sorry, I did not hear anything.",
                  "event":"timeout"
               },
               {
                  "value":"Don't think that was a year. ",
                  "event":"nomatch:1"
               },
               {
                  "value":"Nope, still not a year.",
                  "event":"nomatch:2"
               },
               {
                  "value":"What is your birth year?"
               }
            ],
            "choices":{
               "value":"[4 DIGITS]"
            },
            "bargein":true,
            "timeout":5,
            "name":"year",
            "required":true
         }
      }
   ]

}
"""
    print json
    return json








run_itty()
