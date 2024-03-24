import gtts
from playsound import playsound

tts_eng = gtts.gTTS("The history of the Kyrgyz people and the land now called Kyrgyzstan goes back more than 3,000 years. Although geographically isolated by its mountainous location, it had an important role as part of the historical Silk Road trade route. Turkic nomads, who trace their ancestry to many Turkic states such as the First and Second Turkic Khaganates, have inhabited the country throughout its history. In the 13th century, Kyrgyzstan was conquered by the Mongols")

tts_rus = gtts.gTTS("История кыргызского народа и земли, которая сейчас называется Кыргызстаном, насчитывает более 3000 лет. Несмотря на географическую изоляцию из-за своего горного расположения, она играла важную роль как часть исторического торгового пути Великого Шелкового пути. Тюркские кочевники, которые ведут свою родословную от многих тюркских государств, таких как Первый и Второй Тюркские каганаты, населяли страну на протяжении всей ее истории. В 13 веке Кыргызстан был завоеван монголами", lang='ru')

tts_eng.save("History_eng.mp3")
tts_rus.save("History_rus.mp3")

playsound("History_eng.mp3")
playsound("History_rus.mp3")
