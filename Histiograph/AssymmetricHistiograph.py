from Histiograph.BaseHistiograph import BaseHistiograph

class AssymmetricHistiograph(BaseHistiograph):
    """
    Histiograph module that sets up a arbitrary bucket size histogram.
    """
    def __init__(self, bucket_boundaries):
        super().__init__(bucket_boundaries[0], bucket_boundaries[-1], len(bucket_boundaries)-1)
        self._lower_edges = bucket_boundaries[0:-2]
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
        # Check if the value is within the bounds of this histiograph.
        if self.value_in_range(value):
            idx = self._find_bin(value)
            self._buckets[idx] = self._buckets[idx] + weight
