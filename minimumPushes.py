class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        freq=[0]*26
        for c in word:
            freq[ord(c)-ord('a')]+=1
        freq.sort(reverse=True)
        total_key_presses=0
        for index,count in enumerate(freq):
            if count==0:
                break
            total_key_presses += (index//8+1)*count
        return total_key_presses
