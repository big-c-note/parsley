import click

from parsley.clustering.runner import cluster
from parsley.clean.runner import clean_data
from parsley.plot.runner import plot


@click.group()
def cli():
    """The CLI for the parsley package that groups the various scripts.
    """
    pass


cli.add_command(cluster, name="cluster")
cli.add_command(clean_data, name="clean")
cli.add_command(plot, name="plot")
