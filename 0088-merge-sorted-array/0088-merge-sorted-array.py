class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        i = m - 1
        j = n - 1
        k = m + n - 1

        # Loop on j only: once nums2 is drained, whatever remains in the
        # nums1[0..i] prefix is already sorted and already in position.
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1