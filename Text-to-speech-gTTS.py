# importing google text-to-speech (TTS) modules
from gtts import gTTS

# This module is imported so that we can
# play the converted audio

# The text that you want to convert to audio
mytext = "add your text here"

# Language in which you want to convert
language = 'en'
# tld = 'co.uk'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
file = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
file.save("test.mp3")
