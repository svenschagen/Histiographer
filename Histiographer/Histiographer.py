import math
from BaseHistiographer import BaseHistiographer


class Histiographer(BaseHistiographer):

    def __init__(self, lower_bound, upper_bound, nbins):
        super(self.__init__(lower_bound, upper_bound, nbins))
        self._scale_factor = self._nbins / (self._max - self._min)

    def add(self, value, weight=1.0):
        if value < self._min:
            return
        if self._max < value:
            return
        idx = math.floor(self._scale_factor * (value - self._min))
        self._buckets[idx] = self._buckets[idx] + weight
