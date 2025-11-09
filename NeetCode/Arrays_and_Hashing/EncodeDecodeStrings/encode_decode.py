class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string. Using the pound symbol as the delimeter
        """
        resultString = ""
        for s in strs:
            resultString += str(len(s)) + "#" + s
        return resultString
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res,i = [],0

        j = 1
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1 : j + 1 + length])
            i = j + 1 + length
        return res
