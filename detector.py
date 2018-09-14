import sys
import string

syns_file = open(sys.argv[1], 'r').read()
# maybe do the punctuation thing?
# purpase was an attempt to handle exclamation points
file_1 = ' '.join(open(sys.argv[2], 'r').read().split()).translate(None, string.punctuation)
file_2 = open(sys.argv[3], 'r').read()
num_tuples = int(sys.argv[4])

def synonym_dictionary(synonyms_file):
    dictionary = {}
    synonym_array = synonyms_file.split("\n")

    for row in synonym_array:
        synonyms = row.split()
        sorted_synonyms = sorted(synonyms, key=str.lower)
        hashed_synonyms_value = ''.join([str(x) for x in sorted_synonyms])

        for synonym in synonyms:
            dictionary[synonym] = hashed_synonyms_value

    return dictionary

def tuples(words, tuple_size):
    # Improvements: remove newlines and convert to spaces
    tuples = []
    max_index = len(words) - tuple_size

    for idx, word in enumerate(words):
        if max_index >=  idx:
            tuple = words[idx:idx+tuple_size]
            tuples.append(tuple)

    return tuples

def synonymize(input_file, dictionary):
    words = input_file.split()
    synonymized_file = []

    for word in words:
        if word in dictionary:
            synonymized_file.append(dictionary[word])
        else:
            synonymized_file.append(word)

    return synonymized_file

dictionary = synonym_dictionary(syns_file)
file_1_words = synonymize(file_1, dictionary)
file_2_words = synonymize(file_2, dictionary)

file_1_tuples = tuples(file_1_words, num_tuples)
file_2_tuples = tuples(file_2_words, num_tuples)

print dictionary

print file_1_tuples
print file_2_tuples

