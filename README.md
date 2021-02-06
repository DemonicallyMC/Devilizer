# Devilizer

A plug-and-play sorting algorithm visualizer.

## State of Development

At this early stage, Devilizer is functional in its plug-and-play architecture, but lacks in terms of it's `__main__.py` usability. In the future, we plan to implement many example algorithms which can be visualized, and you can expect to see many implemented in the coming weeks.

### How to get started with Devilizer

To see a basic example of Devilizer, follow the steps below:

1. Ensure that `pipenv` is installed on your system.
2. Clone this repository.
3. From the root of the repository folder, run `pipenv run python3 -m devilizer` to see an example.

Currently, this will visualize the bubble sort algorithm.

### How to use Devilizer effectively

Devilizer's main draw is its ability to visualize _any_ sorting algorithm.

To do so, first write the algorithm you wish to visualize using Devilizer's standard. Here is an example using our [bubble sort algorithm](https://github.com/DemonicallyMC/Devilizer/blob/main/devilizer/sorting/bubble_sort.py):

```py
def bubble_sort(in_lst: list[int]) -> list[list[int], list[int]]:
    """Bubble Sort Algorithm
    Args:
        in (list[int]): List to sort.
    Yields:
        list[
            list[int]: Current values of list.
            list[int]: Indexes to highlight red in visualization.
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
            yield [out_lst, [i+1]]
```

As you can see, an algorithm should take in a list, copy it as to not directly modify the original values, execute one step, and yield the result of that step and the indexes of that list which should be highlighted in the visualization.

When you have your algorithm, you can now visualize it with Devilizer's visualization method:

```py
import random

from devilizer.visualizer.visualize import visualize


def bubble_sort(in_lst: list[int]) -> list[list[int], list[int]]:
    """Bubble Sort Algorithm
    Args:
        in (list[int]): List to sort.
    Yields:
        list[
            list[int]: Current values of list.
            list[int]: Indexes to highlight red in visualization.
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
            yield [out_lst, [i+1]]

lst = random.sample(range(1, 20), 19)
visualize(lst, bubble_sort)
```

## Examples

![example](media/example.gif)
