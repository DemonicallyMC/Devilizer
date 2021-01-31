import random
import time

from rich.console import Console
from rich.live import Live
from rich.panel import Panel
from rich.align import Align

from devilizer.sorting.bubble_sort import bubble_sort
from devilizer.visualizer.display_items import display_items


def generate_table(display: str) -> Panel:
    """Generate a panel to display using the rich library.

    Args:
        display (str): The visualized values to display.

    Returns:
        rich.Panel: The generated a panel.
    """
    table = Panel(display, expand=False, title="[bold blue]Devilizer[/bold blue]")
    return Align(table, align="center")


console = Console()
lst = random.sample(list(range(1, 20)), 19)
with Live(auto_refresh=False) as live:
    for step, current in bubble_sort(lst):
        live.update(generate_table(display_items(step, current)))
        time.sleep(0.1)
        live.refresh()
