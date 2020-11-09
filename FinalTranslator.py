#Goal: create a translator that converts english text to Sonkeigo(Respectful) Japanese
# Reason: Translators have issues on maintaining formality. Japanese happens to have multiple levels of formality:
# Sonkeigo (Respectful), Teneigo (Polite), and Kenjogo(Humble).

# Creating Basic, Hollow GUI
from tkinter import *
from tkinter import Tk
root = Tk()
root.title("Translator")
# Creating Dictionaries
engjpnsub = {"I": "私は", "You": "あなたは", "We": "私たちは", "She": "彼女は", "He": "彼は"}
engjpnverbs ={"drink": "を召し上がります。", "eat":"を召し上がります。", "go":"にいらっしゃいます", 'study': "を勉強いたします。", "like": "が好きでございます。", "do": "をいたします。"}
engjpnobject = {"food.": "食べ物", "water.": "水", "soda.": "コーラを", "university.": "大学", "math.": "数学", "science.": "理解", "literature.": "文学", "Matahacks.": "マタハックス"}
#Creating Variables
global FinishedObject
global FinishedVerb
global FinishedSubject

#Creating Functions

#Break phrase into a list to find subjects, verbs, and objects. English's SVO
def breakphrase():
    sentence = phrase.get()
    broken = sentence.split(' ')
    global phrlist
    phrlist = (tuple(broken))


# Compares list to keys and prints those key's values to find it's japanese equivalent.
def subcomparison():
    global phrlist
    global FinishedSubject
    FinishedSubject= None
    for sub in phrlist:
        if sub in engjpnsub:
            FinishedSubject=(engjpnsub[sub])
            print(FinishedSubject)
            return FinishedSubject


#Variable Result Subject


def verbcomparison():
    global FinishedVerb
    FinishedVerb=None
    for verb in phrlist:
        if verb in engjpnverbs:
            FinishedVerb= (engjpnverbs[verb])
            print(FinishedVerb)
            return FinishedVerb


def objectcomparison():
    global FinishedObject
    FinishedObject=None
    for object in phrlist:
        if object in engjpnobject:
            FinishedObject = (engjpnobject[object])
            print(FinishedObject)
            return FinishedObject

# Creating Results Variables



#Combined the values into a coherent translated sentence. Order is subject object verb (SOV)
def formsentence():
    subcomparison()
    verbcomparison()
    objectcomparison()


#Combines the other functions, and displays finished translation
def translate():
    output = Label(root, text= None).grid(row=3, column= 0, columnspan =6)
    breakphrase()
    formsentence()
    FinishedTranslation=( FinishedSubject + FinishedObject + FinishedVerb)
    output = Label(root, text=FinishedTranslation).grid(row=3, column=0, columnspan=6)

#Clears Results
def Clear():
    output= Label(root, text= "                                                                           ").grid (row =3, column= 0, columnspan=6)


# Furnishing GUI
root.title("Translator")
Label(root, text="English Phrase").grid(row=0, column=0)
phrase = Entry(root, width=60, borderwidth=5)
phrase.grid(row=1, column=0, padx=40, pady=20, columnspan=6)
translatebutton = Button(root,text="Translate", command=translate)
translatebutton.grid(row=2, column=0)
ClearButton= Button(root, text= "Clear", command=Clear)
ClearButton.grid(row= 2, column= 2)





root.mainloop()
