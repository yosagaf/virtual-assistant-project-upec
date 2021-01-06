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

# emotion classification basedon on the text answer
def extractEmotion(text):
    
    class_names = ['joy', 'fear', 'anger', 'sadness', 'neutral']
    
    # Max input length (max number of words) 
    max_seq_len = 500

    model = load_model('nlp-text/models/cnn_w2v.h5')
    
    tokenizer = Tokenizer()
    seq = tokenizer.texts_to_sequences(message)
    padded = pad_sequences(seq, maxlen=max_seq_len)

    start_time = time.time()
    pred = model.predict(padded)

    print('Message: ' + str(message))
    print('predicted: {} ({:.2f} seconds)'.format(class_names[np.argmax(pred)], (time.time() - start_time)))

print("\n\n")
message = ['delivery was hour late and my pizza was cold!']

def text2speech(text):
    output = gTTS(text=text, lang='en', slow=False)
    file = "output.mp3"
    output.save(file)
    os.system("start output.mp3")
    playsound.playsound(file)

#text2speech(str(message))
#extractEmotion(message)
