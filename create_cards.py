import json
import random
import subprocess
import requests
import csv


class Cards:
    def __init__(self):
        # load flash card data
        self.cards = self.loadData()

    def openPDF(self):
        subprocess.Popen(["output/flashcards.pdf"], shell=True)

    def writeCardsWebsite(self):
        data = self.formatCardsWebsite()  # format the flash cards to the right format
        headers = {
            'authority': 'flashcard.online',
            'accept': 'text/html, */*; q=0.01',
            'x-requested-with': 'XMLHttpRequest',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.99 Safari/537.36',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://flashcard.online',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://flashcard.online/editor2/',
            'accept-language': 'en-US,en;q=0.9',
        }

        r = requests.post('https://flashcard.online/editor2/create_pdf.php', headers=headers, data=data)
        r = requests.get(r.text, stream=True)

        with open('output/flashcards.pdf', 'wb') as f:
            f.write(r.content)
        self.openPDF()  # open the saved pdf document for the user to see

    def writeCards(self):
        # field names
        fields = ['Questions', 'Answers']
        rows = []
        # write the rows of questions and answers
        for q in range(len(self.cards['questions'])):
            rows.append([self.cards['questions'][q], self.cards['answers'][q]])

        # name of csv file
        filename = "output/flashcards.csv"

        # writing to csv file
        with open(filename, 'w') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile)

            # writing the fields
            csvwriter.writerow(fields)

            # writing the data rows
            csvwriter.writerows(rows)

    def loadData(self):
        with open('data/flashcards.json', 'r') as fp:
            currentCards = json.load(fp)

        return currentCards

    def formatCardsWebsite(self):
        outputData = {'card_type': 'text',
                      'card_nums': "2",
                      'list_added': str(len(self.cards['questions'])),
                      'card_name': "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890", k=5))}
        # A not so elegant solution for formatting the json
        x = []
        for i in range(len(self.cards['questions'])):
            x.append(self.cards['questions'][i])
            x.append(self.cards['answers'][i])
        for m in range(len(x)):
            outputData.update({f'data[{m}][image_url]': 'undefined',
                               f'data[{m}][text]': x[m]})
        return outputData


if __name__ == '__main__':
    c = Cards()
    while True:
        user_choice = input("Would you like to\n(1) Create CSV file\n(2) Create flashcards\n\nI would like to: ")
        if user_choice == "1":
            c.writeCards()
            input("CSV file has been created. Press ENTER to exit...")
            break
        elif user_choice == "2":
            c.writeCardsWebsite()
        else:
            print("Please only enter '1' or '2'!\n\n")
