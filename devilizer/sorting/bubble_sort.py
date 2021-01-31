def bubble_sort(in_lst: list) -> list:
    """Bubble Sort Algorithm

    Args:
        in (list): List to sort.

    Returns:
        list: Sorted list.
    """
    out_lst = in_lst.copy()
    changes = 1
    while changes:
        changes = 0
        for i in range(len(out_lst)-1):
            if out_lst[i] > out_lst[i+1]:
                out_lst[i], out_lst[i+1] = out_lst[i+1], out_lst[i] 
                changes += 1
            yield out_lst, i+1
    return out_lst