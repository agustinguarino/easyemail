import keyboard
from dotenv import load_dotenv

class EasyEmail:
    def __init__(self):
        load_dotenv()

    def startListener(self):
        while True:
            if keyboard.is_pressed('ctrl+1'):
                print("Test")
                self.writeEmail()
                break

    def writeEmail(self):
        pass

easyemail = EasyEmail()
easyemail.startListener()