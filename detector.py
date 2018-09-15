import sys

from synonym import Synonym
from file import File
from content_tuples import ContentTuples

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

def intersection(file_1_tuples, file_2_tuples):
    file_2_set = set(file_2_tuples)
    intersection_list = [value for value in file_1_tuples if value in file_2_set]
    return intersection_list

synonym_file = args[0]
control_file = args[1]
comparison_file = args[2]

dictionary = Synonym(synonym_file).dictionary()
control = File(control_file, dictionary)
comparison = File(comparison_file, dictionary)

file_1 = control.file_contents
file_2 = comparison.file_contents
file_1_words = control.synonymized_contents
file_2_words = comparison.synonymized_contents

# file_1_tuples = tuples(file_1_words, num_tuples)
file_1_tuples = ContentTuples(file_1_words,num_tuples).tuples
# file_2_tuples = tuples(file_2_words, num_tuples)
file_2_tuples = ContentTuples(file_2_words,num_tuples).tuples
# maybe do the punctuation thing?
# purpase was an attempt to handle exclamation points

intersecting_tuples = intersection(file_1_tuples, file_2_tuples)
rate_of_intersection = float(len(intersecting_tuples)) / len(file_2_tuples)
print "Plagirism Rate: {0:.0%}".format(rate_of_intersection)

# print dictionary
# print file_1_tuples
# print file_2_tuples


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
