import webvtt
import pandas as pd
import os

# Converts vtt to csv for readability
def convert_vtt(filenames):
    #extract the text and times from the vtt file
    for file in filenames:
        captions = webvtt.read(file)
        text_time = pd.DataFrame()
        text_time['text'] = [caption.text for caption in captions]
        text_time['start'] = [caption.start for caption in captions]
        text_time['stop'] = [caption.end for caption in captions]
        return(text_time)

# Extracts ARPABET style phonemes from any sentence
def phonemeExtractor(s):
    result = []
    for word in s.lower().split():
        try:
            pList=arpabet[word][0]
            for p in pList:
                result.append(p)
        except:
            pass
    return result
