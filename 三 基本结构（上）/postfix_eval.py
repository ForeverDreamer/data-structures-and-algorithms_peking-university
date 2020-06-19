"""{7}--307后缀表达式求值8m18s"""
from stack import StackEnd


def do_math(op, op1, op2):
    if op == '*':
        result = op1 * op2
    elif op == '/':
        result = op1 / op1
    elif op == '+':
        result = op1 + op1
    elif op == '-':
        result = op1 - op1
    else:
        raise ValueError('非法操作符！')

    return result


def postfix_eval(postfix_expression):
    operand_stack = StackEnd()
    token_list = postfix_expression.split()
    operators = '*/+-'

    for token in token_list:
        if token not in operators:
            operand_stack.push(token)
        else:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = do_math(token, operand1, operand2)
            operand_stack.push(result)

    return operand_stack.pop()
