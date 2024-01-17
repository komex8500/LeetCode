class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count_set = set()
        number_set = set()
        for n in arr:
            if n not in number_set:
                number_set.add(n)
                count = arr.count(n)
                if count in count_set:
                    return False
                else:
                    count_set.add(count)
        return True
                    