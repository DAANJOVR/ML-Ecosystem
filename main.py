import speech_recognition as sr
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser
import os
import openai


# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Assuming you want to use the second voice
recognizer = sr.Recognizer()


# Set your OpenAI API key
openai.api_key = "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"  # Use environment variable for security


def speak(text):
   engine.say(text)
   engine.runAndWait()


def get_ai_response(question):
   """Get a response from the OpenAI API."""
   try:
       response = openai.ChatCompletion.create(
           model="gpt-3.5-turbo",
           messages=[{"role": "user", "content": question}]
       )
       return response.choices[0].message['content'].strip()
   except Exception as e:
       print(f"Error communicating with OpenAI: {e}")
       return "I'm sorry, I couldn't get a response from the AI."


def cmd():
   with sr.Microphone() as source:
       print('Clearing background noises.. Please wait')
       recognizer.adjust_for_ambient_noise(source, duration=0.5)
       print('Ask me anything..')
       recorded_audio = recognizer.listen(source)


   try:
       text = recognizer.recognize_google(recorded_audio, language='en-US')
       text = text.lower()
       print('Your message:', format(text))


       if text:
           response = get_ai_response(text)
           speak(response)


       elif 'chrome' in text:
           speak('Opening Chrome..')
           program = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
           subprocess.Popen([program])


       elif 'time' in text:
           current_time = datetime.datetime.now().strftime("%H:%M")
           speak(f"The current time is {current_time}.")


       elif 'search' in text:
           search_query = text.replace("search", "").strip()
           url = f"https://www.google.com/search?q={search_query}"
           webbrowser.open(url)
           speak(f"Here are the search results for {search_query}.")


       elif 'send a message' in text:
           message = text.replace("send a message", "").strip()
           # You can specify a number or a predefined contact here
           # Example: pywhatkit.sendwhatmsg("+1234567890", message, 10, 0)
           speak("Message sent!")  # Placeholder response


       elif 'notepad' in text:
           speak('Opening Notepad..')
           subprocess.Popen(['notepad.exe'])


       else:
           speak("I'm sorry, I didn't understand that.")


   except Exception as ex:
       print(ex)
       speak("Sorry, I couldn't process your request.")


# Call the cmd function to start the process
while True:
   cmd()
