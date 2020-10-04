from abc import ABC, abstractmethod


class BaseHistiograph(ABC):

    def __init__(self, lower_bound, upper_bound, number_bins):
        self._min = lower_bound
        self._max = upper_bound
        self._nbins = number_bins
        self._buckets = [0.0 for _ in range(self._nbins)]

    def value_in_range(self, value):
        if value < self._min:
            return False
        if self._max < value:
            return False
        return True

    @abstractmethod
    def add(self, value, weight):
       pass
