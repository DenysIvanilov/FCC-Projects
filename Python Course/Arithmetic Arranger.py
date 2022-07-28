def arithmetic_arranger(problems, val=False):

    if len(problems) > 5:                                               # Too many problems
        arranged_problems = "Error: Too many problems."
        return arranged_problems

    numbers = []

    operations = []

    for i in problems:                                                  # Splitting into numbers and operations
        p = i.split()
        numbers.extend([p[0], p[2]])
        operations.extend(p[1])

    for i in operations:                                                # Only + or - operators handling
        if i == "+" or i == "-":
            continue
        else:
            arranged_problems = "Error: Operator must be '+' or '-'."
            return arranged_problems

    for i in numbers:
        if len(i) > 4:
            arranged_problems = "Error: Numbers cannot be more than four digits."       # No more than 4 digits
            return arranged_problems

    for i in numbers:                                                                   # Number only contains digits
        if i.isdigit():
            continue
        else:
            arranged_problems = "Error: Numbers must only contain digits."
            return arranged_problems

    top_row = ""
    bottom_row = ""
    dashes = ""
    values = list(map(lambda x: eval(x), problems))
    solutions = ""

    for i in range(0, len(numbers), 2):
        space_width = max(len(numbers[i]), len(numbers[i + 1])) + 2
        top_row += numbers[i].rjust(space_width)
        dashes += "-" * space_width
        solutions += str(values[i // 2]).rjust(space_width)
        if i != len(numbers) - 2:
            top_row += ' ' * 4
            dashes += ' ' * 4
            solutions += ' ' * 4

    for i in range(1, len(numbers), 2):
        space_width = max(len(numbers[i - 1]), len(numbers[i])) + 1
        bottom_row += operations[i // 2]
        bottom_row += numbers[i].rjust(space_width)
        if i != len(numbers) - 1:
            bottom_row += ' ' * 4

    if val:
        arranged_problems = "\n".join((top_row, bottom_row, dashes, solutions))
    else:
        arranged_problems = "\n".join((top_row, bottom_row, dashes))
    return arranged_problems

print(arithmetic_arranger(["1 + 1","2 + 2"], True))






