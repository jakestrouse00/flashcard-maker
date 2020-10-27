# flashcard-maker
Helps create flash cards with minimal effort

## Prerequisites
```
requests >= 2.24.0
keyboard >= 0.13.5
pyperclip >= 1.8.1
```



## Installation

### Source code
(Must have Python 3.7+ installed)
1. Download the files from the GitHub
2. Navigate to the directory you downloaded and run the command `python -m pip install -r requirements.txt`

### Executable

1. Download the latest release from GitHub
3. Extract the latest release to your desktop



## How to use

### Create flash cards

1. Open either `windows_collect.py` or `windows_collect.exe`
2. It will ask if you want to clear the current flash cards. Just enter `y` and press `enter`
3. Once the program says it is running, you can begin to make your flash cards
4. Navigate to where you want to make flash cards
5. When you are ready, select a question for your flash card and press `ctrl+c` to copy the text you selected
6. The program will automatically take that text and put it as the question for a flash card. 
7. Then, select the answer you want for the flash card and press `ctrl+c` to copy the text you selected
8. The program will automatically take that text and put it as the answer for a flash card.
9. You can continue to do steps 7 and 8 until you have created the amount of flash cards you want
10. Once you are done making flash cards, close the program you opened in step 1

### Convert program output into user readable flash cards

1. When you are done making your flash cards, you are going to want to convert what the program outputs into something usable
2. Open either `create_cards.py` or `create_cards.exe`
3. The program will ask you if you want to create a PDF, or a CSV file. Choosing the PDF option will give you a pdf document of your flash cards that you can print right away
Choosing the CSV file option will give you a .csv file that has your questions in one column and your answers in another column. This is useful if you want to use your flashcards in another program.
4. After choosing the output you want, press `enter`
5. If you choose the PDF option, the program will put a document named `flashcards.pdf` in the `output` folder. By default, the program will automatically open the pdf for you.
6. If you choose the CSV option, the program will put a document named `flashcards.csv` in the `output` folder. You can then use this csv file as you want.