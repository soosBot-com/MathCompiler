equation = "1 + 1 + (1 + 1 + (1 + 1))"

X=[
{"value": "1 + 1 +", "type": "text"},
{"value": [
    {
        "value": "1 + 1 + ",
        "type": "text"
    },
    {
        "value": [
            {
                "value": "1 + 1",
                "type": "text"
            }
        ],
        "type": "equation"
    }
],
    "type": "equation"
}]

import re

r = re.compile("([()])")

y = ['1 + 1 + ',  '(', '1 + 1 + ', '(', '1 + 1', ')',  ')']

opening = 0
closing = 0

for x in y:
    if x == "(":
        opening += 1
    elif x == ")":
        closing += 1

bruh = ["", ""]


