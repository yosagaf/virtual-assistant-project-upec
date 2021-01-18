# text preprocessing
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
import time
import playsound
from gtts import gTTS
import numpy as np
import os
import speech_recognition as sr

# emotion classification on the text answer
def extractEmotion(text):
    
    class_names = ['joy', 'fear', 'anger', 'sadness', 'neutral']
    
    # Max input length (max number of words) 
    max_seq_len = 500

    model = load_model('nlp-text/models/cnn_w2v.h5')
    
    tokenizer = Tokenizer()
    seq = tokenizer.texts_to_sequences(text)
    padded = pad_sequences(seq, maxlen=max_seq_len)

    start_time = time.time()
    pred = model.predict(padded)

    print('\n\nMessage : ' + str(text))
    print('\n\nPredicted : {} ({:.2f} seconds)'.format(class_names[np.argmax(pred)], (time.time() - start_time)))

print("\n\n")
#message = ['delivery was hour late and my pizza was cold!']

# 
def text2speech(text):
    output = gTTS(text=text, lang='en', slow=False)
    file = "output.mp3"
    output.save(file)
    playsound.playsound(file)
    os.remove(file)

# Call of this function will start audio recording
# Speech recognition using Google Speech Recognition
def speech2text():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("\n\nPlease, start recording :")
        r.adjust_for_ambient_noise(source)
        audio= r.listen(source)
        said = ""
        print("Heeeeeeeeeeeeeeeey")
    try:
        said = r.recognize_google(audio)
        print("\n\nYous said :", said)
    except sr.UnknownValueError:
        print("\n\nGoogle Speech Recognition could not understand audio")
    except Exception as e:
        print("Exception: " + str(e))
    return said

# Process : speak on the mic and you will get a string containing the message.
# The message is passed on the text to speech and then we can extract the emotion.

#message = speech2text()
#text2speech(message)
#extractEmotion(message)
