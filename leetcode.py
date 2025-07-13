class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        haystack_lower=haystack.lower()
        needle_lower=needle.lower()
        return haystack_lower.find(needle_lower)
haystack="sadbutsad"
needle= "sad"
solutions= Solution()
result= solutions.strStr(haystack, needle)
print(result)