"""Usage: parsley cluster [OPTIONS]

  Cluster the text.

Options:
  --model_type TEXT           Value of 'Google' or 'Facebook', to choose which
                              pretrained model to.

  --data_path TEXT            Where to load the data from.
  --text_column TEXT          The column that contains the text to cluster.
  --save_path TEXT            Where to save the output.
  --n_clusters INTEGER        The number of clusters to use for agglomeritive
                              clustering. If not None, then distance_interval
                              must be None.

  --distance_threshold FLOAT  The max distance for neighbors to be grouped
                              into the same cluster. If not None, then
                              n_clusters must be None.

  --help                      Show this message and exit."""
import click

from parsley.clustering.text_grouper import TextGrouper


@click.command()
@click.option(
    "--model_type",
    default='Google',
    help=(
        "Value of 'Google' or 'Facebook', to choose which pretrained model to."
    )
)
@click.option(
    "--data_path",
    help="Where to load the data from."
)
@click.option(
    "--text_column",
    help="The column that contains the text to cluster."
)
@click.option(
    "--save_path",
    help="Where to save the output."
)
@click.option(
    "--n_clusters",
    default=None,
    type=int,
    help=(
        "The number of clusters to use for agglomeritive clustering. If not "
        "None, then distance_interval must be None."
    )
)
@click.option(
    "--distance_threshold",
    default=None,
    type=float,
    help=(
        "The max distance for neighbors to be grouped into the same cluster. "
        "If not None, then n_clusters must be None."
    )
)
def cluster(
    model_type: str,
    data_path: str,
    text_column: str,
    save_path: str,
    n_clusters: int,
    distance_threshold: float
):
    """Cluster the text."""
    text_grouper = TextGrouper(
        model_type=model_type,
        data_path=data_path,
        text_column=text_column,
        save_path=save_path
    )
    text_grouper.cluster(n_clusters, distance_threshold)

if __name__ == "__main__":
    cluster()
