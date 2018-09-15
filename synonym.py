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
