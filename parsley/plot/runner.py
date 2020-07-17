"""Usage: parsley plot [OPTIONS]

  Make a basic plot of the data.

Options:
  --data_path TEXT  Path to the data.
  --head BOOLEAN    Whether or not to show the highest volume data.
  --n INTEGER       Number of labels to show.
  --help            Show this message and exit."""
import logging
import click
import pandas as pd
from matplotlib.pyplot import show

log = logging.getLogger("parsley.plot.runner")


@click.command()
@click.option(
    "--data_path",
    help="Path to the data."
)
@click.option(
    "--head",
    default=True,
    type=bool,
    help="Whether or not to show the highest volume data."
)
@click.option(
    "--n",
    default=15,
    type=int,
    help="Number of labels to show."
)
def plot(data_path: str, head: bool, n: int):
    """Make a basic plot of the data."""
    log.info("Plotting the data.")
    data = pd.read_csv(data_path)
    x = data.groupby('Label')['Volume Total'].mean()\
        .sort_values(ascending=head).tail(n)
    x.plot(kind='barh')
    show()
