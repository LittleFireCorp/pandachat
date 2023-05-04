import speech_recognition as sr
import pyttsx3
import openai

# Init

forever = 220 

def doGetSpeechFromUser():
    """
    """
    audio2 = None
    print('do get speech from user')

    # Initialize the recognizer
    r = sr.Recognizer()
    try:
        # use the microphone as source for input.
        with sr.Microphone() as source2:
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)

            # listens for the user's input
            audio2 = r.listen(source2)

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occurred")
    return audio2

def doTransformSpeechToTxt(audio):
    """
    """
    # Initialize the recognizer
    r = sr.Recognizer()
    text = ""
    print('transform speech to text')
    try:
        text = r.recognize_google(audio)
    except:
        print("ERROR")

        
    text = text.lower()
    print(text)
    return text

def doTalkToGpt(prompt):
    """
    """
    reply = None
    print('talking to gpt')
    return reply

def doSpeak(text):
    """
    """
    print('Speak')
    return




while(forever):
       audio = doGetSpeechFromUser()
       #print(type(audio))

       prompt = doTransformSpeechToTxt(audio)

       reply = doTalkToGpt(prompt)

       doSpeak(reply)

       forever = forever -1 

