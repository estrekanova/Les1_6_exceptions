operation = input('Введите данные для вычисления. Например, + 1 2:')
operation_list = operation.split(sep=" ")

try:

    for i, item in enumerate(operation_list):
        if i == 0:
            assert item in ['+', '-', '*', '/'], 'Unknown operation'
        else:
            try:
                float(item)
            except Exception as e:
                print('Exception:', e)
                break
            else:
                assert float(item) > 0, 'Negative number'
except AssertionError as e:
    print(e)
else:
    result = 0
    if operation_list[0] == '+':
        result = float(operation_list[1]) + float(operation_list[2])
    elif operation_list[0] == '*':
        result = float(operation_list[1]) * float(operation_list[2])
    elif operation_list[0] == '-':
        result = float(operation_list[1]) - float(operation_list[2])
    elif operation_list[0] == '/':
        try:
            result = float(operation_list[1]) / float(operation_list[2])
        except ZeroDivisionError:
            print('Деление на ноль!')
    print(operation_list[1], operation_list[0], operation_list[2], '=', result)


