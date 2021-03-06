There are `2` versions in total.

# _2.md_
## TF2 SavedModel

This is a [SavedModel in TensorFlow 2
format](https://www.tensorflow.org/hub/tf2_saved_model).
Using it requires TensorFlow 2 (or 1.15) and TensorFlow Hub 0.5.0 or newer.

## Overview

Text embedding based on feed-forward Neural-Net Language Models[1] with
pre-built OOV. Maps from text to 128-dimensional embedding vectors.

#### Example use
The saved model can be loaded directly:

```
import tensorflow_hub as hub

embed = hub.load("https://tfhub.dev/google/nnlm-es-dim128-with-normalization/2")
embeddings = embed(["gato", "gato y perro"])
```

It can also be used within Keras:

```
hub_layer = hub.KerasLayer("https://tfhub.dev/google/nnlm-es-dim128-with-normalization/2",
                           input_shape=[], dtype=tf.string)

model = keras.Sequential()
model.add(hub_layer)
model.add(keras.layers.Dense(16, activation='relu'))
model.add(keras.layers.Dense(1, activation='sigmoid'))

model.summary()
```

## Details
Based on NNLM with three hidden layers.

#### Input
The module takes **a batch of sentences in a 1-D tensor of strings** as input.

#### Preprocessing
The module preprocesses its input by **removing punctuation and splitting on spaces**.

#### Out of vocabulary tokens
Small fraction of the least frequent tokens and embeddings (~2.5%) are
**replaced by hash buckets**. Each hash bucket is initialized using the remaining
embedding vectors that hash to the same bucket.

#### Sentence embeddings
Word embeddings are combined into sentence embedding using the `sqrtn` combiner
(see [tf.nn.embedding_lookup_sparse](https://www.tensorflow.org/versions/master/api_docs/python/tf/nn/embedding_lookup_sparse)).

#### References
[1] Yoshua Bengio, Réjean Ducharme, Pascal Vincent, Christian Jauvin.
[A Neural Probabilistic Language Model](http://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf).
Journal of Machine Learning Research, 3:1137-1155, 2003.

# _1.md_
## hub.Module for TF1

This is a hub.Module for use with TensorFlow 1.

## Overview

Text embedding based on feed-forward Neural-Net Language Models[1] with
pre-built OOV. Maps from text to 128-dimensional embedding vectors.

#### Example use
```
embed = hub.Module("https://tfhub.dev/google/nnlm-es-dim128-with-normalization/1")
embeddings = embed(["gato", "gato y perro"])
```

## Details
Based on NNLM with three hidden layers.

#### Input
The module takes **a batch of sentences in a 1-D tensor of strings** as input.

#### Preprocessing
The module preprocesses its input by **removing punctuation and splitting on spaces**.

#### Out of vocabulary tokens
Small fraction of the least frequent tokens and embeddings (~2.5%) are
**replaced by hash buckets**. Each hash bucket is initialized using the remaining
embedding vectors that hash to the same bucket.

#### Sentence embeddings
Word embeddings are combined into sentence embedding using the `sqrtn` combiner
(see [tf.nn.embedding_lookup_sparse](https://www.tensorflow.org/versions/master/api_docs/python/tf/nn/embedding_lookup_sparse)).

#### References
[1] Yoshua Bengio, Réjean Ducharme, Pascal Vincent, Christian Jauvin.
[A Neural Probabilistic Language Model](http://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf).
Journal of Machine Learning Research, 3:1137-1155, 2003.