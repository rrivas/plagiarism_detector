import sys
import argparse

from synonym import Synonym
from file import File
from calculate_intersection import CalculateIntersection

args = sys.argv[1:]

parser = argparse.ArgumentParser(description='Outputs a rate of plagiarizations based on the number of N-tuples in the comparison file that appear in the control file, where the tuples are compared by accounting for synonyms provided in the synonym file.')
parser.add_argument('-s','--synonym_file', help='Synonym file path', required=True)
parser.add_argument('-c','--comparison_file', help='Comparison file path', required=True)
parser.add_argument('-o','--control_file', help='Control file path', required=True)
parser.add_argument('-t','--tuple_size', help='Size of comparison tuple',  default=3, required=False)
args = parser.parse_args()

tuple_size = int(args.tuple_size)

dictionary = Synonym(args.synonym_file).dictionary()
control = File(args.control_file, dictionary, tuple_size)
comparison = File(args.comparison_file, dictionary, tuple_size)

print control.synonymized_tuples
print comparison.synonymized_tuples
print CalculateIntersection(control.synonymized_tuples, comparison.synonymized_tuples).rate_text()
