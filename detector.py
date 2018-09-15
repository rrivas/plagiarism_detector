import sys

from synonym import Synonym
from file import File
from content_tuples import ContentTuples
from calculate_intersection import CalculateIntersection

tuple_size = 3
args = sys.argv[1:]

if not args or len(args) < 3:
    print "Instructions"
    sys.exit()
elif len(args) == 4:
    tuple_size = int(args[3])
elif len(args) > 4:
    print "Instructions"
    sys.exit()

synonym_file = args[0]
control_file = args[1]
comparison_file = args[2]

dictionary = Synonym(synonym_file).dictionary()
control = File(control_file, dictionary, tuple_size)
comparison = File(comparison_file, dictionary, tuple_size)

print CalculateIntersection(control.synonymized_tuples, comparison.synonymized_tuples).rate_text()

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
