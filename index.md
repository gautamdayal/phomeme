# About

Ever wanted to create a frankenbite or YTP of your favourite character? You must've gone through hours of footage
just for a few minutes of dialogue. Well, phoMeme can save all that work. Keep reading to find out more.


# Worflow
PhoMeme, at a high level, does 5 things:


1. Takes in a YouTube link, and a text file with the desired output sentences
1. Creates a pandas DataFrame to store subtitles with timestamps, and does the same for the input text
1. Converts English words to standard ARPABET phonemes
1. Tries matching input words to respective timestamps in the video. If the word is not found, the program searches for individual syllables.
1. Returns a color-coded file with the input text marked with timestamps to each word/syllable

# Sample

<iframe width="965" height="543" src="https://www.youtube.com/embed/0NSTNlePDcA" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
