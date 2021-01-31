def display_items(in_lst: list, current: int) -> str:
    """Display a list of values.

    Args:
        in_lst (list): The list of integers to display.
        current (int): The current column being iterated over.

    Returns:
        str: Display of values.
    """
    result = ""
    max_height = max(in_lst)
    for i in reversed(range(0, max_height+1)):
        for j, el in enumerate(in_lst):
            if el >= i:
                if j == current:
                    result += "[red]#[/red]"
                else:
                    result += "#"
            else:
                result += " "
        result += "\n"
    return result
