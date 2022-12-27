from gtts import gTTS
from PyPDF2 import PdfReader

reader = PdfReader('sample.pdf')
text = ''
for page in reader.pages:
  text = text + page.extract_text()

myobj = gTTS(text=text,lang='en',slow=False)
myobj.save('welcome.mp3')
