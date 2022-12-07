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

## Homework4- Exploration of WordNet and SentiWordNet

In this assignment, I explored the libraries of WordNet and SentiWordNet. I found out the various functionalities of these 
libraries. I found out that WordNet could give a  lot of information about the word itself involving the definition, or
even the hierarchy of these words. SentiWordNet which is built on top of WordNet gave me the functionality of 
understanding the sentiment behind these words by giving it a positive, negative, and objective score. You can
access the [link](Homework4_pbp180000.pdf) to the assignment here.

## Homework5 -N-Grams
In this assignment, I explored the nltk libraries to create unigrams and bigrams. I created a dictionary of unigrams and 
bigrams for the documents that were passed in. These documents contained vocabulary from the English, French, and 
Italian languages. These dictionaries were then pickled. Then in another python file, I unpickled the dictionaries, and
took in a test document, in which I had to predict whether that sentence was English, French or Italian. I did this by
calculating the probabilities of each language and choosing the highest probability. The result was then outputted into 
another document. You can accesss [the first part](Homework5_pbp180000_and_kxn180023_Program1.py) and 
[the second part](Homework5_pbp180000_and_kxn180023_Program2.py) here.

## Homework6 - WebCrawler
In this assignment, I crawled the web and looked for further urls from a wikipedia page, to create a dictionary of facts about
the topic- Halloween- that I was crawling for information about. I had to go through the urls, and use tf-idf to figure out the
most important terms in relation to the topic of Halloween. This allowed me to create a database/information bank with 
facts about Halloween. You can access the [link](Homework6_pbp180000_and_kxn180023.py) to the assignment here.

## Homework7 - Parsing
In this assignment, I created a sentence and applied the PSG, SRL, and Dependecy Parsing to break the sentence down
and get information about it. Then I wrote a paragraph of the pros and cons of each of the parsers. You can access the 
[link](Homework7_pbp180000.pdf) to the assignment here.

## Homework8 - Author Attribution
In this assignment, I tried various models like Bernoulli Naive Bayes, Logistic Regression, and a MLPClassifier(Neural
Networks) to predict who the author of the text is. I looked at the federalist papers and used the tfidf vectorizer to vectorize
the document to put into the models and adjusted the hyperparameters to get the best accuracy possible. You can access the 
[link](Author_Attribution_pbp180000.pdf) to the assignment here.

## Homework9 - ACL Paper Summary
For this assignment, I took a long paper from the Long Paper Proceedings of the 2021 ACL conference and read it. Then I 
created an informative summary of the research paper and of its importance and contributions. You can read the summary
of the paper "How Did This Get Funded?! Automatically Identifying Quirky Scientific Achievements", at this 
[link](ACL_Paper_Summary_pbp180000_and_kxn180023.pdf) here.

## Homework10 - Chatbot
For this assignment, I created a chatbot that gives recipes based on what the user likes and dislikes. I used
a multitude of NLP concepts and got the knowledge base by using a recipe database on the web. 
You can read the project report, at this [link](Chatbot_Report_pbp180000_and_kxn180023.pdf) here.
 The link to the actual [chatbot](Chatbot_pbp180000_and_kxn180023_Program1.py) is here.

## Homework9 - Text Classification
For this assignment, I took a dataset from kaggle that identifies sentences as either belonging to the biology,
chemistry, or physics topic. I tried using a sequential model, a RNN, and using embeddings to see how well the models 
could predict the topic of the sentence. 
You can see the code and the [results](text_classification_pbp180000_and_kxn180023.ipynb_-_Colaboratory (1).pdf) here.