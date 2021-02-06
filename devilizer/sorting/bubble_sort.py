def bubble_sort(in_lst: list[int]) -> list[list[int], list[int]]:
    """Bubble Sort Algorithm

    Args:
        in (list[int]): List to sort.

    Yields:
        list[
            list[int]: Current values of list.
            list[int]: Indexes to highlight red in visualization.ß
        ]
    """
    out_lst = in_lst.copy()
    done = False
    while not done:
        done = True
        for i in range(len(out_lst)-1):
            if out_lst[i] > out_lst[i+1]:
                out_lst[i], out_lst[i+1] = out_lst[i+1], out_lst[i] 
                done = False
            yield out_lst, [i+1]
