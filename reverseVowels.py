class Solution(object):
    def reverseVowels(self, s):
        vow = set('aeiouAEIOU')  # Set for faster lookups
        s = list(s)  # Convert string to list for easy swapping
        left, right = 0, len(s) - 1  # Two-pointer approach
        
        while left < right:
            if s[left] not in vow:
                left += 1
            elif s[right] not in vow:
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]  # Swap vowels
                left += 1
                right -= 1
        
        return ''.join(s)  # Convert list back to string
