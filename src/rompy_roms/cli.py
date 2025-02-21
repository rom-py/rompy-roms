"""Console script for rompy_roms."""
import rompy_roms

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for rompy_roms."""
    console.print("Replace this message by putting your code into "
               "rompy_roms.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    


if __name__ == "__main__":
    app()
