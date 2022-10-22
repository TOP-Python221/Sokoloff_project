from main import help


new_help = help

def show_help() -> None:
    """Выводит в stdout раздел помощи."""
    print(new_help)


#
show_help()