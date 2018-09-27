class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return str.lower()
        # str.islower(), digits and symbols return “True”, Only a lowercase letter (0-9) returns “false”.
        # str.lower(), return lower case of all elements
