# Match parenthesis; returns true if matching, else false

# O(n) time


s = "(())()"


def is_correct_parenthesis(string):
    stack = []

    for i in string:
        if i == "(":
            stack.append(i)

        if i == ")":
            if len(stack) == 0:
                return False
            stack.pop()

    if len(stack) != 0:
        return False
    else:
        return True


print(is_correct_parenthesis(s))