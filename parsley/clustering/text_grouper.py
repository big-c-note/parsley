import logging
import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering
import tensorflow_hub as hub

log = logging.getLogger("parsley.clustering.runner")


class TextGrouper:
    """Group text based on semantic in an unsupervised way.

    Attributes
    ----------
    model_type : str
        Value of 'Google' or 'Facebook', to choose which pretrained model to
        use.
    data_path : str
        Where to load the data from.
    text_column : str
        The column that contains the text to cluster.
    save_path : str
        Where to save the output.
    """
    def __init__(
        self,
        model_type: str,
        data_path: str,
        text_column: str,
        save_path: str
    ):
        self._model_type = model_type
        self._text_column = text_column
        self._save_path = save_path
        self._data = self._load_data(data_path)
        self._sentences = self._get_sentences()

    def cluster(self, n_clusters: int, distance_threshold: float):
        """Cluster the data based on sentence embeddings and agglomeritive
        clustering.

        Parameters
        ----------
        n_clusters : int
            The number of clusters to use for agglomeritive clustering. If not
            None, then distance_interval must be None.
        distance_threshold : float
            The max distance for neighbors to be grouped into the same cluster. If
            not None, then n_clusters must be None.
        """
        log.info("Clustering the data.")
        embs = self._embed()
        clustering = AgglomerativeClustering(
            n_clusters=n_clusters,
            distance_threshold=distance_threshold
        ).fit(embs)
        self._clusters = clustering.labels_
        self._prep_data()
        self._explore()
        self._dump_data()

    def _load_data(self, data_path: str) -> pd.DataFrame:
        """Load data. Assumes the data has already been cleaned.

        Parameters
        ----------
        data_path : str
            Path to the data.

        Returns
        -------
            The data in a pd.DataFrame.
        """
        log.info(f"Getting data from {data_path}.")
        ds = pd.read_csv(data_path)
        return ds

    def _get_sentences(self) -> pd.Series:
        """Get the sentences.

        Returns
        -------
            Series of text.
        """
        col = self._text_column
        return self._data.dropna(subset=[col])[col]

    def _embed(self) -> np.ndarray:
        """Load model and embed sentences.

        Parameters
        ----------
        sentences : pd.Series
            Series of text to cluster.

        Returns
        -------
        embeddings : np.ndarray
            Array of vectorized embeddings of text.
        """
        if self._model_type == 'Google':
            embed_text = hub.load(
                "https://tfhub.dev/google/universal-sentence-encoder/4"
            )
        else:
            raise NotImplementedError
        embs: np.ndarray = embed_text(self._sentences)
        return embs

    def _explore(self):
        """Explore the data."""
        import ipdb;
        ipdb.set_trace()

    def _prep_data(self):
        """Preapare the data for analysis."""
        self._data['Cluster'] = self._clusters
        self._data.sort_values(by='Cluster')

    def _dump_data(self):
        """Dump the new data."""
        log.info(f"Dumping the data to {self._save_path}.")
        self._data.to_csv(self._save_path)
