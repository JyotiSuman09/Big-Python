import sys
import os
import re
import string
import math
from collections import Counter

# =================================================================
#
# Import stop words and support words
#
print(os.getcwd())
sys.path.append(os.getcwd())
from data.stop_words import stop_words
# print(stop_words)

# Another way to read stop_words


def read_stop_words(file_path):
    try:
        with open(file_path) as file:
            text = file.read()
            exec(text, globals())
            stop_words = globals().get('stop_words', [])
            return stop_words
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        return []

# stop_words = read_stop_words('./data/stop_words.py')
# print(stop_words[:5])

support_words = []
# =================================================================

def clean_text(text):
    # Clean the text by removing punctuation, converting to lowercase, and removing stop words.
    text = re.sub(f'[{re.escape(string.punctuation)}]', '', text)
    text = text.lower()
    # remove stop words
    text = ' '.join(word for word in text.split() if word not in stop_words and word not in support_words)
    return text

def check_text_similarity(text1, text2):
    text1 = clean_text(text1)
    text2 = clean_text(text2)

    tokens1 = text1.split()
    tokens2 = text2.split()

    word_counts1 = Counter(tokens1)
    word_counts2 = Counter(tokens2)

    # Get the intersection of words
    intersection = set(word_counts1.keys()) & set(word_counts2.keys())

    # Calculate the dot product
    dot_product = sum(word_counts1[word] * word_counts2[word] for word in intersection)

    # Calculate the magnitude of each vector
    magnitude1 = math.sqrt(sum(word_counts1[word] ** 2 for word in tokens1))
    magnitude2 = math.sqrt(sum(word_counts2[word] ** 2 for word in tokens2))

    # Calculate the cosine similarity
    if magnitude1 == 0 or magnitude2 == 0:
        return 0  # Handle edge case of empty text
    else:
        similarity = dot_product / (magnitude1 * magnitude2)
        return similarity

# Example usage:
if __name__ == "__main__":
    # Example texts
    file_path1 = './data/michelle_obama_speech.txt'
    file_path2 = './data/melina_trump_speech.txt'
    text1 = "This is the first example text."
    text2 = "This is the second example text."

    try:
        with open(file_path1) as f:
            text1 = f.read()
        with open(file_path2) as f:
            text2 = f.read()
    except FileNotFoundError:
        print('File not found.')

    print(text1[:20])
    print(text2[:20])
    
    # Calculate similarity
    similarity_score = check_text_similarity(text1, text2)
    print("Similarity score:", similarity_score)
