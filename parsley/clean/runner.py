"""Usage: parsley clean [OPTIONS]

  Clean the raw data. Only supporting Ahrefs data right now with  Search
  Volume as the weight.

Options:
  --data_path TEXT      Path to the raw data.
  --save_path TEXT      Path to save the clean data.
  --text_column TEXT    The name of the column that contains the text to
                        cluster.

  --weight_column TEXT  The name of the column that contains the weight.
  --help                Show this message and exit."""
import logging
import pandas as pd
import click

log = logging.getLogger("parsley.clean.runner")


@click.command()
@click.option(
    "--data_path",
    help="Path to the raw data."
)
@click.option(
    "--save_path",
    help="Path to save the clean data."
)
@click.option(
    "--text_column",
    help="The name of the column that contains the text to cluster."
)
@click.option(
    "--weight_column",
    help="The name of the column that contains the weight."
)
def clean_data(
    data_path: str,
    save_path: str,
    text_column: str,
    weight_column: str
):
    """Clean the raw data. Only supporting Ahrefs data right now with  Search
    Volume as the weight."""
    log.info("Cleaning data.")
    cols = [text_column, weight_column]
    ds = pd.read_csv(data_path)
    data = ds[cols].dropna(subset=[text_column]).\
        sort_values(by=[text_column, weight_column], ascending=False).\
        drop_duplicates(keep='first')
    data.to_csv(save_path, index=False)
    log.info("Data clean.")


if __name__ == "__main__":
    clean_data()
