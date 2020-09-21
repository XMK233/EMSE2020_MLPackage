There are `3` versions in total.

# _3.md_
### Model Details

*   Developed by researchers at Google, 2019, v2 [1].
*   Transformer.
*   Covers 16 languages, strong performance on cross-lingual question answer
    retrieval.
*   Use the __question_encoder__ signature to encode variable length questions
    in any of the aforementioned languages and the output is a 512 dimensional
    vector. The default signature is identical with the question_encoder
    signature.
*   Use the __response_encoder__ signture to encode the answer and the output is
    a 512 dimensional vector.
*   The __response_encoder__ signature acceptes two input fields:
    *   __text__: the answer text.
    *   __context__: usually the text around the answer text, for example it
        could be 2 sentneces before plus 2 sentences after, it could also be the
        paragraph conaining the answer text. If you don't have context to
        include, you can duplicate of answer into this field.
*   *All input text can have arbitrary length!* However, model time and space
    complexity is $$O(n^2)$$ for question and response input length $$n$$ and
    $$O(n)$$ for context length. We recommend question and response inputs that
    are approximately one sentence in length.

To learn more about text embeddings, refer to the
[TensorFlow Embeddings](https://www.tensorflow.org/guide/embedding)
documentation.

### Intended Use

*   It is trained on a variety of data sources and tasks, with the goal of
    learning text representations that are useful out-of-the-box to retrieve an
    answer given a question, as well as question and answers across different
    languages.
*   It can also be used in other applications, including any type of text
    classification, clustering, etc.

### Factors

*   The Universal Sentence Encoder Multilingual QA module is an extension of the
    [Universal Sentence Encoder](https://tfhub.dev/google/universal-sentence-encoder/4)
    that is for question answer retrieval and trained on multiple tasks across
    languages.
*   The multi-task training setup is based on the paper "Learning Cross-lingual
    Sentence Representations via a Multi-task Dual Encoder" [2].
*   Important: notice that the language of the text input does not need to be
    specified, as the model was trained such that text across languages with
    similar meanings will have embeddings with high dot product scores.

#### Universal Sentence Encoder family

There are several versions of universal sentence encoder models trained with
different goals including size/performance multilingual, and fine-grained
question answer retrieval.

* [Universal Sentence Encoder family](https://tfhub.dev/google/collections/universal-sentence-encoder/1)

An English version
[universal-sentence-encoder-qa](https://tfhub.dev/google/universal-sentence-encoder-qa/3)
is also available, with stronger performance on English.

### Metrics

*   We apply this model on the
    [SQuAD retrieval task](https://github.com/google/retrieval-qa-eval). See
    performance below:

    SQuAD Retrieval | dev  | train
    :-------------- | :--: | ----:
    Precision@1     | 53.2 | 43.3

#### Prerequisites

This module relies on the [Tensorflow Text](https://github.com/tensorflow/text)
for input preprocessing. On
[Google Colaboratory](https://colab.research.google.com/), the Tensorflow Text
library is available by:

```python
!pip3 install tensorflow_text>=2.0.0rc0
```

#### Example use

```python
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import tensorflow_text

questions = ["What is your age?"]
responses = ["I am 20 years old.", "good morning"]
response_contexts = ["I will be 21 next year.", "great day."]

module = hub.load('https://tfhub.dev/google/universal-sentence-encoder-multilingual-qa/3')

question_embeddings = module.signatures['question_encoder'](
            tf.constant(questions))
response_embeddings = module.signatures['response_encoder'](
        input=tf.constant(responses),
        context=tf.constant(response_contexts))

np.inner(question_embeddings['outputs'], response_embeddings['outputs'])
```

## Changelog

#### Version 1

*   Initial release.

#### Version 2

*   Retrained using TF2.

#### Version 3

*   Fixed GitHub issue #409.
*   Default inference function now returns the Tensor instead of a dictionary.


## References

[1] Yinfei Yang, Daniel Cer, Amin Ahmad, Mandy Guo, Jax Law, Noah Constant,
Gustavo Hernandez Abrego , Steve Yuan, Chris Tar, Yun-hsuan Sung, Ray Kurzweil.
[Multilingual Universal Sentence Encoder for Semantic Retrieval](https://arxiv.org/abs/1907.04307).
July 2019

[2] Muthuraman Chidambaram, Yinfei Yang, Daniel Cer, Steve Yuan, Yun-Hsuan Sung,
Brian Strope, Ray Kurzweil. [Learning Cross-Lingual Sentence Representations via
a Multi-task Dual-Encoder Model](https://arxiv.org/abs/1810.12836).
Repl4NLP@ACL, July 2019.

# _2.md_
### Model Details

*   Developed by researchers at Google, 2019, v2 [1].
*   Transformer.
*   Covers 16 languages, strong performance on cross-lingual question answer
    retrieval.
*   Use the __question_encoder__ signature to encode variable length questions
    in any of the aforementioned languages and the output is a 512 dimensional
    vector. The default signature is identical with the question_encoder
    signature.
*   Use the __response_encoder__ signture to encode the answer and the output is
    a 512 dimensional vector.
*   The __response_encoder__ signature acceptes two input fields:
    *   __text__: the answer text.
    *   __context__: usually the text around the answer text, for example it
        could be 2 sentneces before plus 2 sentences after, it could also be the
        paragraph conaining the answer text. If you don't have context to
        include, you can duplicate of answer into this field.
*   *All input text can have arbitrary length!* However, model time and space
    complexity is $$O(n^2)$$ for question and response input length $$n$$ and
    $$O(n)$$ for context length. We recommend question and response inputs that
    are approximately one sentence in length.

To learn more about text embeddings, refer to the
[TensorFlow Embeddings](https://www.tensorflow.org/guide/embedding)
documentation.

### Intended Use

*   It is trained on a variety of data sources and tasks, with the goal of
    learning text representations that are useful out-of-the-box to retrieve an
    answer given a question, as well as question and answers across different
    languages.
*   It can also be used in other applications, including any type of text
    classification, clustering, etc.

### Factors

*   The Universal Sentence Encoder Multilingual QA module is an extension of the
    [Universal Sentence Encoder](https://tfhub.dev/google/universal-sentence-encoder/2)
    that is for question answer retrieval and trained on multiple tasks across
    languages.
*   The multi-task training setup is based on the paper "Learning Cross-lingual
    Sentence Representations via a Multi-task Dual Encoder" [2].
*   Important: notice that the language of the text input does not need to be
    specified, as the model was trained such that text across languages with
    similar meanings will have embeddings with high dot product scores.

#### Universal Sentence Encoder family

There are several versions of universal sentence encoder models trained with
different goals including size/performance multilingual, and fine-grained
question answer retrieval.

*   [universal-sentence-encoder](https://tfhub.dev/google/universal-sentence-encoder/3)
*   [universal-sentence-encoder-large](https://tfhub.dev/google/universal-sentence-encoder-large/4)
*   [universal-sentence-encoder-qa](https://tfhub.dev/google/universal-sentence-encoder-qa/2)
*   [universal-sentence-encoder-lite](https://tfhub.dev/google/universal-sentence-encoder-lite/2)
*   [universal-sentence-encoder-multilingual](https://tfhub.dev/google/universal-sentence-encoder-multilingual/1)
*   [universal-sentence-encoder-multilingual-large](https://tfhub.dev/google/universal-sentence-encoder-multilingual-large/2)

### Metrics

*   We apply this model on the
    [SQuAD retrieval task](https://github.com/google/retrieval-qa-eval). See
    performance below:

    SQuAD Retrieval | dev  | train
    :-------------- | :--: | ----:
    Precision@1     | 53.2 | 43.3

#### Prerequisites

This module relies on the [Tensorflow Text](https://github.com/tensorflow/text)
for input preprocessing. On
[Google Colaboratory](https://colab.research.google.com/), the Tensorflow Text
library is available by:

```python
!pip3 install tensorflow_text>=2.0.0rc0
```

#### Example use

```python
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import tensorflow_text

questions = ["What is your age?"]
responses = ["I am 20 years old.", "good morning"]
response_contexts = ["I will be 21 next year.", "great day."]

module = hub.load('https://tfhub.dev/google/universal-sentence-encoder-multilingual-qa/2')

question_embeddings = module.signatures['question_encoder'](
            tf.constant(questions))["outputs"]
response_embeddings = module.signatures['response_encoder'](
        input=tf.constant(responses),
        context=tf.constant(response_contexts))["outputs"]

np.inner(question_embeddings, response_embeddings)
```

## Changelog

#### Version 1

*   Initial release.

#### Version 2

*   Retrained using TF2.

## References

[1] Yinfei Yang, Daniel Cer, Amin Ahmad, Mandy Guo, Jax Law, Noah Constant,
Gustavo Hernandez Abrego , Steve Yuan, Chris Tar, Yun-hsuan Sung, Ray Kurzweil.
[Multilingual Universal Sentence Encoder for Semantic Retrieval](https://arxiv.org/abs/1907.04307).
July 2019

[2] Muthuraman Chidambaram, Yinfei Yang, Daniel Cer, Steve Yuan, Yun-Hsuan Sung,
Brian Strope, Ray Kurzweil. [Learning Cross-Lingual Sentence Representations via
a Multi-task Dual-Encoder Model](https://arxiv.org/abs/1810.12836).
Repl4NLP@ACL, July 2019.

# _1.md_
### Model Details

*   Developed by researchers at Google, 2019, v1 [1].
*   Transformer.
*   Covers 16 languages, strong performance on cross-lingual question answer
    retrieval.
*   Use the __question_encoder__ signature to encode variable length questions
    in any of the aforementioned languages and the output is a 512 dimensional
    vector. The default signature is identical with the question_encoder
    signature.
*   Use the __response_encoder__ signture to encode the answer and the output is
    a 512 dimensional vector.
*   The __response_encoder__ signature acceptes two input fields:
    *   __text__: the answer text.
    *   __context__: usually the text around the answer text, for example it
        could be 2 sentneces before plus 2 sentences after, it could also be the
        paragraph conaining the answer text. If you don't have context to
        include, you can duplicate of answer into this field.
*   *All input text can have arbitrary length!* However, model time and space
    complexity is $$O(n^2)$$ for question and response input length $$n$$ and
    $$O(n)$$ for context length. We recommend question and response inputs that
    are approximately one sentence in length.

To learn more about text embeddings, refer to the
[TensorFlow Embeddings](https://www.tensorflow.org/guide/embedding)
documentation.

### Intended Use

*   It is trained on a variety of data sources and tasks, with the goal of
    learning text representations that are useful out-of-the-box to retrieve an
    answer given a question, as well as question and answers across different
    languages.
*   It can also be used in other applications, including any type of text
    classification, clustering, etc.

### Factors

*   The Universal Sentence Encoder Multilingual QA module is an extension of the
    [Universal Sentence Encoder](https://tfhub.dev/google/universal-sentence-encoder/2)
    that is for question answer retrieval and trained on multiple tasks across
    languages.
*   The multi-task training setup is based on the paper "Learning Cross-lingual
    Sentence Representations via a Multi-task Dual Encoder" [2].
*   Important: notice that the language of the text input does not need to be
    specified, as the model was trained such that text across languages with
    similar meanings will have embeddings with high dot product scores.

#### Universal Sentence Encoder family

There are several versions of universal sentence encoder models trained with
different goals including size/performance multilingual, and fine-grained
question answer retrieval.

*   [universal-sentence-encoder](https://tfhub.dev/google/universal-sentence-encoder/2)
*   [universal-sentence-encoder-large](https://tfhub.dev/google/universal-sentence-encoder-large/3)
*   [universal-sentence-encoder-lite](https://tfhub.dev/google/universal-sentence-encoder-lite/2)
*   [universal-sentence-encoder-multilingual](https://tfhub.dev/google/universal-sentence-encoder-multilingual/1)
*   [universal-sentence-encoder-multilingual-large](https://tfhub.dev/google/universal-sentence-encoder-multilingual-large/1)

### Metrics

*   We apply this model on the
    [SQuAD retrieval task](https://github.com/google/retrieval-qa-eval). See
    performance below:

    SQuAD Retrieval | dev  | train
    :-------------- | :--: | ----:
    Precision@1     | 53.2 | 43.3

#### Prerequisites

This module relies on the
[SentencePiece library](https://github.com/google/sentencepiece) for input
preprocessing (please make sure the TensorFlow version you use is compatible
with the SentencePiece library). On
[Google Colaboratory](https://colab.research.google.com/), the SentencePiece
library is available by:

```python
!pip3 install sentencepiece
!pip3 install tf-sentencepiece
```

**NOTE:** The combination of tensorflow 1.14.0 and tf-sentencepiece 0.1.82.1
crashes ([GitHub issue #345](https://github.com/tensorflow/hub/issues/345))
when using this module.

#### Example use

```python
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import tf_sentencepiece

questions = ["What is your age?"]
responses = ["I am 20 years old.", "good morning"]
response_contexts = ["I will be 21 next year.", "great day."]

# Set up graph.
g = tf.Graph()
with g.as_default():
  module = hub.Module("https://tfhub.dev/google/universal-sentence-encoder-multilingual-qa/1")
  question_embeddings = module(
    dict(input=questions),
    signature="question_encoder", as_dict=True)

  response_embeddings = module(
    dict(input=responses,
         context=response_contexts),
    signature="response_encoder", as_dict=True)

  init_op = tf.group([tf.global_variables_initializer(), tf.tables_initializer()])
g.finalize()

# Initialize session.
session = tf.Session(graph=g)
session.run(init_op)

# Compute embeddings.
question_results = session.run(question_embeddings)
response_results = session.run(response_embeddings)

np.inner(question_results["outputs"], response_results["outputs"])
```

## References

[1] Yinfei Yang, Daniel Cer, Amin Ahmad, Mandy Guo, Jax Law, Noah Constant,
Gustavo Hernandez Abrego , Steve Yuan, Chris Tar, Yun-hsuan Sung, Ray Kurzweil.
[Multilingual Universal Sentence Encoder for Semantic Retrieval](https://arxiv.org/abs/1907.04307).
July 2019

[2] Muthuraman Chidambaram, Yinfei Yang, Daniel Cer, Steve Yuan, Yun-Hsuan Sung,
Brian Strope, Ray Kurzweil. [Learning Cross-Lingual Sentence Representations via
a Multi-task Dual-Encoder Model](https://arxiv.org/abs/1810.12836). To appear,
Repl4NLP@ACL, July 2019.