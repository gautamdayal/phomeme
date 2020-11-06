# Importing necessary modules
import nltk
import os
import sys
import webvtt
import pandas as pd
import tools
from colorama import Fore, Back, Style

def purify(L):
    outL = []
    for item in L:
        if item not in outL:
            outL.append(item)
    return outL

arpabet = nltk.corpus.cmudict.dict()
# Extracts ARPABET style phonemes from any sentence
def phonemeExtractor(s):
    result = []
    for word in s.lower().split():
        pList=[]
        try:
            pList=arpabet[word][0]
        except:
            pass
        for p in pList:
            result.append(p)
    return result

# Collecting arguments in format [main.py] [link] [inputfile]
args = sys.argv
try:
    link = args[1]
    fin = args[2]
except:
    print('[phoMeme] Input format: main.py <url> <input file>')
# Getting name of project
proj_name = input('Meme name: ')
# Downloading auto-subs of video from YouTube to assets folder
print('[YouTube] Downloading captions...')
os.system(f"youtube-dl --write-auto-sub --skip-download '{link}' --output 'assets/{proj_name}'")

# Converting vtt to CSV in assets folder, generating transcript
print('[phoMeme] Processing captions...')
transcript_frame = tools.convert_vtt([f'assets/{proj_name}.en.vtt'])
with open(fin, 'r') as file:
    text = file.readlines()

words = ''.join(purify(text))
in_nemes = purify(phonemeExtractor(words))

outF = open(f'{proj_name}.txt', 'w')
for i in range(0, len(transcript_frame)-1):
    for s in transcript_frame.loc[i]['text'].split():
        if s in words:
            outF.write(f'{s}, ')
            outF.write(str(transcript_frame.loc[i]['start'])+str(transcript_frame.loc[i]['stop'])+'\n')

for i in range(0, len(transcript_frame)-1):
    for p in phonemeExtractor(transcript_frame.loc[i]['text']):
        if p in in_nemes:
            outF.write(f'{p}, ')
            outF.write(str(transcript_frame.loc[i]['start'])+str(transcript_frame.loc[i]['stop']) + '\n')

outF.close()
