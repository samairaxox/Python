import pyttsx3
Robo = pyttsx3.init()
Robo.setProperty('rate', 125)  # Lower value = slower speech

print("Welcome to Robo-Speaker")
while True:
    user_input = input("What do you want to me to say(Enter 0 to exit):")
    if user_input=="0":
        break
    else:
        print(user_input)
        Robo.say(user_input)
        Robo.runAndWait()