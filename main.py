import os
from gtts import gTTS
import pygame

def get_next_filename(base_filename):
    # Extract the file extension (e.g., '.mp3')
    base_filename='[Your Path/output.mp3]'
    name, extension = os.path.splitext(base_filename)
    
    # Initialize a counter
    count = 1
    
    # Keep incrementing the counter until a unique filename is found
    while os.path.exists(f"{name}_{count}{extension}"):
        count += 1
    
    return f"{name}_{count}{extension}"

def text_to_speech(text, base_filename='output.mp3'):
    output_file = get_next_filename(base_filename)  # Get the next available filename
    tts = gTTS(text, lang='en')  # Create a gTTS object with text and language
    tts.save(output_file)  # Save the speech as an MP3 file
    pygame.mixer.init()
    pygame.mixer.music.load(output_file)  # Load the MP3 file
    pygame.mixer.music.play()  # Play the speech

if __name__ == "__main__":
    text = input("Enter the text you want to convert to speech: ")
    text_to_speech(text)
    input("Press Enter to exit...")

