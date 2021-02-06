from rich.panel import Panel
from rich.align import Align


def generate_display(display: str) -> Panel:
    """Generate a panel to display using the rich library.

    Args:
        display (str): The visualized values to display.

    Returns:
        rich.Panel: The generated panel.
    """
    table = Panel(display, expand=False, title="[bold blue]Devilizer[/bold blue]")
    return Align(table, align="center")