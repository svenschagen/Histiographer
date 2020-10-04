class HealthGenerator(object):

    def __init__(self):
        self._allergen = None
        self._delay_mean = 0.0
        self._delay_spread = 0.0
        pass

    def next(self):
