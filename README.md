# Parsley

Parsley is a unsupervised semantic classifier. Why group a bunch of questions by hand when a computer can?

## Current Research and Roadmap

Currently I've implemented a simple unsupervised clustering method based off already trained word embedding models from Facebook and Google.

## Cluster Your Own text

Start off by cleaning the data. This currently only supports Ahrefs keyword data.

test
```bash
parsley clean --help
```
Then cluster the text. You can choose which model you want to use.
```bash
parsley cluster --help
```
Finally, you can create a simple plot.
```bash
parsley plot --help
```

### Sentence (or Keyword) Embeddings
 
- [Facebook InferSent](https://github.com/facebookresearch/InferSent)
	- [The Paper](https://arxiv.org/abs/1705.02364)
	- Creative Commons Non Commercial.  
- [Google Sentence Encoder](https://tfhub.dev/google/universal-sentence-encoder/1)
	- [The Paper](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/46808.pdf)
	- Apache 2.0 (Mostly free to use)

### Agglomeritiver Clustering

- [Sklearn Implementation](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html)
- [Helpful Video on Undersstanding](https://www.youtube.com/watch?v=XJ3194AmH40)


## Helpful Links

- [this article](https://towardsdatascience.com/semantic-similarity-classifier-and-clustering-sentences-based-on-semantic-similarity-a5a564e22304)
	- [this seasoned author and researcher](https://www.linkedin.com/in/manishchablani/)
- [Helpfull Article](https://medium.com/@adriensieg/text-similarities-da019229c894)
	- Not a well-known author
