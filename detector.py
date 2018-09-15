import sys

from synonym import Synonym
from file import File
from calculate_intersection import CalculateIntersection

tuple_size = 3
args = sys.argv[1:]

if len(args) < 3:
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
