class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + "/:" + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decoded_strs = []
        i = 0
        while i < len(s):
            delim = s.find('/:', i) # search for delimiter from index i onward  
            length = int(s[i:delim]) # length is before the delimiter
            str_ = s[delim+2 : delim+2+length] # string
            decoded_strs.append(str_)
            i = delim+2+length
        return decoded_strs

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))