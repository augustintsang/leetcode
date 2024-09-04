class Solution:
    def similarPairs(self, words: List[str]) -> int:
        def word_to_bitmask(word):
            # Create a bitmask where each bit represents the presence of a character
            bitmask = 0
            for char in word:
                bitmask |= (1 << (ord(char) - ord('a')))
            return bitmask

        # Convert each word into a bitmask
        bitmasks = [word_to_bitmask(word) for word in words]
        
        count = 0
        # Compare each pair of bitmasks
        for i in range(len(bitmasks)):
            for j in range(i + 1, len(bitmasks)):
                if bitmasks[i] == bitmasks[j]:
                    count += 1
                    
        return count