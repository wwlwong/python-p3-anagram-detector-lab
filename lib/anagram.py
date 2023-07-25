# your code goes here!

class Anagram:

    def __init__(self, word):
        self.word = word

    def match(self, anagrams):
        output = []
        for word in anagrams:
            if sorted([x for x in word]) == sorted([y for y in self.word]):
                output.append(word)
        
        return output
