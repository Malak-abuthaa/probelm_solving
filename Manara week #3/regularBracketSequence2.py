"""
For a string consisting of only '(', ')', '[' and ']', determine if it is a regular bracket sequence or not.

Example

For sequence = "[()()]", the output should be
solution(sequence) = true.

Input/Output

[execution time limit] 4 seconds (py3)

[input] string sequence

Guaranteed constraints:
2 ≤ sequence.length ≤ 20.

[output] boolean

true if the bracket sequence is regular, false otherwise.
"""

###################################################################

def regularBracketSequence2(sequence):
    stack = []

    for char in sequence:
        print("".join(stack))
        if char == '(' or char == '[' or char == '{':
            stack.append(char)

        elif char in [')', ']', '}']:
            if len(stack) == 0:
                return False


            elif char == ')' and stack[-1] == '(':
                stack.pop()
            elif char == ']' and stack[-1] == '[':
                stack.pop()
            elif char == '}' and stack[-1] == '{':
                stack.pop()
            else:
                return False

    return True if len(stack) == 0 else False
