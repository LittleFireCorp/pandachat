import os
import pyaudio
import speech_recognition as sr
import pyttsx3
import openai

openai.api_key = "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"

# Init

forever = 20



def list_engines():
    engines = openai.Engine.list()
    for engine in engines['data']:
        print(engine)
    return


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
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )
    reply_text = response.choices[0].text
    return reply_text.strip()


def do_speak(text):
    """
    """
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    return


while forever:
    audio = do_get_speech_from_user()
    # print(type(audio))

    prompt = do_transform_speech_to_txt(audio)

    reply = do_talk_to_gpt(prompt)

    do_speak(reply)

    forever = forever - 1
