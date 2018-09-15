import string
import sys

class File(object):
    def __init__(self, file, synonym_dictionary, tuple_size):
        self.file = file
        self.tuple_size = tuple_size
        self.file_contents = self.sanitized_contents()
        self.synonymized_contents = self.synonymize(synonym_dictionary)
        self.synonymized_tuples = self.generate_tuples(self.synonymized_contents)

    def generate_tuples(self, contents):
        if len(contents) < self.tuple_size:
            print "Tuple size must be less than or equal to word count in {}".format(self.file)
            sys.exit()

        tuples = []
        max_index = len(contents) - self.tuple_size

        for idx, word in enumerate(contents):
            if max_index >=  idx:
                tuple = contents[idx:idx+self.tuple_size]
                joined_tuple = ' '.join(tuple)
                tuples.append(joined_tuple)

        return tuples

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

    def words(self):
        return self.file_contents.split()

    def synonymize(self, dictionary):
        synonymized_contents = []

        for word in self.words():
            if word in dictionary:
                synonymized_contents.append(dictionary[word])
            else:
                synonymized_contents.append(word)

        return synonymized_contents
