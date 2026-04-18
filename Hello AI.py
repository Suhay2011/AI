print("Hello! I am an AI Chat assistant. What is your name? :")

name = input()

print(f"Nice to meet you, {name}!")

print("How was your day today? (good/bad) :")
mood = input().lower()

if mood == "good" :
    print("I am SO glad to hear that!")
elif mood == "bad":
    print("I am sorry. I hope it might be better :(")
else:
    print("I see. it is sometimes hard to put it to words.")

print(f"It was great talking with you {name}. Goodbye!!")