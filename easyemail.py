import keyboard

class EasyEmail:
    def __init__(self):
        pass

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