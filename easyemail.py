import keyboard, pyperclip

class EasyEmail:
    def __init__(self):
        pass

    def startListener(self):
        while True:
            if keyboard.is_pressed('ctrl+1'):
                print("Test")
                break

    def copyToClipboard(self):
        pass