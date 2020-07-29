class Stats:
    def __init__(self, *args):
        self._args = args
    def mean(self):
        length = len(self._args)
        summation = sum(self._args)
        return summation / length
    def median(self):
        length = len(self._args)
        sorted_args = sorted(self._args)
        if length % 2 == 1:
            median_index = length // 2
            return sorted_args[median_index]
        else:
            middle_two_0 = length // 2 - 1
            middle_two_1 = length // 2
            middle_two_mean = (sorted_args[middle_two_0] + sorted_args[middle_two_1]) / 2
            return middle_two_mean
    def modes(self):
        # find frequencies
        counter_dict = dict()
        for arg in self._args:
            if arg in counter_dict.keys():
                counter_dict[arg] += 1
            else:
                counter_dict[arg] = 1
        # find max frequency
        max_freq = max(counter_dict.values())
        # find mode
        modes = [k for k, v in counter_dict.items() if v == max_freq]
        return modes