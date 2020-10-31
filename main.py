# Importing necessary modules

import nltk
import os
import sys
import webvtt
import pandas as pd

# Collecting arguments in format [main.py] [link] [inputfile]
args = sys.argv
try:
    link = args[1]
    fin = args[2]
except:
    print('[phoMeme] Input format: main.py <url> <input file>')

# Getting name of project
proj_name = input('[phoMeme] Meme name: ')

# Converts vtt to csv for readability
def convert_vtt(filenames):
    #create an assets folder if one does not yet exist
    if os.path.isdir('{}/assets'.format(os.getcwd())) == False:
        os.makedirs('assets')
    #extract the text and times from the vtt file
    for file in filenames:
        captions = webvtt.read(file)
        text_time = pd.DataFrame()
        text_time['text'] = [caption.text for caption in captions]
        text_time['start'] = [caption.start for caption in captions]
        text_time['stop'] = [caption.end for caption in captions]
        text_time.to_csv('assets/{}.csv'.format(file[:-4]),index=False) #-4 to remove '.vtt'
        #remove files from local drive
        os.remove(file)



# Opening the ARPABET corpus as a dictionary
arpabet = nltk.corpus.cmudict.dict()

# Extracts ARPABET style phonemes from any sentence
def phonemeExtractor(s):
    result = []
    for word in s.lower().split():
        try:
            result.append(arpabet[word])
        except:
            pass
    return result

"""
explore: webvtt segmenting, python re (reg exp stuff)

Flow ^_^
1. Get link from cl arg (link, input) $$$$$
2. download autosubs
3. locate subs file
4. convert subs to readable format, delete subs file $$$$$$
6. convert to phonemes
7. make epic thing with phonemes matched with timestamps

8. Convert input to phonemes.
9. matching process
10. Output timestamps for each phoneme chain
"""
