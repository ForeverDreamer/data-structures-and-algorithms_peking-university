"""
HJ50 四则运算

描述
输入一个表达式（用字符串表示），求这个表达式的值。
保证字符串中的有效字符包括[‘0’-‘9’],‘+’,‘-’, ‘*’,‘/’ ,‘(’， ‘)’,‘[’, ‘]’,‘{’ ,‘}’。且表达式一定合法。

数据范围：表达式计算结果和过程中满足 ∣val∣≤1000  ，字符串长度满足 1≤n≤1000

输入描述：
输入一个算术表达式

输出描述：
得到计算结果

示例1
输入：
3+2*{1+2*[-4/(8-6)+7]}
输出：
25
"""

# input_str = '5-3+9*6*(6-10-2)'
input_str = '-1*(-1-1)'


def infix_to_postfix(infix_expression):
    priority = {'*': 3, '/': 3, '+': 2,  '-': 2, '(': 1}
    operands = '0123456789'

    operator_stack = []
    postfix_list = []
    token_list = list(infix_expression)

    prev = None
    i = 0
    while i < len(token_list):
        token = token_list[i]
        if token in '[{':
            token = '('
        elif token in ']}':
            token = ')'

        if token in operands:
            # 处理两位以上的操作数
            try:
                while token_list[i + 1] in operands:
                    token += token_list[i + 1]
                    i += 1
            except IndexError:
                pass
            postfix_list.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            top_token = operator_stack.pop()
            while top_token != '(':
                postfix_list.append(top_token)
                top_token = operator_stack.pop()
        else:
            # 处理负数，list(prev)[0]：处理两位以上的操作数
            if (token == '-') and (prev is None or (prev and (list(prev)[0] not in operands) and (prev != ')'))):
                postfix_list.append(token+token_list[i+1])
                token = token_list[i+1]
                i += 1
            else:
                while len(operator_stack) > 0 and (priority[operator_stack[-1]] >= priority[token]):
                    postfix_list.append(operator_stack.pop())
                operator_stack.append(token)
        prev = token
        i += 1

    while len(operator_stack) > 0:
        postfix_list.append(operator_stack.pop())
    return ' '.join(postfix_list)


def do_math(op, op1, op2):
    if op == '*':
        result = op1 * op2
    elif op == '/':
        result = op1 / op2
    elif op == '+':
        result = op1 + op2
    elif op == '-':
        result = op1 - op2
    else:
        raise ValueError('非法操作符！')

    return result


def postfix_eval(postfix_expression):
    operand_stack = []
    token_list = postfix_expression.split()
    operators = '*/+-'

    for token in token_list:
        if token not in operators:
            operand_stack.append(int(token))
        else:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = do_math(token, operand1, operand2)
            operand_stack.append(result)

    return int(operand_stack.pop())


# print(infix_to_postfix(input_str))
print(postfix_eval(infix_to_postfix(input_str)))
