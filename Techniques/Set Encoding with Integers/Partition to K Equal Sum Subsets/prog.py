from functools import cache


class Solution:
    def canPartitionKSubsets(self, arr: List[int], k: int) -> bool:
        """
        LeetCode: 698. Partition to K Equal Sum Subsets

        Given an integer array nums and an integer k,
        return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

        Set Encoding by Integers Solution:
        """
        arr.sort(reverse=True)

        totalSum = sum(arr)
        targetSum, remainder = divmod(totalSum, k)

        if remainder:
            return False

        # 1 << len(arr) is the total number of subsets possible i.e 2^n
        subsetSums = [0]*(1 << len(arr))

        # compute all subset sums
        for i, _ in enumerate(arr):
            for S in range(1 << i):
                subsetSums[S | (1 << i)] = subsetSums[S]+arr[i]

        # filter out all subsets whose sum != targetSum
        subsetSums = list(
            filter(lambda x: x[1] == targetSum, enumerate(subsetSums)))

        setsWithSumK = [S for S, sumS in subsetSums]

        chosenSets = []
        ans = False

        # array must be sorted in reverse or dynamic programming will yield wrong answer
        # brute force is possible by disabling DP
        # check if there exists k-1 disjoint subsets whose sum is target.
        # which implies the kth subset must exist

        @cache
        def searchAns(start=0, prev=None):
            nonlocal ans
            if len(chosenSets)+1 == k:
                ans = True
            if ans:
                return
            for A in setsWithSumK[start:]:
                if not chosenSets or all(A & B == 0 for B in chosenSets):
                    chosenSets.append(A)
                    searchAns(start+1, chosenSets[-1])
                    chosenSets.pop()

        searchAns()

        return ans
