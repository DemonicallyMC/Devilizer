import time

from rich.live import Live

from devilizer.visualizer.generate_string import generate_string
from devilizer.visualizer.generate_display import generate_display


def visualize(lst: list[int], algorithm: callable) -> None:
    """Visualize a sorting algorithm.

    Args:
        lst (list[int]): List of numbers to sort.
        algorithm (callable): Sorting algorithm to visualize.
    """
    with Live(auto_refresh=False) as live:
        for step, current in algorithm(lst):
            live.update(generate_display(generate_string(step, current)))
            time.sleep(0.1)
            live.refresh()
