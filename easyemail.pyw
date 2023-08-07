from dotenv import load_dotenv, dotenv_values
from time import sleep
import keyboard

class EasyEmail:
    def __init__(self):
        load_dotenv()

    def startListeners(self):
        keyboard.add_hotkey('ctrl+shift+1', lambda: self.writeData("1"))
        keyboard.add_hotkey('ctrl+shift+2', lambda: self.writeData("2"))
        keyboard.add_hotkey('ctrl+shift+3', lambda: self.writeData("3"))
        keyboard.add_hotkey('ctrl+shift+4', lambda: self.writeData("4"))
        keyboard.add_hotkey('ctrl+shift+5', lambda: self.writeData("5"))

        while True:
            sleep(10000000)
            self.startListener()

    def writeData(self, option):
        pass

    def startListener(self):
        while True:
            if keyboard.is_pressed('ctrl+shift+1'):
                print("Written!")
                self.writeEmail()
                break

    def writeEmail(self):
        email = dotenv_values(".env")["EMAIL"]
        keyboard.write(email)
        self.startListener()

easyemail = EasyEmail()
easyemail.startListener()