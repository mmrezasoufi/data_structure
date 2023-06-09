# This script checks the matching of parentheses by using the stack

from stack import Stack


def is_matched(expression):
    left = '({['
    right = ')}]'
    stack = Stack()

    for char in expression:
        if char in left:
            stack.push(char)
        elif char in right:
            if stack.is_empty():
                return False
            if right.index(char) != left.index(stack.pop()):
                return False

    return stack.is_empty()
