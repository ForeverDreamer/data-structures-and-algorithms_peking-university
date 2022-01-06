"""{6}--606树的应用：表达式解析（下）15m15s"""
import operator

from stack import StackEnd
from binary_tree_linked_list import BTNode


def build_parse_tree(expression):
    exp_list = list(expression)
    parse_stack = StackEnd()
    root_node = BTNode('')
    parse_stack.push(root_node)
    current_node = root_node

    for token in exp_list:
        if token == '(':
            current_node.insert_left('')
            parse_stack.push(current_node)
            current_node = current_node.left
        elif token not in ['+', '-', '*', '/', ')']:
            current_node.data = int(token)
            current_node = parse_stack.pop()
        elif token in ['+', '-', '*', '/']:
            current_node.data = token
            current_node.insert_right('')
            parse_stack.push(current_node)
            current_node = current_node.right
        elif token == ')':
            current_node = parse_stack.pop()
        else:
            raise ValueError('无效字符！')

    return root_node


operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}


def evaluate(node):
    left = node.left
    right = node.right

    if left and right:
        fn = operators[node.data]
        return fn(evaluate(left), evaluate(right))
    else:
        return node.data


def print_exp(node):
    exp = ''
    if node.left and node.right:
        exp = '(' + print_exp(node.left)
        exp += str(node.data)
        exp += print_exp(node.right) + ')'
    else:
        exp += str(node.data)

    return exp


if __name__ == '__main__':
    r_node = build_parse_tree('(4+((5+8)/(7*3))')
    r_node.preorder()
    print(print_exp(r_node))
    print(evaluate(r_node))

#     +
#   /   \
#  4     /
#      /   \
#     +     *
#    / \    / \
#   5   8  7   3
