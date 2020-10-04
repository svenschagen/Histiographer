import math

from Histiograph.BaseHistiograph import BaseHistiograph


class Histiograph(BaseHistiograph):

    def __init__(self, lower_bound, upper_bound, nbins):
        super().__init__(lower_bound, upper_bound, nbins)
        self._scale_factor = self._nbins / (self._max - self._min)

    def add(self, value, weight=1.0):
        if self.value_in_range(value):
            idx = math.floor(self._scale_factor * (value - self._min))
            self._buckets[idx] = self._buckets[idx] + weight
