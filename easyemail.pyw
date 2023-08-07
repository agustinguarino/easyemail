from dotenv import load_dotenv, dotenv_values
from time import sleep
import keyboard

class EasyEmail:
    def __init__(self):
        load_dotenv()
        self.startListeners()

    def startListeners(self):
        keyboard.add_hotkey('o+1', lambda: self.writeData("1"))
        keyboard.add_hotkey('o+2', lambda: self.writeData("2"))
        keyboard.add_hotkey('o+3', lambda: self.writeData("3"))
        keyboard.add_hotkey('o+4', lambda: self.writeData("4"))
        keyboard.add_hotkey('o+5', lambda: self.writeData("5"))
        while True:
            sleep(10000000)
            self.startListeners()

    def writeData(self, option):
        self.prepareForInput()
        option_data = dotenv_values(".env")[f"OPTION{option}"]
        keyboard.write(option_data)

    def prepareForInput(self):
        keyboard.press_and_release("backspace")
        keyboard.press_and_release("backspace")

easyemail = EasyEmail()