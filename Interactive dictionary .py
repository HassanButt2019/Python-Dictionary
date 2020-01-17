import json
from difflib import  SequenceMatcher # import for the text matcher
from  difflib import get_close_matches

class Dictionary:
    data = {}
    Translated_word = []
    word = ""
    def __init__(self):
        print("==--==--==--==--WELCOME TO THE DICTIONARY--==--==--==--==--==")
        self.data = json.load(open("data.json"))  # loading the json file


    def Input(self):#this function will take only input from user
        self.word = input("Enter word :")
        self.Translated_word = self.Translate(self.word)

        
    def Translate(self , word_arg ):
        word_arg = word_arg.lower()
        if (word_arg) in self.data:
               return self.data[word_arg]
        elif len(get_close_matches(word_arg , self.data.keys() )) > 0:
            yn =  input("DID YOU MEAN %s INSEATED OF ? ENTER Y IF YES , OR NO IF NO "  %get_close_matches(word_arg , self.data.keys())[0])
            if yn == "Y":
                return self.data[get_close_matches(word_arg , self.data.keys())[0]]
            elif yn == "N":
                return "THE WORD DOESN;T EXIST . PLEASE CHECK IT"
            else:
                return "WE DIDN'T UNDERSTAND YOUR ENTRY"
        else:
            return "THE WORD DOESN'T EXIST.PLEASE CHECK IT AGAIN"

    def Print(self):
        if type(self.Translated_word) == list:
            for i in self.Translated_word:
                print("Defination ", i)
        else:
            print(self.Translated_word)



Disctionary_1 = Dictionary()

print("PLEASE ENTER WORDS ENTER \end TO TERMINATE THE PROGRAM")
while True:
    print("ENTER WORD YOU WANT TO SEARCH")
    Disctionary_1.Input()
    Disctionary_1.Print()
