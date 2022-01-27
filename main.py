def flipWord(words):
    flip = words.split()
    backflip = flip[::-1]
    return " ".join(backflip)

str = "This is a test of alex's code"
rts = flipWord(str)

print(rts == "code alex's of test a is This")


def vandc(string):
    vowels = 0
    consonants = 0
    vowelset = {"a", "e", "i", "o", "u"}
    string = string.lower()
    for x in string:
        if x in vowelset:
            vowels += 1
        elif x.isalpha():
            consonants += 1

    return vowels, consonants

string = "twenty fAIVE 123 ?? iS a BOY! .. "
consandvowels = vandc(string)

print(consandvowels == (7, 10))


def validanagram(word1, word2):
    dict1 = {}
    dict2 = {}

    for x in word1:
        dict1[x] = dict1.get(x, 0) + 1
    for x in word2:
        dict2[x] = dict2.get(x, 0) + 1

    return dict1 == dict2

word1 = "oibbo"
word2 = "bobio"

valid = validanagram(word1, word2)
print(valid)

def twonums(numlist, equalnum):
    numset = set(numlist)

    for x in numlist:
        if equalnum - x in numset:
            return True
    return False

numset = [10, 15, 2, 7, 1]
givennum = 3

print(twonums(numset, givennum))

stack = []
def openclose(brackets):
    for x in brackets:
        if x == "(" or x == "[" or x == "{":
            stack.append(x)
        elif x == ")" and stack[-1] == "(":
            stack.pop()
        elif x == "]" and stack[-1] == "[":
            stack.pop()
        elif x == "}" and stack[-1] == "{":
            stack.pop()
        else:
            return False
    if len(stack) > 0 :
        return False
    else:
        return True

brackets = "([])[]({})"

print(openclose(brackets))

def maxsell(prices):
    minprice = 100
    maxsell = 0

    for x in prices:
        if x < minprice:
            minprice = x
        if x - minprice > maxsell:
            maxsell = x - minprice
    return maxsell

stockprices = [6, 9, 13, 5, 7, 10]

print(maxsell(stockprices))
