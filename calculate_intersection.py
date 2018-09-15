class CalculateIntersection:
    def __init__(self, control_tuples, comparison_tuples):
        self.control = control_tuples
        self.comparison = comparison_tuples

    def intersections(self):
        comparison_set = set(self.comparison)
        intersection_list = [value for value in self.control if value in comparison_set]
        return intersection_list

    def rate(self):
        return float(len(self.intersections())) / len(self.comparison)

    def rate_text(self):
        return "{0:.0%}".format(self.rate())
