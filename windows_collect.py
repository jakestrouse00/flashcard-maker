import keyboard
import time
import pyperclip
import json


def readAndDump(textType: str, selectedText: str):
    """

    :param textType: The type of text. So either 'question' or 'answer'
    :param selectedText: The text copied from the clipboard
    """
    with open('data/flashcards.json', 'r') as fp:
        currentCards = json.load(fp)

    currentCards[textType].append(selectedText)
    with open('data/flashcards.json', 'w') as f:
        json.dump(currentCards, f)
    print(f"Wrote {selectedText} to {textType}")


class Flashcards:
    def __init__(self):
        pyperclip.copy('')  # wipe the current clipboard contents
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

    def getText(self):
        # a bit confusing, but pyperclip.paste() copies the stuff in the clipboard, and pyperclip.copy() puts stuff in they clipboard
        data = pyperclip.paste()
        return data

    def waiter(self):
        keyboard.wait('ctrl+c')  # blocks until 'ctrl + c' (or the key combination for copying on windows) is pressed
        time.sleep(0.5)  # I make it sleep for 0.5 seconds to make sure the text is copied by Windows before I try and get what is in the clipboard
        data = self.getText()
        # just a basic switch that turns on/off to determine if the copied text is a question or answer
        if not self.switch:
            readAndDump(textType='questions', selectedText=data)
            self.switch = True
        else:
            readAndDump(textType='answers', selectedText=data)
            self.switch = False

    def start(self):
        """
        Since this is a 'while True' loop. The program needs to be manually closed for it to stop making flash cards.
        """
        print("The program is now running!")
        while True:
            self.waiter()


if __name__ == '__main__':
    c = Flashcards()
    c.start()
