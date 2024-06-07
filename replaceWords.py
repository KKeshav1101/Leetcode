class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        s=sentence.split()
        for i in range(len(s)):
            for j in range(len(dictionary)):
                if s[i].startswith(dictionary[j]):
                    s[i]=dictionary[j]
        print(s)
        s=" ".join(s)
        return s
