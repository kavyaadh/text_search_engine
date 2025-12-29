Mini Search Engine

A Python-based text search engine that allows users to search for words across multiple text files. The engine includes text normalization, word frequency analysis, top-k frequent word ranking, and an optional inverted index for efficient multi-file search.

Features

Text Normalization: Converts all text to lowercase, removes punctuation, handles apostrophes ('s, 'd), and stores one word per line.

Word Frequency Analysis: Counts the occurrence of each word in each file.

Top-K Frequent Words: Finds the top-k most frequent words in each file using a heap-based approach.

Search Engine: Allows users to search for a word in multiple text files, displaying frequency per file.

Inverted Index: Maps each word to the files it appears in, providing faster lookup and scalability.

Interactive CLI Interface: Users can repeatedly search for words and view top-k frequent words.


Installation

Clone the repository:

git clone <repository_url>


Ensure you have Python 3.x installed.

Place your text files in the data/ folder.

Run the program:

python src/main.py

Usage

When prompted, enter a word to search for.

The engine will display:

The files the word exists in

The frequency of the word in each file

You can also view the top-k frequent words by entering a number when prompted.

Continue searching or type N when prompted to exit.

Example Output:

Search Engine 1.0
________________________________________________
Enter the word: programming
Found in file 1: 5 times
Found in file 2: 3 times
________________________________________________
Enter k for the top k frequent words to be found: 3
The top 3 words in file one are:
Word: PROGRAMMING   Frequency: 5
Word: AND           Frequency: 3
Word: SCIENCE       Frequency: 3
The top 3 words in file two are:
Word: PROGRAMMING   Frequency: 3
Word: STUDENTS      Frequency: 2
Word: DATA         Frequency: 2
________________________________________________
Do you want to continue(Y/N)?

Future Improvements

Support for multi-word queries (AND/OR)

Phrase search and positional indexing

GUI interface for better usability

Performance optimization for large datasets

Author

Name: Kavya Adhikari

Email: adhikarikavya16@gmail.com
