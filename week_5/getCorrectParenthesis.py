from collections import deque

balanced_parentheses_string = "()))((()"


def isCorrectParenthesis(string):
    stack = []
    for s in string:
        if s == "(":
            stack.append(s)
        elif stack:
            stack.pop()
    return len(stack) == 0

def separateToUV(string):
    queue = deque(string)
    u, v = "", ""
    left, right = 0, 0
    while queue:
        char = queue.popleft()
        u += char
        if char == "(":
            left += 1
        else:
            right += 1
        if left == right:
            break

    v = "".join(list(queue))
    return u, v

def reverseParenthesis(string):
    reversedString = ""
    for char in string:
        if char == "(":
            reversedString += ")"
        else:
            reversedString += "("
    return reversedString


def changeToCorrectParenthesis(string):
    if string == "":
        return ""

    u, v = separateToUV(string)

    if isCorrectParenthesis(u):
        return u + changeToCorrectParenthesis(v)
    else:
        return "(" + changeToCorrectParenthesis(v) + ")" + reverseParenthesis(u[1:-1])


def get_correct_parentheses(balanced_parentheses_string):
    if isCorrectParenthesis(balanced_parentheses_string):
        return balanced_parentheses_string
    else:
        return changeToCorrectParenthesis(balanced_parentheses_string)


print(get_correct_parentheses(balanced_parentheses_string))