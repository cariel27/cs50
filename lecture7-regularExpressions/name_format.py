import re


def get_format_name(input_str: str):
    if matches := re.search(pattern=r"^(.+), *(.+)$", string=input_str):
        # last, first = matches.groups()
        # input_str = f"{first} {last}"
        input_str = matches.group(2) + " " + matches.group(1)

    return input_str
