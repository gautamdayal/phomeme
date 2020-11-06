# Importing necessary modules
import nltk
import os
import sys
import webvtt
import pandas as pd
import tools
from colorama import Fore, Back, Style

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

print('transcript', transcript_frame)
print('input',text)

# Opening the ARPABET corpus as a dictionary
# arpabet = nltk.corpus.cmudict.dict()


"""
explore: webvtt segmenting, python re (reg exp stuff)

Flow ^_^
6. convert to phonemes
7. make epic thing with phonemes matched with timestamps

8. Convert input to phonemes.
9. matching process
10. Output timestamps for each phoneme chain
"""
