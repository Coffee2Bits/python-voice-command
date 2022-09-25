"""An pvc function module."""
from pvc import sounds

def run():
    """Run the program."""
    print("I'm alive!")
    sounds.play_sound("/workspace/python-voice-command/resources/Ding-sound-effect.wav")
