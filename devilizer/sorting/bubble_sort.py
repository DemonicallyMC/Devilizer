def bubble_sort(in_lst: list[int]) -> list[int]:
    """Bubble Sort Algorithm

    Args:
        in (list[int]): List to sort.

    Returns:
        list[int]: Sorted list.
    """
    out_lst = in_lst.copy()
    done = False
    while not done:
        done = True
        for i in range(len(out_lst)-1):
            if out_lst[i] > out_lst[i+1]:
                out_lst[i], out_lst[i+1] = out_lst[i+1], out_lst[i] 
                done = True
            yield out_lst, i+1
    return out_lst