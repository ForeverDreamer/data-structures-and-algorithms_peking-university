"""{6}--606树的应用：表达式解析（下）15m15s"""
import operator

from stack import StackEnd
from binary_tree_linked_list import BinaryTree


def build_parse_tree(expression):
    exp_list = list(expression)
    parse_stack = StackEnd()
    parse_tree = BinaryTree('')
    parse_stack.push(parse_tree)
    current_tree = parse_tree

    for token in exp_list:
        if token == '(':
            current_tree.insert_left('')
            parse_stack.push(current_tree)
            current_tree = current_tree.left_child
        elif token not in ['+', '-', '*', '/', ')']:
            current_tree.root_data = int(token)
            current_tree = parse_stack.pop()
        elif token in ['+', '-', '*', '/']:
            current_tree.root_data = token
            current_tree.insert_right('')
            parse_stack.push(current_tree)
            current_tree = current_tree.right_child
        elif token == ')':
            current_tree = parse_stack.pop()
        else:
            raise ValueError('无效字符！')

    return parse_tree


def evaluate(parse_tree):
    operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    left_child = parse_tree.left_child
    right_child = parse_tree.right_child

    if left_child and right_child:
        fn = operators[parse_tree.root_data]
        return fn(evaluate(left_child), evaluate(right_child))
    else:
        return parse_tree.root_data


def print_exp(parse_tree):
    exp = ''
    if parse_tree:
        if parse_tree.left_child or parse_tree.right_child:
            exp = '(' + print_exp(parse_tree.left_child)
            exp += str(parse_tree.root_data)
            exp += print_exp(parse_tree.right_child) + ')'
        else:
            exp += str(parse_tree.root_data)

    return exp


if __name__ == '__main__':
    par_tree = build_parse_tree('(4+((5+8)/(7*3))')
    par_tree.preorder()
    print(evaluate(par_tree))
    print(print_exp(par_tree))
