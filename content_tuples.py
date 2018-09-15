class ContentTuples(object):
    def __init__(self, content, tuple_size):
        self.tuple_size = tuple_size
        self.content = content
        self.tuples = self.__generate_tuples()

    def __generate_tuples(self):
        tuples = []
        max_index = len(self.content) - self.tuple_size

        for idx, word in enumerate(self.content):
            if max_index >=  idx:
                tuple = self.content[idx:idx+self.tuple_size]
                joined_tuple = ' '.join(tuple)
                tuples.append(joined_tuple)

        return tuples
