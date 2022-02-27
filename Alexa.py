# אחרי שעושים פייאינסטלר, האייקון של התוכנית הוא לא האייקון של החלון (בשורת המשימות כן, בתיקייה לא)
#  התוכנית לא עובדת בלי הקונסול
# ניסיון לסגור אותה גורם לה להיתקע ואז לקרוס

import speech_recognition as sr
import pyttsx3 as p3
import pywhatkit
import datetime
import webbrowser
import os

# creating a listener variable using the sr package
listener = sr.Recognizer()
engine = p3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    print(text)
    engine.say(text)
    engine.runAndWait()


def take_command():
    # using a try clause so nothing will happen if a voice wasn't recognized
    try:
        # declaring the microphone as the speech source
        with sr.Microphone() as source:
            print('listening...')
            # creating a variable to store the input from the source
            voice = listener.listen(source)
            # using a method to process the audio
            command = listener.recognize_google(voice)
            # making the converted text lowercase to check if it consists the keyword:
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
            print(command)
    except:
        pass
    return command


def run_alexa():
    talk('Hello Danielle, what can I do for you?')
    command = take_command()
    if 'play' in command:
        command = command.replace('play', '')
        talk('would you like me to play ' + command)
        answer = take_command()
        if 'yes' in answer:
            talk('playing ' + command)
            pywhatkit.playonyt(command)
        elif 'no' in answer:
            pass
    if 'time' in command:
        time = datetime.datetime.now().strftime('%H %M')
        talk('Current time is ' + time)
    elif 'date' in command:
        date = datetime.datetime.now().date().strftime('%d/%m/%y')
        talk("the date today is " + date)
    # elif 'mail myself' in 'command':
    #     talk('what should I write in the mail?')
    #     content = take_command()
    #     talk('writing ')
    elif 'youtube' in command:
        talk('what would you like me to search in youtube?')
        answer = take_command()
        talk('searching in youtube ' + answer)
        url = "https://www.youtube.com.tr/search?q={}".format(answer)
        webbrowser.open(url)
    elif 'google' in command:
        talk('what would you like me to search in google?')
        answer = take_command()
        talk('searching in google ' + answer)
        url = "https://www.google.com.tr/search?q={}".format(answer)
        webbrowser.open(url)
    elif 'balance' in command:
        talk('opening your Balance excel spreadsheet')
        os.startfile("C:/Users/danie/Desktop/דניאל/כללי/פיננסי/balance.xlsx")
    elif 'reminder' in command:
        talk('what should I write to boti?')
        answer = take_command()
        talk('sending boti your massage')
        now = datetime.datetime.now()
        now_hour = int(now.hour)
        now_minute = int(now.minute + 2)
        pywhatkit.sendwhatmsg('+972559847775', answer, now_hour, now_minute, 40)
    elif 'myself' in command:
        talk('what should I write to yourself?')
        answer = take_command()
        talk('sending you the message')
        now = datetime.datetime.now()
        now_hour = int(now.hour)
        now_minute = int(now.minute + 1)
        pywhatkit.sendwhatmsg_to_group('HEnaJiiLRcbCszDzc7dLb5', answer, now_hour, now_minute)


run_alexa()
