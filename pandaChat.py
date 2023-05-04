import os
import SpeechRecognition as sr
import pyttsx3
import openai

# Init

forever = 20


def do_get_speech_from_user():
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


def do_transform_speech_to_txt(audio):
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


def do_talk_to_gpt(prompt):
    """
    """
    reply = None
    print('talking to gpt')
    return reply


def do_speak(text):
    """
    """
    print('Speak')
    return


while forever:
    audio = do_get_speech_from_user()
    # print(type(audio))

    prompt = do_transform_speech_to_txt(audio)

    reply = do_talk_to_gpt(prompt)

    do_speak(reply)

    forever = forever - 1
