
import speech_recognition as sr

def recognize_speech():
    # Create a recognizer instance
    recognizer = sr.Recognizer()
    
    # Use microphone as source
    with sr.Microphone() as source:
        print("Listening... Speak now!")
        
        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)
        
        # Listen for audio input
        #audio = recognizer.listen(source)
        audio = recognizer.listen(source, 
                                timeout=1,  # Wait up to X seconds for phrase to start
                                phrase_time_limit=15)
        
        try:
            # Use Google's speech recognition
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
            
        except sr.UnknownValueError:
            print("Could not understand the audio")
        except sr.RequestError:
            print("Could not request results")

def transcribe_audio_file(file_path):
    recognizer = sr.Recognizer()
    
    # Load the audio file
    with sr.AudioFile(file_path) as source:
        # Record the audio data
        audio = recognizer.record(source)
        
        try:
            # Convert speech to text
            text = recognizer.recognize_google(audio)
            print(f"Transcription: {text}")
            return text
            
        except sr.UnknownValueError:
            print("Could not understand the audio")
        except sr.RequestError:
            print("Could not request results")

# Example usage
#file_path = "path/to/your/audiofile.wav"
#transcribe_audio_file(file_path)

"""
recognize_sphinx() for offline recognition
recognize_wit() for Wit.ai
recognize_bing() for Microsoft Azure
recognize_ibm() for IBM Speech to Text
"""

if __name__ == "__main__":
    recognize_speech()