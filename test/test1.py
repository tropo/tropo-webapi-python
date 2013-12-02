import sys
sys.path = ['..'] + sys.path
from tropo import Choices, MachineDetection, JoinPrompt, LeavePrompt, On, Ask, Say, Tropo

t = Tropo()

#CPA
mc = MachineDetection(introduction="THis is a CPA test", voice="Victor").json
t.call("+14071234321", machineDetection=mc)

#CPA with Boolean value which will detect CPA with 30 seconds of silence. 
t.call("+14071234321", machineDetection=True)


#Conference with join/leave prompts
jp = JoinPrompt(value="Someone just joined the conference", voice="Victor").json
lp = LeavePrompt(value="Someone just left the conference", voice="Victor").json
t.conference(id="1234", joinPrompt=jp, leavePrompt=lp)


whisper = {}

c = Choices(value="1", mode="dtmf")
ask = Ask(say="Press 1 to accept this call", choices=c).json
whisper["ask"] = ask

say = Say("You are now being connected to the call").json
whisper["say"] = say

say1 = Say("http://www.phono.com/audio/holdmusic.mp3").json
whisper["ring"] = say1

t.transfer(to="+14071234321", on=whisper)
t.on(event="incomplete", say="You are now being disconnected. Goodbye")

print t.RenderJson()

