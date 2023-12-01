import re

first_digit_regex = re.compile(r"[^\d]*?(one|two|three|four|five|six|seven|eight|nine|\d).*$")
last_digit_regex = re.compile(r".*(one|two|three|four|five|six|seven|eight|nine|\d).*?$")

digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

with open("data") as f:
    data = f.readlines()
    total = 0
    for line in data:
        first_digit = first_digit_regex.match(line).groups()[0]
        first_digit = digits[first_digit] if first_digit in digits else first_digit
        last_digit = last_digit_regex.match(line).groups()[0]
        last_digit = digits[last_digit] if last_digit in digits else last_digit
        print(first_digit + last_digit)
        total += int(first_digit + last_digit)
    print(total)