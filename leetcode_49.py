#hash_table_ds

from collections import defaultdict

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
d = defaultdict(list)

for word in strs:
    key = ''.join(sorted(word))
    d[key].append(word)

print(dict(d))

# another solution with hash tables
from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        letters = defaultdict(list)
        for word in strs:
            letters[tuple(sorted(word[:]))].append(word)
        return list(letters.values())
        
