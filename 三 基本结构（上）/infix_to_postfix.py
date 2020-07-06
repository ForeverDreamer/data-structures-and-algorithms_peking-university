"""{6}--306表达式转换（下）12m36s"""
from stack import StackEnd


def infix_to_postfix(infix_expression):
    priority = {'*': 3, '/': 3, '+': 2,  '-': 2, '(': 1}
    operands = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'

    operator_stack = StackEnd()
    postfix_list = []
    token_list = infix_expression.split()

    for token in token_list:
        # if token in operands or token in digits:
        if token in operands or token in digits:
            postfix_list.append(token)
        elif token == '(':
            operator_stack.push(token)
        elif token == ')':
            top_token = operator_stack.pop()
            while top_token != '(':
                postfix_list.append(top_token)
                top_token = operator_stack.pop()
        else:
            while (not operator_stack.is_empty()) and (priority[operator_stack.peek()] >= priority[token]):
                postfix_list.append(operator_stack.pop())
            operator_stack.push(token)

    while not operator_stack.is_empty():
        postfix_list.append(operator_stack.pop())
    return ' '.join(postfix_list)


if __name__ == '__main__':
    # AB*CD+EF*-/
    print(infix_to_postfix('A * B / ( ( C + D ) - E * F )'))
