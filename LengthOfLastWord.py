#Given a string s consisting of words and spaces, return the length of the last word in the string.

def LengthOfLastWord(s:str)-> int:
    s = s.strip()
    word = ""
    for char in s:
        if char != " ":
            word = word+char
        else:
            word = ""
    return len(word)

k = LengthOfLastWord("the moon is highest")
print("Legth of last word in the sentence is: ", k)