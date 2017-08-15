import re
regex_numbers = re.compile("^((-?[0-9])+[\W+]*)+$")
regex_negative_numbers = re.compile("-[0-9]+")
regex_with_custom_delim = re.compile("^\[\W+\]+\n((-?[0-9])+[\W+]*)+$")
regex_custom_delimiters = re.compile("^\[\W+\]+\n")
regex_one_delimmiter = re.compile("\[(.*?)\]")
default_delimiter = '\n'

class Calc(object):

    def _str_to_int(self, input ):
        return [int(x) for x in input]

    def _smaller_than(self, input, thres=1000):
        return [x for x in input if x < thres]

    def _check_negatives(self, number):
        negatives = re.findall(regex_negative_numbers, number)
        if negatives:
            raise ValueError('Negatives not allowed {}'.format(negatives))

    def _split_delimiters_and_numbers(self, input):
        if regex_with_custom_delim.match(input):
            delim_raw = re.search(regex_custom_delimiters, input).group()
            delim_list = re.findall(regex_one_delimmiter, delim_raw)
            delimiter = "|".join([re.escape(item) for item in delim_list])
            numbers = re.sub(regex_custom_delimiters, '', input)
            return delimiter, numbers
        else:
            return default_delimiter, input

    def add(self, input):
        try:
            regex_delimiter, number = self._split_delimiters_and_numbers(input)
            self._check_negatives(number)
            if number == "":
                return 0
            elif regex_numbers.match(number):
                numlist = re.split(regex_delimiter, number)
                numlist = self._str_to_int(numlist)
                numlist = self._smaller_than(numlist)
                return sum(numlist)
            else:
                raise ValueError('''Input string has to be in a format  "" or "1" or "1,2" or 1,2,5,10,20... ""''')
        except Exception as e:
            print(e)

