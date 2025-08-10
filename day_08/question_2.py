def calculate(s: str) -> int:
    s = s.replace(" ", "")
    current_num = 0
    last_num = 0
    result = 0
    operation = '+'
    for i, ch in enumerate(s):
        if ch.isdigit():
            current_num = current_num * 10 + int(ch)
        if not ch.isdigit() or i == len(s) - 1:
            if operation == '+':
                result += last_num
                last_num = current_num
            elif operation == '-':
                result += last_num
                last_num = -current_num
            elif operation == '*':
                last_num *= current_num
            elif operation == '/':
                last_num = int(last_num / current_num) 
            operation = ch
            current_num = 0
    result += last_num
    return result

print(calculate("3+2*2"))    