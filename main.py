#REMOVE PASS AND FIX THIS FUNCTION
def anagram(word1, word2):
    if word1 == " ": return False
    else:
        word1 = word1.lower().replace(" ", "")
        word2 = word2.lower().replace(" ", "")
        
        splitword1 = []
        for i in word1:
            splitword1.append(i)

        for i in splitword1:
            if i in word2:
                continue
            else: return False
        return True


if __name__ == '__main__':
    #REMOVE PASS YOUR CODE GOES HERE
    word1 = input()
    word2 = input()

    anagram(word1, word2)