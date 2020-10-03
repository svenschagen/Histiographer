from abc import ABC, abstractmethod


class BaseHistiographer(ABC):

    def __init__(self, lower_bound, upper_bound, nbins):
        self._min = lower_bound
        self._max = upper_bound
        self._nbins = nbins
        self._buckets = [0.0 for _ in range(self._nbins)]

    @abstractmethod
    def add(self, value, weight):
        return
