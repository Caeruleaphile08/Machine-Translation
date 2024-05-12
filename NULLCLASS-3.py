import speech_recognition as sr
from googletrans import Translator
import datetime

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

def startConversion():
    with sr.Microphone() as source:
        print('Listening...')
        audio_text = r.listen(source)
        print('Done Listening...')
        # recognize_() method will throw a request error if the API is unreachable, hence using exception handling
        try:
            # using google speech recognition
            print('Converting audio transcript into text ...')
            text = r.recognize_google(audio_text, language='en-IN')
            print('Recognized text:', text)
            return text
        except sr.UnknownValueError:
            print('Sorry, Please repeat one more time.')
        except sr.RequestError as e:
            print('Sorry, an error occurred while trying to request results from Google Speech Recognition service:', e)

def translate_to_hindi(text):
    translator = Translator()
    translation = translator.translate(text, src="en", dest="hi")
    print("Translated text:", translation.text)

if __name__ == '__main__':
    current_time = datetime.datetime.now()
    if current_time.hour < 18:
        print("Translation feature works only after 6 PM IST.")
    else:
        english_text = startConversion()
    
    translate_to_hindi(english_text)
