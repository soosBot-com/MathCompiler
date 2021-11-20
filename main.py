import sys
import math
import re

text = input(": ")

text = text.replace(" ", "")


# print("Equation without spaces: " + text)


def is_number(value):
    return value.isnumeric()


def is_operator(value):
    return value in ["+", "-", "*", "/", "^"]


def parse_equation(equation):
    temp_number = ""
    items = []

    for char in equation:
        if is_number(char):
            temp_number += char
        else:
            if temp_number:
                items.append({
                    "value": temp_number,
                    "type": "number"
                })
                temp_number = ""

            if is_operator(char):
                items.append({
                    "value": char,
                    "type": "operator"
                })

    if temp_number:
        items.append({
            "value": temp_number,
            "type": "number"
        })

    return items


parsed_equation = parse_equation(text)

if len(parsed_equation) == 0:
    raise SyntaxError("INVALID SYNTAX: NO NUMBERS OR OPERATIONS")

print("Parsed equation: " + str(parsed_equation))

# Checks

if parsed_equation[0]["type"] == "operator":
    raise SyntaxError("INVALID SYNTAX: MISPLACED OPERATOR")


def solve_equation(equation):
    value = equation[0]["value"]
    equation.pop(0)
    operating_next_value = False
    next_operator = ""

    for x in equation:
        type_ = x["type"]
        if operating_next_value:
            if type_ == "operator":
                raise SyntaxError("INVALID SYNTAX: MISPLACED OPERATOR")
            if next_operator == "+":
                value = int(value) + int(x["value"])
            elif next_operator == "-":
                value = int(value) - int(x["value"])
            elif next_operator == "*":
                value = int(value) * int(x["value"])
            elif next_operator == "/":
                value = int(value) / int(x["value"])
            elif next_operator == "^":
                value = int(value) ** int(x["value"])
            next_operator = ""
            operating_next_value = False
        if type_ == "operator":
            operating_next_value = True
            next_operator = x["value"]
    return value


print(str(solve_equation(parsed_equation)))
