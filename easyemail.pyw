from dotenv import load_dotenv, dotenv_values
from time import sleep
import keyboard

class EasyEmail:
    def __init__(self):
        load_dotenv()

    def startListeners(self):
        print("Test 1")
        keyboard.add_hotkey('ctrl+alt+1', lambda: self.writeData("1"))
        keyboard.add_hotkey('ctrl+alt+2', lambda: self.writeData("2"))
        keyboard.add_hotkey('ctrl+alt+3', lambda: self.writeData("3"))
        keyboard.add_hotkey('ctrl+alt+4', lambda: self.writeData("4"))
        keyboard.add_hotkey('ctrl+alt+5', lambda: self.writeData("5"))
        print("Test 2")

        while True:
            sleep(10000000)
            self.startListener()

    def writeData(self, option):
        print("Test 3")
        option_data = dotenv_values(".env")[f"OPTION{option}"]
        keyboard.write(option_data)
        print("Test 4")

easyemail = EasyEmail()
#easyemail.startListener()
easyemail.startListeners()