"""{7}--307后缀表达式求值8m18s"""
from stack import StackEnd
from infix_to_postfix import infix_to_postfix as itp


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
            operand_stack.push(int(token))
        else:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = do_math(token, operand1, operand2)
            operand_stack.push(result)

    return operand_stack.pop()


if __name__ == '__main__':
    pe = itp('1 * 2 / ( ( 3 + 4 ) - 5 * 6 )')
    print(postfix_eval(pe))
