''' Before Using the Program, Install these two libraries in your system,
namely, "gtts" and "playsound".'''
'''
Step 1: Open Command Prompt as administrator.
Step 2: write command: "pip install gtts".
Step 3: write command: "pip install playsound==1.2.2".
You are good to go Now:)              
'''

import gtts
import playsound

print("Welcome to RoboSpeaker 1.1. Created by Kushagra:)")
while True:
    text = input("Enter what you want me to speak:")
    if text == "stop":
        print("")
        break
    sound = gtts.gTTS(text, lang="en")
    sound.save("welcome.mp3")
    playsound.playsound("welcome.mp3")
