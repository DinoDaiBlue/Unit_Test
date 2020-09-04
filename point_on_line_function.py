# point_on_line_function
def point_on_line(point1, point2, input):
    x1 = point1[0]
    y1 = point1[1]
    x2 = point2[0]
    y2 = point2[1]
    if (x1 - x2) == 0:
        return "NaN"
    elif (y1 - y2) == 0:
        return input
    else:
        k = (y2 - y1)/(x2 - x1)
        b = y1 - k * x1
        output = input * k + b
        return output


def point_on_line_tf(point1, point2, input):
    x1 = point1[0]
    y1 = point1[1]
    x2 = point2[0]
    y2 = point2[1]
    if (x1 - x2) == 0:
        if input[0] == x1:
            return "True"
        else:
            return "False"
    elif (y1 - y2) == 0:
        if input[1] == y1:
            return "True"
        else:
            return "False"
    else:
        k = (y2 - y1)/(x2 - x1)
        b = y1 - k * x1
        output = input[0] * k + b
        if output == input[1]:
            return "True"
        else:
            return "False" 
