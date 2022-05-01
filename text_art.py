# Hangman written in text art, to be used for the headers.
hangman = [" _   _    _    _   _  ____ __  __    _    _   _ ",
           "| | | |  / \  | \ | |/ ___|  \/  |  / \  | \ | |",
           "| |_| | / _ \ |  \| | |  _| |\/| | / _ \ |  \| |",
           "|  _  |/ ___ \| |\  | |_| | |  | |/ ___ \| |\  |",
           "|_| |_/_/   \_\_| \_|\____|_|  |_/_/   \_\_| \_|",
           ""]

# Used to show the three difficulty level in the game as user Avatars.
difficulty_art = [
    "{:^17} | {:^17} | {:^17}".format("  0/$", ' 0 ', "  0 "),
    "{:^17} | {:^17} | {:^17}".format(" /| ", ' /|\ ', "  /|\ "),
    "{:^17} | {:^17} | {:^17}".format(" / \ ", ' / \ ', "/ "),
    "{:^17} | {:^17} | {:^17}".format("Easy (7Hp)", "Normal (6Hp)", "Hard(5Hp)")
    ]

