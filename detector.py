import sys
import string

num_tuples = 3
args = sys.argv[1:]

if not args or len(args) < 3:
    print "Instructions"
    sys.exit()
elif len(args) == 4:
    num_tuples = int(args[3])
elif len(args) > 4:
    print "Instructions"
    sys.exit()

synonym_file = args[0]
control_file = args[1]
comparison_file = args[2]

syns_file = open(synonym_file, 'r').read()
# maybe do the punctuation thing?
# purpase was an attempt to handle exclamation points
# lower case all the things
file_1 = ' '.join(open(control_file, 'r').read().split()).translate(None, string.punctuation)
file_2 = open(comparison_file, 'r').read()

def synonym_dictionary(synonyms_file):
    dictionary = {}
    synonym_array = synonyms_file.split("\n")

    for row in synonym_array:
        synonyms = row.split()
        sorted_synonyms = sorted(synonyms, key=str.lower)
        hashed_synonyms_value = ''.join(sorted_synonyms)

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
            joined_tuple = ' '.join(tuple)
            tuples.append(joined_tuple)

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

def intersection(file_1_tuples, file_2_tuples):
    file_2_set = set(file_2_tuples)
    intersection_list = [value for value in file_1_tuples if value in file_2_set]
    return intersection_list

dictionary = synonym_dictionary(syns_file)
file_1_words = synonymize(file_1, dictionary)
file_2_words = synonymize(file_2, dictionary)

file_1_tuples = tuples(file_1_words, num_tuples)
file_2_tuples = tuples(file_2_words, num_tuples)

# print dictionary
# print file_1_tuples
# print file_2_tuples

intersecting_tuples = intersection(file_1_tuples, file_2_tuples)
rate_of_intersection = float(len(intersecting_tuples)) / len(file_2_tuples)
print "Plagirism Rate: {0:.0%}".format(rate_of_intersection)

# Base file to run as a main
# - Outputs instructions if no args passed in
# - Deals with bad args
# - Adds default to num_tuples
# Dictionary object
# - Passed aound to find keys
# Tuples/Words Object
# - Place where the document information is stored
# Plagirism Calculator Object
# - Object that calculates the intersection and the rate

# to deal with
# if tuple is larger than string then error out
