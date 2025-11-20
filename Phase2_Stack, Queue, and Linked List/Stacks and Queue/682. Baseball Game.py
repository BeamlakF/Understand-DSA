def calPoints(operations):
    stack = []   # this stores valid round scores

    for op in operations:

        if op == "C":
            # remove the last valid score from the stack
            stack.pop()

        elif op == "D":
            # take the last score, double it, and push to stack
            stack.append(stack[-1] * 2)

        elif op == "+":
            # sum the last two scores and push to stack
            stack.append(stack[-1] + stack[-2])

        else:
            # convert the number string to int and push
            stack.append(int(op))

    #  return the sum of all valid scores in the stack
    return sum(stack)
