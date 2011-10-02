import math
import time

class AccrualFailureDetector(object):

    SAMPLE_SIZE = 1000

    def __init__(self):
        self.last_time = None
        self.intervals = []

    def add(self, arrival=None):
        if not arrival:
            raise AttributeError("You must supply an arrival time")
        else:
            arrival = int(arrival)

        if not self.last_time:
            # Set arbitrary interval, allow suspicion to be lowered by peer.
            interval = 500
        else:
            interval = arrival - self.last_time

        self.last_time = arrival
        self.intervals.append(interval)
        if len(self.intervals) > self.SAMPLE_SIZE:
            self.intervals.pop(0)

    def clear(self):
        if self.intervals:
            del self.intervals[:]

    def phi(self, current_time=None):
        if not current_time:
            current_time = int(time.time())

        # Calculate probability
        current_interval = current_time - self.last_time
        exp = -1.0 * current_interval / self._interval_mean()
        prob = 1 - (1.0 - math.pow(math.e, exp))

        return -1 * math.log10(prob)

    def _interval_mean(self):
        return sum(self.intervals) / len(self.intervals)

