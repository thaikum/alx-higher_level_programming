#!/usr/bin/python3

"""
file appender
"""


def append_after(filename="", search_string="", new_string=""):
    """
    appender
    """
    lines = []
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    with open(filename, "w", encoding="utf-8") as f:
        new_lines = []

        for line in lines:
            new_lines.append(line)
            if search_string in line:
                new_lines.append(new_string)

        f.writelines(new_lines)
