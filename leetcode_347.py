#hash_table_ds

from collections import defaultdict
class Solution(object):
    def topKFrequent(self, nums, k):
        freq_dict = defaultdict(int)

        for num in nums:
            freq_dict[num] += 1

        top_k = []

        for _ in range(k):
            max_freq = max(freq_dict.values())
            max_num = None
            for num, freq in freq_dict.items():
                if freq == max_freq:
                    max_num = num
                    break
            top_k.append(max_num)
            del freq_dict[max_num] 

        return top_k
