print("Hello! I am an AI Chat assistant. What is your name? :")

name = input()

print(f"Nice to meet you, {name}!")

print("How was your day today? (good/bad) :")
mood = input().lower()

print("What is your favourite food between these two? (burgers/pizza) :")
food = input().lower()

print("What TV show are you fond of? (Dragon ball Z/Naruto)")
show = input().lower()

if mood == "good" :
    print("I am SO glad to hear that!")
elif mood == "bad":
    print("I am sorry. I hope it might be better :(")
else:
    print("I see. it is sometimes hard to put it to words.")
print("-------------")
if food == "pizza" :
    print("Ahh so you are more into Italian food! thats great to know!!")
elif food == "burgers":
    print("Ahh so you like more home cooked type food! Amazing to know!!")
else:
    print("Okay so you like other food. I'll note that!")
print("-------------")
if show == "Dragon ball Z":
    print("So you like more figting type shows! Me presonaly i like vegeta")
elif show == "Naruto":
    print("So you like a good story and charactor development I see!")

else:
    print("Ahh okay i'll update my system to add more shows you would like next time!!")

print(f"It was great talking with you {name}. Goodbye!!")
