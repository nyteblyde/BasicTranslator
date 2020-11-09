# BasicTranslator
Translate a basic English phrase into Sonkeigo Japanese.
This was made for my first hackathon.

This translator can only translate basic English sentences, specifically sentences that contain words that are found within the program's dictionaries.

These are the keys and values in the dictionaries:
engjpnsub = {"I": "私は", "You": "あなたは", "We": "私たちは", "She": "彼女は", "He": "彼は"}
engjpnverbs ={"drink": "を召し上がります。", "eat":"を召し上がります。", "go":"にいらっしゃいます", 'study': "を勉強いたします。", "like": "が好きでございます。", "do": "をいたします。"}
engjpnobject = {"food.": "食べ物", "water.": "水", "soda.": "コーラを", "university.": "大学", "math.": "数学", "science.": "理解", "literature.": "文学", "Matahacks.": "マタハックス"}

So, if the sentence has those words, the translator should work.
