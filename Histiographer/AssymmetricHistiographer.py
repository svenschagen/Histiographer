from BaseHistiographer import BaseHistiographer


class AssymmetricHistiographer(BaseHistiographer):
    """
    Histiographer module that sets up a arbitrary bucket size histogram.
    """
    def __init__(self, bucket_boundaries):
        super(self.__init__(bucket_boundaries))
        self._lower_edges = bucket_boundaries[0:-1]
        self._upper_edges = bucket_boundaries[1:]
        self._start = round(self._nbins/2)

    def _find_bin(self, value):
        bin_found = False

        idx = self._start
        while not bin_found:
            if value < self._lower_edges[idx]:
                idx = round(idx/2)
            elif value > self._upper_edges[idx]:
                idx = round((self._nbins + idx)/2)
            else:
                bin_found = True
        return idx

    def add(self, value, weight=1.0):
        """
        Utilise Newtonian search to find the proper bucket and add the weight.
        """
        # Check if the value is within the bounds of this histiogram.
        if value < self._min:
            return
        if self._max < value:
            return

        idx = self._find_bin(value)
        self._buckets[idx] = self._buckets[idx] + weight
        return
