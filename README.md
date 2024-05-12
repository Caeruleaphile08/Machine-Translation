# Speech to Hindi Translation

This project is a simple Python script that converts speech to text using the Google Speech Recognition API and translates the text to Hindi using the Google Translate API.

## Requirements

- Python 3.x
- `speech_recognition` library
- `googletrans` library

You can install the required libraries using pip:

```bash
pip install SpeechRecognition googletrans==4.0.0-rc1
pip install googletrans
```

## Problem Statement  

Creating a feature to translate the audio into Hindi. The system will listen the english audio from user and it will convert into Hindi word. If the system does not understand the audio it will ask repeat one more time to make it better.. The audio should be in English word only. This translation feature work on only after 6 PM IST timing and before that it should show message like please try after 6 PM IST as well as it should not translate any english which is start with M and O apart from that it should translate all other words.

## Usage

1. Run the `main.py` file.
2. Ensure that your microphone is connected and functional.
3. After 6 PM IST, the program will listen for your speech input.
