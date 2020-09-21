There are `4` versions in total.

# _4.md_
## TF2 SavedModel

This is a SavedModel in TensorFlow 2 format.
Using it requires TensorFlow 2 (or 1.15) and TensorFlow Hub 0.5.0 or newer.

## Overview

Inception V3 is a neural network architecture for image classification,
originally published by

  * Christian Szegedy, Vincent Vanhoucke, Sergey Ioffe, Jonathon Shlens,
    Zbigniew Wojna: ["Rethinking the Inception Architecture for Computer
    Vision"](https://arxiv.org/abs/1512.00567), 2015.

This TF-Hub module uses the TF-Slim implementation of `inception_v3`.
The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/tf2-preview/inception_v3/classification/4`](https://tfhub.dev/google/tf2-preview/inception_v3/classification/4)
instead.


## Training

The checkpoint exported into this module was `inception_v3_2016_08_28/inception_v3.ckpt` downloaded
from
[TF-Slim's pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/README.md#pre-trained-models).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").


## Usage

This module can be used with the `hub.KerasLayer` as follows.
It *cannot* be used with the `hub.Module` API for TensorFlow 1.

```python
m = tf.keras.Sequential([
    hub.KerasLayer("https://tfhub.dev/google/tf2-preview/inception_v3/feature_vector/4", output_shape=[2048],
                   trainable=False),  # Can be True, see below.
    tf.keras.layers.Dense(num_classes, activation='softmax')
])
m.build([None, 299, 299, 3])  # Batch input shape.
```

The output of the module is a batch of feature vectors. For each input image,
the feature vector has size `num_features` = 2048. The feature
vectors can then be used further, e.g., for classification as above.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 299 x 299 pixels.


## Fine-tuning

Consumers of this module can [fine-tune](https://www.tensorflow.org/hub/fine_tuning) it
by passing `trainable=True` to `hub.KerasLayer`.
(Note that this automatically updates the moving averages of
batch normalization.)


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed missing default `trainable=False`.
  * Fixed broken regularization_losses.

#### Version 3

  * Provides proper names for variables, fixing crash in `Model.save()`
    ([GitHub issue #287](https://github.com/tensorflow/hub/issues/287)).

#### Version 4

  * Adds back missing update ops for batch norm that were lost in version 3
    ([GitHub issue #304](https://github.com/tensorflow/hub/issues/304)).

# _3.md_
## TensorFlow 2.0 Preview

This module uses the SavedModel 2.0 format and was created to help
preview TensorFlow 2.0 functionality. Using it requires the (currently
experimental) library versions TensorFlow 2.0 and TensorFlow Hub 0.3.0.

## Overview

Inception V3 is a neural network architecture for image classification,
originally published by

  * Christian Szegedy, Vincent Vanhoucke, Sergey Ioffe, Jonathon Shlens,
    Zbigniew Wojna: ["Rethinking the Inception Architecture for Computer
    Vision"](https://arxiv.org/abs/1512.00567), 2015.

This TF-Hub module uses the TF-Slim implementation of `inception_v3`.
The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/tf2-preview/inception_v3/classification/3`](https://tfhub.dev/google/tf2-preview/inception_v3/classification/3)
instead.


## Training

The checkpoint exported into this module was `inception_v3_2016_08_28/inception_v3.ckpt` downloaded
from
[TF-Slim's pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/README.md#pre-trained-models).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").


## Usage

This module can be used with the `hub.KerasLayer` as follows:

```python
m = tf.keras.Sequential([
    hub.KerasLayer("https://tfhub.dev/google/tf2-preview/inception_v3/feature_vector/3", output_shape=[2048],
                   trainable=False),  # Can be True, see below.
    tf.keras.layers.Dense(num_classes, activation='softmax')
])
m.build([None, 299, 299, 3])  # Batch input shape.
```

The output of the module is a batch of feature vectors. For each input image,
the feature vector has size `num_features` = 2048. The feature
vectors can then be used further, e.g., for classification as above.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 299 x 299 pixels.


## Fine-tuning

Consumers of this module can [fine-tune](https://www.tensorflow.org/hub/fine_tuning) it
by passing `trainable=True` to `hub.KerasLayer`.
(Note that this automatically updates the moving averages of
batch normalization.)


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed missing default `trainable=False`.
  * Fixed broken regularization_losses.

#### Version 3

  * Provides proper names for variables, fixing crash in `Model.save()`
    ([GitHub issue #287](https://github.com/tensorflow/hub/issues/287)).

# _2.md_
## TensorFlow 2.0 Preview

This module uses the SavedModel 2.0 format and was created to help
preview TensorFlow 2.0 functionality. Using it requires the (currently
experimental) library versions TensorFlow 2.0 and TensorFlow Hub 0.3.0.

## Overview

Inception V3 is a neural network architecture for image classification,
originally published by

  * Christian Szegedy, Vincent Vanhoucke, Sergey Ioffe, Jonathon Shlens,
    Zbigniew Wojna: ["Rethinking the Inception Architecture for Computer
    Vision"](https://arxiv.org/abs/1512.00567), 2015.

This TF-Hub module uses the TF-Slim implementation of `inception_v3`.
The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/tf2-preview/inception_v3/classification/2`](https://tfhub.dev/google/tf2-preview/inception_v3/classification/2)
instead.


## Training

The checkpoint exported into this module was `inception_v3_2016_08_28/inception_v3.ckpt` downloaded
from
[TF-Slim's pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/README.md#pre-trained-models).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").


## Usage

This module can be used with the `hub.KerasLayer` as follows:

```python
m = tf.keras.Sequential([
    hub.KerasLayer("https://tfhub.dev/google/tf2-preview/inception_v3/feature_vector/2", output_shape=[2048],
                   trainable=False),  # Can be True, see below.
    tf.keras.layers.Dense(num_classes, activation='softmax')
])
m.build([None, 299, 299, 3])  # Batch input shape.
```

The output of the module is a batch of feature vectors. For each input image,
the feature vector has size `num_features` = 2048. The feature
vectors can then be used further, e.g., for classification as above.

For this module, the size of the input image is fixed to
`height` x `width` = 299 x 299 pixels.
The input `images` are expected to have 3 RGB color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions (analogously to TF 1.x).


## Fine-tuning

Consumers of this module can [fine-tune](https://www.tensorflow.org/hub/fine_tuning) it
by passing `trainable=True` to `hub.KerasLayer`.
(Note that this automatically updates the moving averages of
batch normalization.)

# _1.md_
## TensorFlow 2.0 Preview

This module uses the SavedModel 2.0 format and was created to help
preview TensorFlow 2.0 functionality. Using it requires the (currently
experimental) library versions TensorFlow 2.0 and TensorFlow Hub 0.3.0.

## Overview

Inception V3 is a neural network architecture for image classification,
originally published by

  * Christian Szegedy, Vincent Vanhoucke, Sergey Ioffe, Jonathon Shlens,
    Zbigniew Wojna: ["Rethinking the Inception Architecture for Computer
    Vision"](https://arxiv.org/abs/1512.00567), 2015.

This TF-Hub module uses the TF-Slim implementation of `inception_v3`.
The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/tf2-preview/inception_v3/classification/1`](https://tfhub.dev/google/tf2-preview/inception_v3/classification/1)
instead.


## Training

The checkpoint exported into this module was `inception_v3_2016_08_28/inception_v3.ckpt` downloaded
from
[TF-Slim's pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/README.md#pre-trained-models).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").


## Usage

This module can be used with the `hub.KerasLayer` as follows:

```python
m = tf.keras.Sequential([
    hub.KerasLayer("https://tfhub.dev/google/tf2-preview/inception_v3/feature_vector/1", output_shape=[2048],
                   trainable=False),  # Can be True, see below.
    tf.keras.layers.Dense(num_classes, activation='softmax')
])
m.build([None, 299, 299, 3])  # Batch input shape.
```

The output of the module is a batch of feature vectors. For each input image,
the feature vector has size `num_features` = 2048. The feature
vectors can then be used further, e.g., for classification as above.

For this module, the size of the input image is fixed to
`height` x `width` = 299 x 299 pixels.
The input `images` are expected to have 3 RGB color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions (analogously to TF 1.x).


## Fine-tuning

Consumers of this module can [fine-tune](https://www.tensorflow.org/hub/fine_tuning) it
by passing `trainable=True` to `hub.KerasLayer`.
(Note that this automatically updates the moving averages of
batch normalization.)