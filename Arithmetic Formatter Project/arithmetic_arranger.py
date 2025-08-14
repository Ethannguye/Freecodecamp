def arithmetic_arranger(problems, answers = False):
    #Too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    numbers =[]
    operations = []
    values = []

    #Validation
    for p in problems:
        parts = p.split()
        if len(parts) != 3:
            return  "False"

        num1, opt, num2 = parts

        if opt not in {'+', '-'}:
            return "Error: Operator must be '+' or '-'."

        if not (num1.isdigit() and num2.isdigit()):
            return 'Error: Numbers must only contain digits.'

        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        numbers.extend([num1,num2])
        operations.append(opt)
        if opt == '+':
            values.append(int(num1)+int(num2))
        else:
            values.append(int(num1) - int(num2))

    #Formatting
    top_line = ''
    bot_line = ''
    dash_line = ''
    answer_line = ''

    for i in range(0, len(numbers), 2):
        space_width = max(len(numbers[i]), len(numbers[i + 1])) + 2

        top_line += numbers[i].rjust(space_width)
        bot_line += operations[i // 2] + numbers[i + 1].rjust(space_width - 1)
        dash_line += "-" * space_width
        if answers:
            answer_line += str(values[i // 2]).rjust(space_width)

        if i != len(numbers) - 2:
            top_line += ' '*4
            bot_line += ' ' * 4
            dash_line += ' '*4
            if answers:
                answer_line += ' '*4

    # Return final string
    if answers:
        return f"{top_line}\n{bot_line}\n{dash_line}\n{answer_line}"
    else:
        return f"{top_line}\n{bot_line}\n{dash_line}"
