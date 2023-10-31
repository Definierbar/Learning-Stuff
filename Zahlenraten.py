from random import randint
repeat="ja"
highscore=1000
while repeat == "ja" or repeat == "Ja":
    n = randint(1,100)
    u = None
    score=int(1)
    while n != u : 
        u = input("Rate meine Nummer:")
        if int(u)>int(n):
            print("Zu Hoch!")
            score +=1
        elif int(u)<int(n):
            print("Zu niedrig!")
            score +=1
        elif int(n) == int(u):
            if highscore > score:
                highscore = score
                print("!!!NEUER HIGHSCORE!!!")
            print("Glückwunsch du hast es geschaftt!")
            print("Du hast",score,"Versuche gebraucht!")
            print("Aktueller Highscore:",highscore)
            repeat = input("Noch eine Runde?")
            print(repeat)



print("Danke!")


        