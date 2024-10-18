def is_valid_expression(expr):
    bracket_stack = []
    bracket_pairs = {')': '(', '}': '{', ']': '['}

    for char in expr:
        if char in '({[':
            bracket_stack.append(char)
        elif char in ')}]':
            if not bracket_stack or bracket_stack[-1] != bracket_pairs[char]:
                return False
            bracket_stack.pop()

    return not bracket_stack

test_expressions = ["( )(( )){([( )])}", "((( )(( )){([( )])}))", " )(( )){([( )])}", "({[])}", "("]
for expression in test_expressions:
    print(f"{expression}: {is_valid_expression(expression)}")

def reverse_lines_in_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    with open(file_name, 'w') as file:
        for line in reversed(lines):
            file.write(line)


reverse_lines_in_file('myfile.txt')
