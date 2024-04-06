# importing required classes 
from pypdf import PdfReader 
from gtts import gTTS
import os

# creating a pdf reader object 
reader = PdfReader('test.pdf') 
  
# printing number of pages in pdf file 
key = len(reader.pages)

# an empty container
store = ""
  
# creating a page object
# looging through the whole pdf and store its content in a veriable
for i in range(key):
    page = reader.pages[i]
    text = page.extract_text()
    store=store+text
  
# extracting text from page
language = 'en'

mytext = store
# Passing the text and language to the engine,  
# here we have marked slow=False. Which tells  
# the module that the converted audio should  
# have a high speed 
myobj = gTTS(text=mytext, lang=language, slow=False) 
  
# Saving the converted audio in a mp3 file named 
# welcome  
myobj.save("welcome.mp3") 
  
# Playing the converted file 
os.system("mpg321 welcome.mp3") 

