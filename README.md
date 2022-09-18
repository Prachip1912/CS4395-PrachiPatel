# CS4395-PrachiPatel

## Homework Zero
You can see the [homework zero answers here](HomeWork0_pbp180000.pdf)

## Homework1

In this assignment, I took a file with employee information and standardized the information that was presented
This program takes the employee data, makes sure that the information is in the correct format and that 
if the information is in the incorrect format the user will have to re-enter the information. To run this file, you 
can go to any python idle and in the run configurations make sure you enter the data file as an argument. Then you just run
the program like any other python file. Otherwise the program will give you an error. 
I think the strengths of Python for text processing is that there are so many ways in which the data can be altered to format it 
the way the user wants it. Regex gives that flexibility. It is also a very simple language and I know that Python is good for string operations which is why it is good for text processing. 
I believe in comparison to other programming languages it may not be the fastest as I have heard that a weakness of Python 
is that it can get slow. In this assignment I learned how to pickle a file, how to import a file in python without using pandas'
library and the pd.read_csv function, and I learned how to write some basic regex. While I had heard of regex and seen
it used in other people's projects, I had never personally used it, so it was interesting to learn. The splitting the data based 
on commas and removing the header from the csv file was review for me. All the formatting that was required except for
anything containing regex was review for me.

Here is the [link](Homework1_pbp180000.py) to the assignment.

## Homework2

In this assignment, I explored the many nltk functions such as the word and sentence tokenizers. I also explored the 
text object's methods. Here is the [link](Homework2_pbp180000.pdf) to the assignment.

## Homework3- HangMan/Wheel Of Fortune

In this assignment, I was given a text file containing information from an anatomy textbook. I preprocessed the data
by tokenizing it, making sure the word was larger than 5 characters, that it was actually a word, and that it wasn't a 
stopword. I also lemmatized this tokenized information to get the set of unique lemmas and do POS tagging. Then I got 
the first 50 most commonly used nouns and set them aside for the word guessing game. I then created a Hangman/Wheel
of Fortune style word guessing game, and made sure to keep score of points and whether the user wanted to end the game.
To play the game and see the assignment, here is the [link](Homework3_pbp180000.py). Enjoy playing the game! I know
that I did.