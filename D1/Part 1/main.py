import re

first_digit_regex = re.compile(r"^[^\d]*(\d).*$")

with open("data") as f:
    data = f.readlines()
    total = 0
    for line in data:
        first_digit = first_digit_regex.match(line).groups()[0]
        last_digit = first_digit_regex.match(line[::-1]).groups()[0]
        total += int(first_digit + last_digit)
    print(total)