import click


@click.group(short_help="iauthfunctions CLI.")
def iauthfunctions():
    """iauthfunctions CLI.
    """
    pass


@iauthfunctions.command()
@click.argument("name", default="iauthfunctions")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [iauthfunctions]
