from os import system, name


def clear_screen():
    """
    When used in the terminal, will clear everything from the screen.
    """
    # for Windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux (here os.name is 'posix')
    else:
        _ = system('clear')
    print()


def solid_line(width, char="-", end_character="+"):
    """
    Prints the complete horizontal line the width of the box. Used for top, bottom and divisions
    :param width: width of the box, automatically set from what's in the box
    :param char: (-) or your choice for the lines
    :param end_character: (+) or your choice for the corners of the box
    :return 1: for interface box sizing
    """
    print(end_character + (char * (width - len(end_character) * 2)) + end_character)
    return 1


def header(inner_width, game_name, company="SIMPLE GAME COLLECTIVE", version=1.1):
    """
    Prints header banner with large scale text art. Also shows company and current version within box borders
    :param inner_width: width of the box minus outer edge
    :param game_name: large scale text art (list format)
    :param company: who the product is made by
    :param version: current version
    :return line_count: for interface box sizing
    """
    line_count = 1
    line_count += text_line(inner_width, game_name, "^")
    print(f"| BY {company:{inner_width - 8}} V{version} |")
    return line_count


def text_line(inner_width, text, position="<"):
    """
    Prints lines of text if in a list, or single line strings. Prints within box borders
    :param inner_width: width of the box minus outer edge
    :param text: to be printed
    :param position: choose from '<' for the left edge, '^' for central or '>' for the right edge. Default on left
    :return line_count: for interface box sizing
    """
    line_count = 0
    if type(text) is list:
        for line in text:
            print(f"| {line:{position}{inner_width}} |")
            line_count += 1
    else:
        print(f"| {text:{position}{inner_width}} |")
        line_count += 1
    return line_count


def empty_line(inner_width):
    """
    Prints an empty line for space purposes
    :param inner_width: width of the box minus outer edge
    :return 1: for interface box sizing
    """
    print(f"| {' ':{inner_width}} |")
    return 1


def scoreboard(inner_width):
    """
    Prints a formatted scoreboard, showing the high score holders
    :param inner_width: width of the box minus outer edge
    :return line_count: for interface box sizing
    """
    line_count = 0
    headings = ""
    first = ""
    second = ""
    third = ""
    custom_scores = list()

    # Opens the high score file.
    file = open("game_files/high_scores.txt", "r")

    # Create lines to print from the file.
    lines = 0
    for line in file:
        if lines < 3:
            parts = line.split(",")
            headings += f"{parts[0].strip():<19}"
            first += f"{parts[1].strip():<19}"
            second += f"{parts[2].strip():<19}"
            third += f"{parts[3].strip():<19}"
            lines += 1
        else:
            parts = line.split(",")
            custom_scores.append(parts[0].strip())
            custom_scores.append(parts[1].strip())
            custom_scores.append(parts[2].strip())
            custom_scores.append(parts[3].strip())

    # Closes the high score file.
    file.close()

    # Prints information.
    line_count += text_line(inner_width, headings)
    line_count += text_line(inner_width, first)
    line_count += text_line(inner_width, second)
    line_count += text_line(inner_width, third)
    line_count += empty_line(inner_width)
    line_count += text_line(inner_width, custom_scores)

    return line_count
