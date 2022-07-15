"""{3}--303栈的应用：简单括号匹配11m19s"""
from stack import StackEnd


def parenthese_matcher1(tokens):
    s = StackEnd()
    balance = True
    pos = 0

    while pos < len(tokens):
        token = tokens[pos]
        if token == '(':
            s.push(token)
        else:
            if s.is_empty():
                balance = False
                break
            else:
                s.pop()
        pos += 1

    return True if balance and s.is_empty() else False


open_tokens = '([{'
close_tokens = ')]}'


def matches(open_token, close_token):
    # if open_symbol == '(':
    #     return True if close_symbol == ')' else False
    # elif open_symbol == '[':
    #     return True if close_symbol == ']' else False
    # elif open_symbol == '{':
    #     return True if close_symbol == '}' else False
    # else:
    #     raise ValueError('invalid symbol string!')
    return open_tokens.index(open_token) == close_tokens.index(close_token)


def parenthese_matcher2(tokens):
    s = StackEnd()
    balance = True
    pos = 0

    while pos < len(tokens):
        token = tokens[pos]
        if token in open_tokens:
            s.push(token)
        else:
            if s.is_empty():
                balance = False
                break
            else:
                if not matches(s.pop(), token):
                    balance = False
                    break
        pos += 1

    return True if balance and s.is_empty() else False


if __name__ == '__main__':
    print(parenthese_matcher1('((()))'))
    print(parenthese_matcher1('(()'))
    print(parenthese_matcher2('{{([][])}()}'))
    print(parenthese_matcher2('[{()]'))
