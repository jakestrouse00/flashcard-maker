import keyboard
import time
import pyperclip
import json


class Flashcards:
    def __init__(self):
        pyperclip.copy('')
        self.switch = False
        self.askWipe()

    def askWipe(self):
        userInput = input("Would you like to clear your current flash cards? (y/n):   ").lower()
        if userInput == "y":
            currentCards = {"questions": [], "answers": []}
            with open('data/flashcards.json', 'w') as f:
                json.dump(currentCards, f)
        else:
            pass



    def readAndDump(self, textType: str, selectedText: str):
        with open('data/flashcards.json', 'r') as fp:
            currentCards = json.load(fp)

        currentCards[textType].append(selectedText)
        with open('data/flashcards.json', 'w') as f:
            json.dump(currentCards, f)
        print(f"Wrote {selectedText} to {textType}")

    def getText(self):
        data = pyperclip.paste()
        return data

    def waiter(self):
        keyboard.wait('ctrl+c')
        time.sleep(0.5)
        data = self.getText()

        if not self.switch:
            self.readAndDump(textType='questions', selectedText=data)
            self.switch = True
        else:
            self.readAndDump(textType='answers', selectedText=data)
            self.switch = False

    def start(self):
        while True:
            self.waiter()


if __name__ == '__main__':
    c = Flashcards()
    c.start()
