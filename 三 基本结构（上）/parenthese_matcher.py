"""{3}--303栈的应用：简单括号匹配11m19s"""
from stack import StackEnd


def parenthese_matcher1(symbol_string):
    s = StackEnd()
    balance = True
    index = 0
    while index < len(symbol_string) and balance:
        symbol = symbol_string[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.is_empty():
                balance = False
                break
            else:
                s.pop()
        index += 1
    match = True if balance and s.is_empty() else False
    return match


def matches(open_symbol, close_symbol):
    # if open_symbol == '(':
    #     return True if close_symbol == ')' else False
    # elif open_symbol == '[':
    #     return True if close_symbol == ']' else False
    # elif open_symbol == '{':
    #     return True if close_symbol == '}' else False
    # else:
    #     raise ValueError('invalid symbol string!')
    open_symbols = '([{'
    close_symbols = ')]}'
    return open_symbols.index(open_symbol) == close_symbols.index(close_symbol)


def parenthese_matcher2(symbol_string):
    s = StackEnd()
    balance = True
    index = 0
    while index < len(symbol_string) and balance:
        symbol = symbol_string[index]
        if symbol in '([{':
            s.push(symbol)
        else:
            if s.is_empty():
                balance = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balance = False
        index += 1
    match = True if balance and s.is_empty() else False
    return match


if __name__ == '__main__':
    print(parenthese_matcher1('((()))'))
    print(parenthese_matcher1('(()'))
    print(parenthese_matcher2('{{([][])}()}'))
    print(parenthese_matcher2('[{()]'))
