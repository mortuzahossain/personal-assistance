import wikipedia
import wolframalpha
from gtts import gTTS
import os

# espeak.synth("What are you doing ? Need any help : ")

tts = gTTS(text='What are you doing ? Need any help : ', lang='en')
tts.save("temp.mp3")
os.system("mpg123 temp.mp3")
os.remove('temp.mp3')

wikipedia.set_lang('en')
app_id = '29778R-Q4T2Q759RR'
client = wolframalpha.Client(app_id)

while True:
	input = raw_input('Q: ')
	try:
		result = client.query(input)
		ans = next(result.results).text
		print ans
		tts = gTTS(text=ans, lang='en')
		tts.save("temp.mp3")
		os.system("mpg123 temp.mp3")
		os.remove('temp.mp3')
	except:
		ans = wikipedia.summary(input,sentences = 2)
		print ans
		tts = gTTS(text=ans, lang='en')
		tts.save("temp.mp3")
		os.system("mpg123 temp.mp3")
		os.remove('temp.mp3')