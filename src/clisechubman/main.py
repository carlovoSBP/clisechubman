import typer

from .clisechubman import hello

app = typer.Typer(invoke_without_command=True)


@app.callback()
def callback(
    ctx: typer.Context, username: str = typer.Option("you", help="Your username")
) -> None:
    """
    A CLI to help manage findings from AWS Security Hub
    """
    if ctx.invoked_subcommand is None:
        typer.echo(hello(username))
