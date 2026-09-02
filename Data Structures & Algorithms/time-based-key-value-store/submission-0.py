from sortedcontainers import SortedDict

class TimeMap:

    def __init__(self):
        self.d = defaultdict(SortedDict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""

        timestamps = self.d[key]
        idx = timestamps.bisect_right(timestamp) - 1

        if idx >= 0:
            closest = timestamps.iloc[idx]
            return timestamps[closest]

        return ""
