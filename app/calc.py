import re
regex_numbers = re.compile("^(-?([0-9])+[\W]?)+$")             #
regex_negative_numbers = re.compile("-[0-9]+")
regex_with_custom = re.compile("^\[\W\]\n(-?([0-9])+[\W])+(-?[0-9]+)$") #
regex_delimiter_brackets = re.compile("^\[\W+\]\n")
default_delimiter = '\n|,'

class Calc(object):

    def _check_negatives(self, number):
        negatives = re.findall(regex_negative_numbers, number)
        if negatives:
            raise ValueError('Negatives not allowed {}'.format(negatives))


    def _preprocess(self, input):
        if regex_with_custom.match(input):
            m = re.search(regex_delimiter_brackets, input)
            delimiter = "\\"+m.group(0)[1:-2]                     # do this better
            numbers = re.sub(regex_delimiter_brackets, '', input)
            return delimiter, numbers
        else:
            return default_delimiter, input

    def add(self, input):
        regex_delimiter, number = self._preprocess(input)
        self._check_negatives(number)
        if number == "":
            return 0
        elif regex_numbers.match(number):
            numlist = re.split(regex_delimiter, number)
            numlist = map(int, numlist)
            numlist = filter(lambda x: x if x < 1000 else 0, numlist)
            return sum(numlist)
        else:
            raise ValueError('''Input string has to be in a format  "" or "1" or "1,2" or 1,2,5,10,20... ""''')


