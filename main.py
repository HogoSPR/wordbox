import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
from random import randint


root = ttk.Window(themename = 'cyborg')
root.title = 'memerise'
root.geometry = '550x410'


def next():
    answer_label.config(text = '')
    entry.delete(0, 1000)
    global random_word
    random_word = randint(0, count-1)
    greek_word.config(text=words[random_word][0])



def answer():
    if entry.get() == words[random_word][1]:
        answer_label.config(text=f'Correct!', font = ('Helvetica', 30))
    else:
        answer_label.config(text=f'Incorrect, het goede antwoord is: {words[random_word][1]}', font = ('Helvetica', 30))
 
#put here your own list of words
#your smart enough i hope

#((word), (answer))

#just if you werent

#you can also copy lists from smort

#legit collab
words = [
	(("ἀγαθός, -ή, -όν"), ("goed")),
	(("ὁ ἀδελφός"), ("broer")),
	(("ἀεί"), ("altijd, steeds")),
	(("ἀλλά, ἀλλ’"), ("maar")),
	(("ἀνδρεῖος, -α, -ον"), ("dapper")),
	(("ὁ ἀνήρ, ἀνδρός"), ("man")),
	(("ἄρα"), ("dus")),
	(("ἁρπάζω, ἥρπασα"), ("roven")),
	(("αὐτός, -ή, -ό"), ("zelf, dezelfde, hetzelfde als; gen/dat/acc hij, zij, het")),
	(("βαίνω, ἔβην"), ("gaan, stappen")),
	(("γάρ"), ("want, immers, namelijk")),
	(("γιγνώσκω, ἔγνων"), ("begrijpen, (leren) kennen")),
	(("δέ, δ’"), ("en, maar")),
	(("τὸ δένδρον"), ("boom")),
	(("δή"), ("dus, dan, natuurlijk")),
	(("ὁ δοῦλος"), ("slaaf")),
	(("δύο"), ("twee")),
	(("ἐγώ"), ("ik")),
	(("ἐθέλω"), ("willen")),
	(("εἰ"), ("als, indien; indirecte vraag of")),
	(("εἰμί"), ("zijn, bestaan")),
	(("εἰς + acc."), ("naar (binnen)")),
	(("ἔξεστι(ν) + inf."), ("het is mogelijk om")),
	(("ἐπεί"), ("toen, nadat; omdat, aangezien")),
	(("τὸ ἔργον"), ("werk, taak; daad")), 
	(("ἐρωτάω"), ("vragen")),
	(("ἡ ἐσθής, ἐσθῆτος"), ("kleding(stuk)")),
	(("εὑρίσκω, ηὗρον"), ("vinden")),
	(("ἤ"), ("of; vergelijking dan")),
	(("ὁ ἥλιος"), ("de zon")),
	(("ἰσχυρός, -ά, -όν"), ("krachtig, sterk")),
	(("καθαρός, -ά, -όν"), ("schoon, zuiver")),
	(("καί"), ("en; ook, zelfs")),
	(("καὶ δὴ καί"), ("en ook, en vooral")),
	(("κακός, -ή, -όν"), ("slecht, laf")),
	(("καλός, -ή, -όν"), ("mooi, goed")),
	(("ὁ κόσμος"), ("wereld(orde); sier, opsmuk")),
	(("λαμβάνω, ἔλαβον"), ("nemen, krijgen")),
	(("λέγω, εἶπον"), ("zeggen, spreken")),
	(("ὁ λόγος"), ("woord, verhaal")),
	(("μανθάνω, ἔμαθον"), ("leren (kennen), vernemen")),
	(("μέγας, μεγάλη, μέγα"), ("groot")),
	(("μέλλω"), ("zullen, van plan zijn, op het punt staan")),
	(("μέν ... δέ"), ("(weliswaar) … maar; … en")),
	(("μένω"), ("blijven, wachten (op)")),
	(("ὁ, ἡ, τό"), ("de, het")),
	(("ὅδε, ἥδε, τόδε"), ("deze, dit")),
	(("ὁράω, εἶδον"), ("zien")),
	(("οὗ"), ("waar")),
	(("οὐ, οὐκ, οὐχ"), ("niet")),
	(("οὐκέτι bijw"), ("niet meer")),
	(("ὁ οὐρανός"), ("hemel")),
	(("οὗτος, αὗτη, τοῦτο"), ("die, dat")),
	(("παρέχω"), ("geven, verschaffen")),
	(("περί + gen."), ("over, om")),
	(("περί + acc."), ("rondom, om")),
	(("πολύς, πολλή, πολύ"), ("veel")),
	(("ὁ ποταμός"), ("rivier")),
	(("ῥέω"), ("stromen")),
	(("σοφός, -ή, -όν"), ("wijs, slim")),
	(("τάττω, ἔταξα"), ("opstellen, ordenen")),
	(("τε καί, τε ... καί"), ("en")),
	(("τελέω, ἐτέλεσα"), ("voltooien, afmaken")),
	(("τί"), ("wat (nom/acc); waarom")),
	(("τὸ ὕδωρ, ὕδατος"), ("water")),
	(("ὑψηλός, -ή, -όν"), ("hoog")),
	(("φιλός, -ή, -όν"), ("vriend")),
	(("ὡς"), ("zoals, als; hoe, wat (in een uitroep); dat"))
]





count = len(words)

name_label = ttk.Label(root, text = 'wordbox by mindswift', font=('Helvetica', 50))
name_label.pack(pady=30)

greek_word = ttk.Label(root, text = '', font=('Helvetica', 100))
greek_word.pack(pady=50)


answer_label = ttk.Label(root, text = '')
answer_label.pack(pady=10)

entry = ttk.Entry(root, font=('Helvetica', 20))
entry.pack(pady=20)

#Buttons
button_frame = ttk.Frame(root)
button_frame.pack(pady=20)

answer_button = ttk.Button(button_frame, text = 'answer', command = answer)
answer_button.grid(row=0, column=0, padx=20)

next_button = ttk.Button(button_frame, text = 'next', command= next)
next_button.grid(row=0, column=1)







next()

root.mainloop()