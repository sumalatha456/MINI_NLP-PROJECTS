#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install gTTS')


# In[2]:


from gtts import gTTS


# In[3]:


#choose the language , english('en')
#choose the language , english('en')
convert = gTTS(text='I like this NLP. How about you dude!', lang='en', slow=False)
#saving the converted audio in a mp3 file named
convert.save("audio.mp3")


# In[4]:


get_ipython().system('pip3 install pyttsx3')


# In[5]:


get_ipython().system('sudo apt install espeak')


# In[6]:


get_ipython().system('apt-get install alsa-utils')


# In[7]:


#!pip install pyttsx3
import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text in english")
engine.runAndWait()


# In[8]:


text = ['Natural language processing is a field of computer science and a subfield of artificial intelligence',\
'that aims to make computers understand human language NLP uses computational linguistics, which is the study',\
'of how language works, and various models based on statistics machine learning, and deep learning. These technologies allow computers',\
'to analyze and process text or voice data, and to grasp their full meaning, including the speakers or writer intentions and emotions']


# In[9]:


engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()


# In[10]:


import pyttsx3
engine = pyttsx3.init() # object creation

"""RATE"""
rate = engine.getProperty('rate') # getting details of current speaking rate
print(rate)                       # printing current voice rate
engine.setProperty('rate', 150)

"""VOlUME"""
volume = engine.getProperty('volume')      # getting the max and min values of volume
print(volume)
engine.setProperty('volume', 1.0)


"""VOICE"""
voices = engine.getProperty('voices')        # getting the detaiks of the current voices
#engine.setProperty('voice' , voices[0].id)  # changing index, changes voices. o for male
engine.setProperty('voice' , voices[1].id)   # changing index, changes voices. 1 for female
engine.say("Hello world!")
engine.say('My current speaking rate is' + str(rate))
engine.say('My current speaking volume is' + str(volume))
engine.runAndWait()


# In[11]:


"""RATE"""
rate = engine.getProperty('rate') # getting details of current speaking rate
print(rate)                       # printing current voice rate
engine.setProperty('rate', 150)   # setting up new voice rate


# In[12]:


"""VOlUME"""
volume = engine.getProperty('volume')      # getting the max and min values of volume
print(volume)
engine.setProperty('volume', 1.0)


# In[13]:


"""VOICE"""
voices = engine.getProperty('voices')        # getting the detaiks of the current voices
#engine.setProperty('voice' , voices[0].id)  # changing index, changes voices. o for male
engine.setProperty('voice' , voices[1].id)   # changing index, changes voices. 1 for female
engine.say("Hello world!")
engine.say('My current speaking rate is' + str(rate))
engine.say('My current speaking volume is' + str(volume))
engine.runAndWait()


# In[20]:


get_ipython().system('pip install goslate')


# In[22]:


import goslate


# In[24]:


gs = goslate.Goslate()
translatedText = gs.translate(text,'en')
print(translatedText)


# In[26]:


get_ipython().system('pip install translate')


# In[30]:


##translating text to the telugu
from translate import Translator
translator = Translator(to_lang="te")
translation = translator.translate("How are you? Is everything is going good")


# In[32]:


##translating text to the telugu
from translate import Translator
translator = Translator(to_lang="ta")
translation = translator.translate("How are you? Is everything is going good")


# In[ ]:


##play sound


# In[34]:


get_ipython().system('pip install python-vlc')


# In[35]:


import vlc
p = vlc.MediaPlayer("audio.mp3")
p.play()


# In[16]:


get_ipython().system('pip install playsound')


# In[18]:


import playsound as pl
pl.playsound('audio.mp3')
print('playing sound using playsound')


# In[41]:


get_ipython().system('pip install SpeechRecognition')


# In[39]:


get_ipython().system('pip install PyAudio')


# In[ ]:




