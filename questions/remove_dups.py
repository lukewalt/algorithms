def remove_duplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        # establishes an extra pointer along with the index that is generated by the loop.
        p = 0

        # always skips first element by default. each comparison will look at the value prior
        # to see if they are equal. if they are, nothing is mutated until reaching a new value.
        # the pointer keeps a reference to last unique num so that when the loop
        # encounters a new number, it is set to the pointer+1
        for (i, num) in enumerate(nums):
            if i == 0:
                continue
            if num != nums[i - 1]:
                p += 1
                nums[p] = num

        return p + 1


d = remove_duplicates([0, 1, 1, 2, 3, 4, 4, 4, 5, 6])
print(d)