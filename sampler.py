import mido, os, pyaudio, wave
from playsound import playsound

outport = mido.open_output('Launchpad S 1')
inport = mido.open_input('Launchpad S 0')

soundfile = os.getcwd() + '/example_sounds/beep-07.wav'

# file recording 
recordedfile = os.getcwd() + '/example_sounds/recorded.wav'


while(True):
    msg = inport.receive()
    playsound(soundfile,False)
    outport.send(msg)