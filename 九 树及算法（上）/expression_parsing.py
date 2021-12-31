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


def evaluate(parse_tree):
    left = parse_tree.left
    right = parse_tree.right

    if left and right:
        fn = operators[parse_tree.data]
        return fn(evaluate(left), evaluate(right))
    else:
        return parse_tree.data


def print_exp(parse_tree):
    exp = ''
    if parse_tree:
        if parse_tree.left and parse_tree.right:
            exp = '(' + print_exp(parse_tree.left)
            exp += str(parse_tree.data)
            exp += print_exp(parse_tree.right) + ')'
        else:
            exp += str(parse_tree.data)

    return exp


if __name__ == '__main__':
    par_tree = build_parse_tree('(4+((5+8)/(7*3))')
    par_tree.preorder()
    print(print_exp(par_tree))
    print(evaluate(par_tree))

#     +
#   /   \
#  4     /
#      /   \
#     +     *
#    / \    / \
#   5   8  7  3
