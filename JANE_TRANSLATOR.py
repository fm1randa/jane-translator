# -*- coding: UTF-8
import emoji 
frase = []
frasedemoji = []
#x = emoji.demojize("🎈 🎉 👁️ 👑 💍 👄 👓 🎩 🌹 🌟 🌙 🔥 💥 🍼 🎂 🏀 🏉 ⛸️ 🏆 🎲 🎺 ✈️ 🎡")
emojiscod_lista = [(":balloon:", "a"), (":party_popper:", "b"), (":eye:", "c"), (":crown:", "d"), (":ring:", "e"), (":mouth:", "f"), (":glasses:", "g"), (":top_hat:", "h"), (":rose:", "i"), (":glowing_star:", "j"), (":crescent_moon:", "l"), (":fire:", "m"), (":collision:", "n"), (":baby_bottle:", "o"), (":birthday_cake:", "p"), (":basketball:", "q"), (":rugby_football:", "r"), (":american_football:", "r"), (":ice_skate:", "s"), (":trophy:", "t"), (":game_die:", "u"), (":trumpet:", "v"), (":airplane:", "x"), (":ferris_wheel:", "z")]
emojis_lista = emojis_lista = [("🎈", "a"), ("🎉", "b"), ("👁️", "c"), ("👑", "d"), ("💍", "e"), ("👄", "f"), ("👓", "g"), ("🎩", "h"), ("🌹", "i"), ("🌟", "j"), ("🌙", "l"), ("🔥", "m"), ("💥", "n"), ("🍼", "o"), ("🎂", "p"), ("🏀", "q"), ("🏉", "r"), ("🏈", "r"), ("⛸️", "s"), ("🏆", "t"), ("🎲", "u"), ("🎺", "v"), ("✈️", "x"), ("🎡", "z")]
emojis = dict(emojiscod_lista)

textoemoji = input("Texto emojizado: ")
for j in textoemoji:
    frasedemoji.append(emoji.demojize(j))
for i in frasedemoji:
    if i == " ":
        frase.append(" ")
    elif i != "":
        frase.append(emojis[i])
frase = "".join(frase)
print(frase)
