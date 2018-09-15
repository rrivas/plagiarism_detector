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

class File(object):
    def __init__(self, file):
        self.file = file
        self.file_contents = self.sanitized_contents()

    def __get_file_contents(self):
        return open(self.file, 'r').read()

    def __singularize_whitespace(self, contents):
        return contents.split()

    def __join_file_contents(self, contents):
        return ' '.join(contents)

    def __remove_punctuation(self, contents):
        return contents.translate(None, string.punctuation)

    def __lower_case(self, contents):
        return contents.lower()

    def sanitized_contents(self):
        contents = self.__get_file_contents()
        contents = self.__singularize_whitespace(contents)
        contents = self.__join_file_contents(contents)
        contents = self.__remove_punctuation(contents)
        contents = self.__lower_case(contents)

        return contents


control = File(control_file)
comparison = File(comparison_file)

class Synonym(object):
    def __init__(self, file):
        self.file = file
        self.file_contents = open(self.file, 'r').read()
        self.synonym_dictionary = self.generate_dictionary()

    def dictionary(self):
        return self.synonym_dictionary

    def generate_dictionary(self):
        dictionary = {}
        synonym_array = self.file_contents.split("\n")

        for row in synonym_array:
            synonyms = row.split()
            sorted_synonyms = sorted(synonyms, key=str.lower)
            hashed_synonyms_value = ''.join(sorted_synonyms)

            for synonym in synonyms:
                dictionary[synonym] = hashed_synonyms_value

        return dictionary
# maybe do the punctuation thing?
# purpase was an attempt to handle exclamation points
# lower case all the things
file_1 = control.file_contents
file_2 = comparison.file_contents

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

dictionary = Synonym(synonym_file).dictionary()
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
