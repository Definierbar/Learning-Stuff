print("Ich errate deine Zahl!")
nmax = None
correct = "nein"

while nmax == None:
    try:
        nText = input("Wie gross kann deine Zahl höchstens sein? ")
        nmax = int(nText)
    except:
        print("Es muss sich um eine Zahl handeln!") 

print("Danke.")
from random import randint
nmin=1
score=0
tip = None
versuch=randint(nmin,nmax)

while tip !="ja":
    versuch=randint(nmin,nmax)
    print("Ist es",versuch,"? Höher oder Tiefer?")
    score +=1
    tip=input()
    if tip == "höher":
        nmin = versuch + 1
    elif tip == "tiefer":
        nmax = versuch - 1

print("Super, ich hab", score,"Versuche gebraucht!")
