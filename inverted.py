import json
import os
import frequency

INDEX_FILE = "inverted_index.json"


def load_index():
    if os.path.exists(INDEX_FILE):
        with open(INDEX_FILE, "r") as file:
            return json.load(file)
    return {}


def save_index(index):
    with open(INDEX_FILE, "w") as file:
        json.dump(index, file, indent=2)


def add_file(cl_filename):
    inverted_index = load_index()
    raw_words = frequency.find_freq(cl_filename)

    for word, freq in raw_words.items():
        if word not in inverted_index:
            inverted_index[word] = {}

        inverted_index[word][cl_filename] = freq

    save_index(inverted_index)


add_file("f1_clean.txt")
add_file("f2_clean.txt")
