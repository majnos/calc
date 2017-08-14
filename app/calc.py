import re

class Calc(object):

    def add(self, input):
        regex_one_number = re.compile("^(-?[0-9]+)$")
        # regex_two_numbers = re.compile("^([0-9]+),([0-9]+)$")
        regex_n_numbers = re.compile("^(-?([0-9])+[\n|,])+-?[0-9]+$")
        regex_delimiter = '\n|,'
        if input == "":
            return 0
        elif regex_one_number.match(input):
            return int(input)
        # elif regex_two_numbers.match(input):
        #     numlist = input.split(",")
        #     numlist = map(int, numlist)
        #     return sum(numlist)
        elif regex_n_numbers.match(input):
            numlist = re.split(regex_delimiter, input)
            numlist = map(int, numlist)
            return sum(numlist)
        else:
            raise ValueError('''Input string has to be in a format  "" or "1" or "1,2" or 1,2,5,10,20... ""''')
            # raise ValueError('''Input string has to be in a format  “” or “1” or “1,2”''')


