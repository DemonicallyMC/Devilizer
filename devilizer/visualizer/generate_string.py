def generate_string(in_lst: list[int], current: list[int]) -> str:
    """Display a list of values.

    Args:
        in_lst (list): The list of integers to display.
        current (int): The current column being iterated over.

    Returns:
        str: Display of values.
    """
    result = ""
    max_height = max(in_lst)
    for i in range(max_height, -1, -1):
        for j, el in enumerate(in_lst):
            if el >= i:
                if j in current:
                    result += "[red]#[/red]"
                else:
                    result += "#"
            else:
                result += " "
        result += "\n"
    return result
