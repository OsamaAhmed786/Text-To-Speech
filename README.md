# Text-to-Speech (TTS) Synthesis Project

### Overview

The Text-to-Speech (TTS) Synthesis Project is a Python-based application that demonstrates the conversion of text into speech using the gTTS (Google Text-to-Speech) library. This project allows users to input text, which is then converted into speech and saved as an MP3 audio file. Additionally, the project includes functionality to automatically increment the filename to avoid overwriting existing files when saving multiple speech outputs.

### Features

1. **Text-to-Speech Conversion:** Users can input text of their choice, and the application will use gTTS to convert the text into speech in the English language.

2. **Auto-Incrementing Filenames:** The project ensures that saved MP3 files have unique filenames by automatically incrementing the filename for each new speech output.

### Installation and Setup

1. **Python Environment:** Ensure you have a Python environment set up. You can download Python from the official website (https://www.python.org/).

2. **Library Installation:** Install the necessary Python libraries using pip:

    ```bash
    pip install gtts
    pip install pygame
    pip install os
    ```

### Usage

1. **Run the Application:** Execute the Python script in your terminal or preferred development environment.

2. **Enter Text:** The application will prompt you to enter the text you want to convert to speech.

3. **Generated Speech:** The program will generate speech from the input text using gTTS and save it as an MP3 file in the specified directory.

4. **Auto-Incremented Filenames:** To avoid overwriting existing files, the filenames of the saved MP3s will be automatically incremented (e.g., "output_1.mp3," "output_2.mp3," and so on).

### Directory Structure

- `main.py`: The main Python script that provides the TTS functionality.
- `output_directory/`: The directory where generated MP3 files are saved.

### Dependencies

- GTTS: The library used for text-to-speech conversion.
- pygame: Used for playing the generated speech.
- os: The library used for join paths.

### Future Enhancements

This project serves as a basic example of TTS synthesis. Future enhancements could include:
- Support for multiple languages and language selection.
- Improved error handling and user input validation.
- A graphical user interface (GUI) for a more user-friendly experience.

### Contributors

- Osama Ahmed

### License

MIT license

