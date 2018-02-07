class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

in_case_you_didnt_know = Song(["In case you didnt know",
                               "baby im crazy bout yuh",
                               "and I will be lying if I said that I",
                               "could live this life without yuh even tho",
                               "I dont tell you all the time",
                               "you had my heart a long long time ago",
                               "in case you didnt know"])

print("""You're taking the love of your life on a date
Where are you going date #1 or date #2""")

date = input("> ")

if date == "1":
    print("You go out in a  open field at night.")
    print("What do you do?")
    print("1. Set everything up to show how creative you are.")
    print("2. Just sit there and let her figure everything out.")

    decision = input("> ")

    if decision == "1":
        print("Yall chill and sit back listen to country music and look at the stars. AYEEEEEE!!!!!" )
        in_case_you_didnt_know.sing_me_a_song()
    elif decision == "2":
        print("Both of yall just sit there and look dumb for the rest of the night")
    else:
        print(f"WOW you could do better.")

elif date == "2":
    print("You go to mall and shop.")
    print("What do you do?")
    print("1.Buy her nice things that she wants ")
    print("2.Both spend money on each other")
    print("3. Make her spend all her money while you pretend you're broke.")

    choice = input("> ")

    if choice == "1" or choice == "2":
        print("Good choice you're a keeper!!!!!.")
        in_case_you_didnt_know.sing_me_a_song()
    else:
        print("You're selfish so she breakup with you.")