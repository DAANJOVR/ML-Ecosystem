import tkinter as tk
import speech_recognition as sr
import datetime
import subprocess
import pyttsx3
import webbrowser
import os
import cv2
import random
from tkinter import PhotoImage

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Use the second voice (female)
recognizer = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def capture_photo():
    """Function to capture a photo using the webcam."""
    speak("Taking a photo in 3 seconds. Please smile!")
    cv2.waitKey(3000)  # Wait for 3 seconds
    cap = cv2.VideoCapture(0)  # Open the webcam
    ret, frame = cap.read()  # Read a frame from the webcam
    if ret:
        photo_path = "captured_photo.jpg"  # Save the photo
        cv2.imwrite(photo_path, frame)  # Save the captured frame
        speak("Photo taken and saved.")
        output_text.set(f"Photo saved as {photo_path}.")
    else:
        speak("Sorry, I couldn't take a photo.")
    cap.release()  # Release the webcam
    cv2.destroyAllWindows()  # Close any OpenCV windows

def open_website(website_name):
    """Open a website based on the user's command."""
    websites = {
        'youtube': 'https://www.youtube.com',
        'facebook': 'https://www.facebook.com',
        'google': 'https://www.google.com',
        'x': 'https://www.x.com',
        'instagram': 'https://www.instagram.com',
        'github':'https://www.github.com',
        'wikipedia':'https://en.wikipedia.com',
        'reddit':'https://www.reddit.com',
        'music':'https://music.youtube.com/watch?v=CKpbdCciELk&list=OLAK5uy_lk4hlzR_Y1Mk5x6hjZJbwNgugWtMlrj3I',
    }
    
    # Check if the website is in the dictionary, otherwise search it on Google
    website_url = websites.get(website_name, f"https://www.google.com/search?q={website_name}")
    
    webbrowser.open(website_url)
    speak(f"Opening {website_name}.")
    output_text.set(f"Opening {website_name}.")

def play_rock_paper_scissors(user_choice):
    """Play a simple game of Rock, Paper, Scissors."""
    choices = ['rock', 'paper', 'scissors']
    assistant_choice = random.choice(choices)
    
    # Determine the winner
    if user_choice == assistant_choice:
        result = "It's a tie!"
    elif (user_choice == 'rock' and assistant_choice == 'scissors') or \
         (user_choice == 'paper' and assistant_choice == 'rock') or \
         (user_choice == 'scissors' and assistant_choice == 'paper'):
        result = "You win!"
    else:
        result = "I win!"
    
    speak(f"You chose {user_choice}. I chose {assistant_choice}. {result}")
    output_text.set(f"You chose {user_choice}. I chose {assistant_choice}. {result}")

def process_command(text):
    """Process the recognized speech command."""
    # Convert the text to lower case to make it case-insensitive
    text = text.lower()

    if 'chrome' in text:
        speak('Opening Chrome..')
        program = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        subprocess.Popen([program])
        output_text.set("Chrome opened.")

    elif 'time' in text:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}.")
        output_text.set(f"The current time is {current_time}.")

    elif 'search for' in text:
        search_query = text.replace("search for", "").strip()
        url = f"https://www.google.com/search?q={search_query}"
        webbrowser.open(url)
        speak(f"Here are the search results for {search_query}.")
        output_text.set(f"Searching for: {search_query}")

    elif 'send a message' in text:
        message = text.replace("send a message", "").strip()
        speak("Message sent!")  # Placeholder response
        output_text.set(f"Message sent: {message}")

    elif 'open notepad' in text:
        speak('Opening Notepad..')
        subprocess.Popen(['notepad.exe'])
        output_text.set("Notepad opened.")

    elif 'open file explorer' in text:
        speak('Opening File Explorer..')
        subprocess.Popen('explorer')
        output_text.set("File Explorer opened.")

    elif 'open camera' in text:
        speak('Opening Camera..')
        subprocess.Popen('start microsoft.windows.camera:', shell=True)
        output_text.set("Camera opened.")

    elif 'take a photo' in text:
        capture_photo()  # Call the function to take a photo

    elif 'open' in text:
        # Check if the command is to open a website
        website_name = text.replace("open", "").strip()  # Remove "open" from the command
        if website_name:
            open_website(website_name)

    elif 'rock' in text or 'paper' in text or 'scissors' in text:
        # Play rock, paper, scissors
        user_choice = ''
        if 'rock' in text:
            user_choice = 'rock'
        elif 'paper' in text:
            user_choice = 'paper'
        elif 'scissors' in text:
            user_choice = 'scissors'
        
        if user_choice:
            play_rock_paper_scissors(user_choice)
        else:
            speak("Please specify rock, paper, or scissors.")
            output_text.set("Please specify rock, paper, or scissors.")

    else:
        # Placeholder response for unrecognized commands
        speak("Sorry, I didn't understand that.")
        output_text.set("Sorry, I didn't understand that.")

def record_speech():
    """Function to record speech and process the command."""
    with sr.Microphone() as source:
        output_text.set("Clearing background noises... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        output_text.set("Listening... Please speak now.")
        
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio).lower()
            output_text.set(f"Recognized Text: {text}")
            process_command(text)
        except sr.UnknownValueError:
            output_text.set("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            output_text.set(f"Could not request results; {e}")
        except Exception as e:
            output_text.set(f"An error occurred: {e}")

# Set up the GUI
root = tk.Tk()
root.title("ATLAS-Voice Assistant")
root.geometry("400x300")

# Load the background image
bg_image = PhotoImage(file="assistant.gif")  # Make sure the image is in the same directory
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Label to display the instructions
instruction_label = tk.Label(root, text="Press 'Record' and start speaking:", bg="white", font=("Arial", 12))
instruction_label.pack(pady=10)

# Button to start recording
record_button = tk.Button(root, text="Record", command=record_speech, font=("Arial", 12), bg="lightblue")
record_button.pack(pady=10)

# Text box to display the recognized text and responses
output_text = tk.StringVar()
output_text.set("Press 'Record' to start.")
output_label = tk.Label(root, textvariable=output_text, wraplength=300, justify="center", bg="white", font=("Arial", 12))
output_label.pack(pady=10)

# Run the GUI event loop
root.mainloop()
