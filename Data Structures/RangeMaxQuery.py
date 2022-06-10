class RangeMaxQuery:
    """Range maximum query

    maintains a table t, can read/write items t[i],
    and query range_max(i,k) = max{ t[i], t[i + 1], ..., t[k - 1]}
    :complexity: all operations in O(log n), for n = len(t)
    """
    def __init__(self, t, INF=float('-inf')):
        self.INF = INF
        self.N = 1
        while self.N < len(t):                     # find size N
            self.N *= 2
        self.s = [self.INF] * (2 * self.N)
        for i in range(len(t)):                    # store values of t
            self.s[self.N + i] = t[i]              # in the leaf nodes
        for p in range(self.N - 1, 0, -1):         # fill inner nodes
            self.s[p] = max(self.s[2 * p], self.s[2 * p + 1])

    def __getitem__(self, i):
        return self.s[self.N + i]

    def __setitem__(self, i, v):
        """ sets t[i] to v.
            :complexity: O(log len(t))
        """
        p = self.N + i
        self.s[p] = v
        p //= 2                                    # climb up the tree
        while p > 0:                               # update node
            self.s[p] = max(self.s[2 * p], self.s[2 * p + 1])
            p //= 2

    def range_max(self, i, k):
        """:returns:  max{ t[i], t[i + 1], ..., t[k - 1]}
        :complexity: O(log len(t))
        """
        return self._range_max(1, 0, self.N, i, k)

    def _range_max(self, p, start, span, i, k):
        """returns the maximum in t in the indexes [i, k) intersected
           with [start, start + span).
           p is the node associated to the later interval.
        """
        if start + span <= i or k <= start:        # disjoint intervals
            return self.INF
        if i <= start and start + span <= k:       # contained intervals
            return self.s[p]
        left = self._range_max(2 * p, start, span // 2,
                               i, k)
        right = self._range_max(2 * p + 1, start + span // 2, span // 2,
                                i, k)
        return max(left, right)
