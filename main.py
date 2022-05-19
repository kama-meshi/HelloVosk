#!/usr/bin/env python3
# Hello Vosk. Vosk sample repl.
# 
# Reffer to
#  - https://github.com/alphacep/vosk-api/blob/v0.3.32/python/example/test_simple.py
from vosk import Model, KaldiRecognizer, SetLogLevel
import os
import wave

SetLogLevel(0)

if not os.path.exists("model"):
    print ("Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
    exit (1)

wav = "sample_voice_16khz.wav"
wf = wave.open(wav, "rb")
if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
    print ("Audio file must be WAV format mono PCM.")
    exit (1)

model = Model("model")
rec = KaldiRecognizer(model, wf.getframerate())
rec.SetWords(True)

while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        print(rec.Result())
    else:
        print(rec.PartialResult())

print(rec.FinalResult())
