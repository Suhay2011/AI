import random
destination={
    "beaches":["The Golden Mile","Natures Valley","Clifton"],
    "Mountains":["The Matterhorn","Mount Kilimonjaro","Mount Fuji"],
    "cites":["Tokyo","Paris","Dubai"]
}
jokes=["Why don't penguins like talking to strangers? They find it hard to break the ice","I used to hate facial hair... then it grew on me..","I'm reading a book about anti-gravity. It's impossible to put down"]

def recomend():
    pre=input("enter beaches, mountains or cites")
    if (pre in destination ):
        place = random.choice(destination[pre])
        print("try this",place)
    else:
        print('invalid choice')

def packing():
    days=input("input the no days")
    place=input("enter the place")
    print(f"I hope that you have a wonderfull vacation, enjoy the holidays at {place} for those {days}!")

def chat():
    while True:
        msg=input("enter from recomend, packing or joke")
        if "recomend" in msg:
            recomend()
        elif "joke" in msg:
            print(random.choice(jokes))
        elif "packing" in msg:
            packing()
        elif msg in ["exit","bye"]:
            print("Good bye :(")
            break
        else:
            print("enter from recomend, packing or joke")
chat()
