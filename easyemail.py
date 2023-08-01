import keyboard
from dotenv import load_dotenv, dotenv_values

class EasyEmail:
    def __init__(self):
        load_dotenv()

    def startListener(self):
        while True:
            if keyboard.is_pressed('ctrl+shift+1'):
                print("Test")
                self.writeEmail()
                break

    def writeEmail(self):
        email = dotenv_values(".env")["EMAIL"]
        keyboard.write(email)
        self.startListener()

easyemail = EasyEmail()
easyemail.startListener()