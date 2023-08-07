# EasyEmail

## About

The objective of this program is to reduce the amount of time spent on typing long/repetitive pieces of text (like my incredibly long email I need to type regularly).

By pressing the combination **O+1/2/3/4/5,** you will be able to auto type any text you want.

## Requirements

In order to use this program, you will need to [install the latest version of Python](https://www.python.org/downloads/) for your OS (make sure to add Python to PATH while installing)

Once installed, you need to install two dependencies in order for the program to work.

To do this, open your cmd and execute the following commands:

    pip install keyboard
    pip install python-dotenv

## Cloning the code

Clone the respository or dowbload it and place at a path of your preference.


## Set up

### .env file

At the same folder where the file called "easyemail.pyw" is, you will find a file called **.env**, open it and after every option, fill with the text you want to be typed when you press the shortcut. (O=1 will trigger OPTION1, O=2 will trigger OPTION2, and so on...).

    OPTION1=example@gmail.com
    OPTION2=git status

Replace the example email with your email/text.

### Auto start on boot

If you want to start "easyemail.pyw" every time on boot, do this:

 1. Right click the file called "easyemail.pyw", create a shortcut and copy/cut it.
 2. Press Windows Key + R (to open Run), type "%appdata%" and click "OK".
 3. Open folder Microsoft. Windows, Start Menu and Programs.
 4. Paste the shortcut there.
 5. You're ready to go, program will auto execute every time on boot.


### First launch

If you just downloaded the program and don't want to reboot the system in order to start using it, double click the file called "easyemail.pyw". You won't see any window, but it should start working.
