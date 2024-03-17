#hash_table_ds

from collections import defaultdict

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
d = defaultdict(list)

for word in strs:
    key = ''.join(sorted(word))
    d[key].append(word)

print(dict(d))
