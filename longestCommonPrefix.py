def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            
            return ""
        
        shortest_length_string = min(strs, key=len)
        
        for i, c in enumerate(shortest_length_string):
            for rest_of_string in strs:
                if rest_of_string[i] != c:
                    return shortest_length_string[:i]
        return shortest_length_string

# s = ["flower","flow","flight"]
# s = ["dog","racecar","car"]
s = ["master", "mask", "magician", "man"]
print(longestCommonPrefix(s))
