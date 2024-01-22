import time
import random

words = (
    "abandon",
    "absurd",
    "accomplish",
    "accurate",
    "adventure",
    "aggressive",
    "amaze",
    "ancestor",
    "annoy",
    "anxious",
    "apparent",
    "approve",
    "arrogant",
    "astonish",
    "attractive",
    "authority",
    "awkward",
    "baffle",
    "bargain",
    "beneath",
    "bizarre",
    "blunder",
    "bold",
    "bravery",
    "brief",
    "brilliant",
    "calculate",
    "captivate",
    "careful",
    "celebrate",
    "challenge",
    "chaos",
    "character",
    "charming",
    "cheerful",
    "clarify",
    "coincidence",
    "collaborate",
    "combine",
    "comfort",
    "commend",
    "compete",
    "complain",
    "concentrate",
    "concern",
    "confident",
    "confuse",
    "congratulate",
    "conquer",
    "consider",
    "constant",
    "construct",
    "consume",
    "contemplate",
    "contribute",
    "convince",
    "cooperate",
    "courage",
    "create",
    "criticize",
    "curious",
    "daring",
    "deceive",
    "decide",
    "defend",
    "definite",
    "delight",
    "demand",
    "depend",
    "desire",
    "determine",
    "develop",
    "devour",
    "different",
    "diligent",
    "discover",
    "distract",
    "doubt",
    "dramatic",
    "earnest",
    "educate",
    "effective",
    "efficient",
    "elaborate",
    "embarrass",
    "embrace",
    "encourage",
    "engage",
    "enjoy",
    "entertain",
    "enthusiastic",
    "envy",
    "essential",
    "establish",
    "evaluate",
    "evidence",
    "examine",
    "excite",
    "expand",
    "expect",
    "experience",
    "experiment",
    "explain",
    "explore",
    "express",
    "extend",
    "extraordinary",
    "fabulous",
    "fascinate",
    "fearless",
    "feisty",
    "flexible",
    "focus",
    "forgive",
    "fortunate",
    "frustrate",
    "generous",
    "genuine",
    "gigantic",
    "glorious",
    "grateful",
    "grieve",
    "guarantee",
    "happiness",
    "harmful",
    "hasty",
    "hilarious",
    "honest",
    "humble",
    "humiliate",
    "identify",
    "ignore",
    "imagine",
    "immediate",
    "impress",
    "improve",
    "include",
    "influence",
    "inform",
    "innovate",
    "inspire",
    "intelligent",
    "intense",
    "interesting",
    "interpret",
    "introduce",
    "investigate",
    "involve",
    "irritate",
    "jealous",
    "jovial",
    "judge",
    "knowledge",
    "lack",
    "laugh",
    "legendary",
    "limit",
    "listen",
    "loyal",
    "magnificent",
    "maintain",
    "manage",
    "mature",
    "measure",
    "mischief",
    "mischievous",
    "miserable",
    "mysterious",
    "nervous",
    "notice",
    "observe",
    "obvious",
    "opportunity",
    "optimistic",
    "organize",
    "original",
    "outstanding",
    "overcome",
    "participate",
    "passionate",
    "patience",
    "peaceful",
    "perceive",
    "perform",
    "persevere",
    "persuade",
    "pessimistic",
    "pleasure",
    "polite",
    "popular",
    "positive",
    "potential",
    "praise",
    "precise",
    "predict",
    "prefer",
    "prepare",
    "preserve",
    "prevent",
    "pride",
    "priority",
    "procrastinate",
    "produce",
    "progress",
    "promise",
    "protect",
    "proud",
    "provide",
    "punctual",
    "puzzle",
    "quarrel",
    "question",
    "quick",
    "quiet",
    "rare",
    "realize",
    "reasonable",
    "rebel",
    "recognize",
    "recommend",
    "recover",
    "refuse",
    "regret",
    "reject",
    "relax",
    "reliable",
    "remarkable",
    "remember",
    "remind",
    "remove",
    "repair",
    "repeat",
    "replace",
    "represent",
    "request",
    "require",
    "rescue",
    "research",
    "respect",
    "responsible",
    "reveal",
    "reward",
    "ridiculous",
    "risk",
    "satisfy",
    "scare",
    "search",
    "secret",
    "selfish",
    "sensitive",
    "serious",
    "shatter",
    "shy",
    "silly",
    "sincere",
    "skillful",
    "smart",
    "solve",
    "special",
    "spontaneous",
    "stingy",
    "strange",
    "strength",
    "struggle",
    "succeed",
    "sudden",
    "support",
    "surprise",
    "suspicious",
    "talented",
    "tease",
    "tempt",
    "terrific",
    "thorough",
    "thoughtful",
    "thrill",
    "timid",
    "tolerate",
    "tragic",
    "transform",
    "trust",
    "typical",
    "understand",
    "unique",
    "unite",
    "unusual",
    "upset",
    "valuable",
    "venture",
    "victory",
    "vigorous",
    "vivid",
    "volunteer",
    "vulnerable",
    "wander",
    "wary",
    "weary",
    "wonder",
    "worry",
    "worthy",
    "youthful",
    "zealous"
)
HANGMANPICS = ['''
       
       
        
       
          
        
=========''','''
      +
      |
      |
      |
      |
      |
=========''','''
  +---+
      |
      |
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

startOrNot = input("Would you like to start the game? ")
if startOrNot == "y" or "yes":
    print("""
             _                    _       
 __ __ _____| |__ ___ _ __  ___  | |_ ___ 
 \ V  V / -_) / _/ _ \ '  \/ -_) |  _/ _ \
  \_/\_/\___|_\__\___/_|_|_\___|  \__\___/
                                          

 /$$   /$$  /$$$$$$  /$$   /$$  /$$$$$$  /$$      /$$  /$$$$$$  /$$   /$$
| $$  | $$ /$$__  $$| $$$ | $$ /$$__  $$| $$$    /$$$ /$$__  $$| $$$ | $$
| $$  | $$| $$  \ $$| $$$$| $$| $$  \__/| $$$$  /$$$$| $$  \ $$| $$$$| $$
| $$$$$$$$| $$$$$$$$| $$ $$ $$| $$ /$$$$| $$ $$/$$ $$| $$$$$$$$| $$ $$ $$
| $$__  $$| $$__  $$| $$  $$$$| $$|_  $$| $$  $$$| $$| $$__  $$| $$  $$$$
| $$  | $$| $$  | $$| $$\  $$$| $$  \ $$| $$\  $ | $$| $$  | $$| $$\  $$$
| $$  | $$| $$  | $$| $$ \  $$|  $$$$$$/| $$ \/  | $$| $$  | $$| $$ \  $$
|__/  |__/|__/  |__/|__/  \__/ \______/ |__/     |__/|__/  |__/|__/  \__/
                                                                         
created by webadderall
          """)
    
    loading_wait = round(random.uniform(1, 5), 2)
    random_word = words[random.randint(0, 302)].lower()
    wordLength = len(random_word)
    losses = 0
    def hangmanLoss():
        global losses
        losses += 1
    def hangmanStatus():
        global losses
        print(HANGMANPICS[losses])

    print("Loading...")
    time.sleep(1)
    print("Game starting...")
    print("█▒▒▒▒▒▒▒▒▒ 10%")
    time.sleep(loading_wait)
    print("Computer is choosing a word...")
    print("███▒▒▒▒▒▒▒ 30%")
    time.sleep(loading_wait)
    print("███████▒▒▒ 70%")
    time.sleep(loading_wait)
    print("█████████▒ 90%")
    time.sleep(4)
    print("██████████ 100%")
    print("Computer has chosen.")
    time.sleep(1)
    print("The word has been chosen. You have 6 guesses.")
    time.sleep(1)
    displayed_word = '_' * len(random_word)
    while displayed_word != random_word:
        print(f"There are {wordLength} letters in the word.")
        hangmanStatus()
        print(displayed_word)
        chosenLetter = input("Pick a letter from the alphabet. ").lower()

        if chosenLetter not in random_word:
            print("Try again.")
            hangmanLoss()
            print(hangmanLoss())
        else:
            print("Success!")
            for i in range(wordLength):
              if random_word[i] == chosenLetter:
                displayed_word = displayed_word[:i] + chosenLetter + displayed_word[i+1:]
            if losses == 9:
                print("You lost!")
                breakpoint()
        
      

