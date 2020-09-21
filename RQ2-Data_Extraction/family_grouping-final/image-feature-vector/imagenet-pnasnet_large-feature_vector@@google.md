There are `4` versions in total.

# _4.md_
## TF2 SavedModel

This is a [SavedModel in TensorFlow 2
format](https://www.tensorflow.org/hub/tf2_saved_model).
Using it requires TensorFlow 2 (or 1.15) and TensorFlow Hub 0.5.0 or newer.

## Overview

PNASNet-5 is a family of convolutional neural networks for image classification.
The architecture of its convolutional cells (or layers) has been found by
Progressive Neural Architecture Search. PNASNet reuses several techniques from
is precursor NASNet, including regularization by path dropout.
PNASNet and NASNet were originally published by

  * Chenxi Liu, Barret Zoph, Jonathon Shlens, Wei Hua, Li-Jia Li, Li Fei-Fei,
    Alan Yuille, Jonathan Huang, Kevin Murphy: ["Progressive Neural
    Architecture Search"](https://arxiv.org/abs/1712.00559), 2017.
  * Barret Zoph, Vijay Vasudevan, Jonathon Shlens, Quoc V. Le:
    ["Learning Transferable Architectures for Scalable Image
    Recognition"](https://arxiv.org/abs/1707.07012), 2017.

PNASNets come in various sizes. This TF Hub model uses the TF-Slim
implementation `pnasnet_large` of PNASNet-5 for ImageNet
that uses 12 cells (plus 2 for the "ImageNet stem"),
starting with 216 convolutional filters (after the stem).
It has an input size of 331x331 pixels.

The model contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use
[`google/imagenet/pnasnet_large/classification/4`](https://tfhub.dev/google/imagenet/pnasnet_large/classification/4)
instead.


## Training

The checkpoint exported into this model was `pnasnet-5_large_2017_12_13/model.ckpt` downloaded
from
[TF-Slim's pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/README.md#pre-trained-models).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("ImageNet").

## Usage

This model can be used with the `hub.KerasLayer` as follows.
It *cannot* be used with the `hub.Module` API for TensorFlow 1.

```python
m = tf.keras.Sequential([
    hub.KerasLayer("https://tfhub.dev/google/imagenet/pnasnet_large/feature_vector/4",
                   trainable=False),  # Can be True, see below.
    tf.keras.layers.Dense(num_classes, activation='softmax')
])
m.build([None, 331, 331, 3])  # Batch input shape.
```

The output is a batch of feature vectors. For each input image,
the feature vector has size `num_features` = 4320. The feature
vectors can then be used further, e.g., for classification as above.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this model, the size of the input images is fixed to
`height` x `width` = 331 x 331 pixels.


## Fine-tuning

Consumers of this model can [fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.
by passing `trainable=True` to `hub.KerasLayer`.

The dropout probability in NASNet path dropout is not scaled with
the training steps of fine-tuning and remains at the final (maximal) value
from the initial training.

The momentum (a.k.a. decay coefficient) of batch norm's exponential moving
averages defaults to 0.99 for this model, in order to accelerate training
on small datasets (or with huge batch sizes).
Advanced users can set another value (say, 0.997) by loading this model like

```python
hub.KerasLayer("https://tfhub.dev/google/imagenet/pnasnet_large/feature_vector/4",
               trainable=True, arguments=dict(batch_norm_momentum=0.997))
```


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed broken UPDATE_OPS for fine-tuning,
    [GitHub issue 86](https://github.com/tensorflow/hub/issues/86).

#### Version 3

  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.

#### Version 4

  * Switched to the SavedModel format of TensorFlow 2.
    The `hub.Module` class cannot load this or later versions any more.

# _3.md_
## hub.Module for TF1

This is a hub.Module for use with TensorFlow 1.

## Overview

PNASNet-5 is a family of convolutional neural networks for image classification.
The architecture of its convolutional cells (or layers) has been found by
Progressive Neural Architecture Search. PNASNet reuses several techniques from
is precursor NASNet, including regularization by path dropout.
PNASNet and NASNet were originally published by

  * Chenxi Liu, Barret Zoph, Jonathon Shlens, Wei Hua, Li-Jia Li, Li Fei-Fei,
    Alan Yuille, Jonathan Huang, Kevin Murphy: ["Progressive Neural
    Architecture Search"](https://arxiv.org/abs/1712.00559), 2017.
  * Barret Zoph, Vijay Vasudevan, Jonathon Shlens, Quoc V. Le:
    ["Learning Transferable Architectures for Scalable Image
    Recognition"](https://arxiv.org/abs/1707.07012), 2017.

PNASNets come in various sizes. This TF-Hub module uses the TF-Slim
implementation `pnasnet_large` of PNASNet-5 for ImageNet
that uses 12 cells (plus 2 for the "ImageNet stem"),
starting with 216 convolutional filters (after the stem).
It has an input size of 331x331 pixels.

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/pnasnet_large/classification/3`](https://tfhub.dev/google/imagenet/pnasnet_large/classification/3)
instead.


## Training

The checkpoint exported into this module was `pnasnet-5_large_2017_12_13/model.ckpt` downloaded
from
[TF-Slim's pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/README.md#pre-trained-models).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("ImageNet").

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used with the `hub.Module` API like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/pnasnet_large/feature_vector/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
features = module(images)  # Features with shape [batch_size, num_features].
```

...or using the signature name `image_feature_vector`.
For use with TF2 APIs, see TF Hub's [migration
guide](https://github.com/tensorflow/hub/blob/master/docs/migration_tf2.md).

The output for each image
in the batch is a feature vector of size `num_features` = 4320.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 331 x 331 pixels.


## Fine-tuning

Consumers of this module can [fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.

Fine-tuning requires to import the graph version with tag set `{"train"}`
in order to operate batch normalization and dropout in training mode,
and setting `trainable=True`.

The dropout probability in NASNet path dropout is not scaled with
the training steps of fine-tuning and remains at the final (maximal) value
from the initial training.

The momentum (a.k.a. decay coefficient) of batch norm's exponential moving
averages defaults to 0.99 for this module, in order to accelerate training
on small datasets (or with huge batch sizes).
Advanced users can set another value (say, 0.997) by calling this module like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/pnasnet_large/feature_vector/3",
                    trainable=True, tags={"train"})
features = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                  signature="image_feature_vector_with_bn_hparams")
```


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed broken UPDATE_OPS for fine-tuning,
    [GitHub issue 86](https://github.com/tensorflow/hub/issues/86).

#### Version 3

  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.

# _2.md_
## Overview

PNASNet-5 is a family of convolutional neural networks for image classification.
The architecture of its convolutional cells (or layers) has been found by
Progressive Neural Architecture Search. PNASNet reuses several techniques from
is precursor NASNet, including regularization by path dropout.
PNASNet and NASNet were originally published by

  * Chenxi Liu, Barret Zoph, Jonathon Shlens, Wei Hua, Li-Jia Li, Li Fei-Fei,
    Alan Yuille, Jonathan Huang, Kevin Murphy: ["Progressive Neural
    Architecture Search"](https://arxiv.org/abs/1712.00559), 2017.
  * Barret Zoph, Vijay Vasudevan, Jonathon Shlens, Quoc V. Le:
    ["Learning Transferable Architectures for Scalable Image
    Recognition"](https://arxiv.org/abs/1707.07012), 2017.

PNASNets come in various sizes. This TF-Hub module uses the TF-Slim
implementation `pnasnet_large` of PNASNet-5 for ImageNet
that uses 12 cells (plus 2 for the "ImageNet stem"),
starting with 216 convolutional filters (after the stem).
It has an input size of 331x331 pixels.

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/pnasnet_large/classification/2`](https://tfhub.dev/google/imagenet/pnasnet_large/classification/2)
instead.


## Training

The checkpoint exported into this module was `pnasnet-5_large_2017_12_13/model.ckpt` downloaded
from
[TF-Slim's pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/README.md#pre-trained-models).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("ImageNet").

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/pnasnet_large/feature_vector/2")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
features = module(images)  # Features with shape [batch_size, num_features].
```

...or using the signature name `image_feature_vector`. The output for each image
in the batch is a feature vector of size `num_features` = 4320.

For this module, the size of the input image is fixed to
`height` x `width` = 331 x 331 pixels.
The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.


## Fine-tuning

Consumers of this module can [fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.

Fine-tuning requires to import the graph version with tag set `{"train"}`
in order to operate batch normalization and dropout in training mode.
The dropout probability in NASNet path dropout is not scaled with
the training steps of fine-tuning and remains at the final (maximal) value
from the initial training.


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed broken UPDATE_OPS for fine-tuning,
    [GitHub issue 86](https://github.com/tensorflow/hub/issues/86).

# _1.md_
## Overview

PNASNet-5 is a family of convolutional neural networks for image classification.
The architecture of its convolutional cells (or layers) has been found by
Progressive Neural Architecture Search. PNASNet reuses several techniques from
is precursor NASNet, including regularization by path dropout.
PNASNet and NASNet were originally published by

  * Chenxi Liu, Barret Zoph, Jonathon Shlens, Wei Hua, Li-Jia Li, Li Fei-Fei,
    Alan Yuille, Jonathan Huang, Kevin Murphy: ["Progressive Neural
    Architecture Search"](https://arxiv.org/abs/1712.00559), 2017.
  * Barret Zoph, Vijay Vasudevan, Jonathon Shlens, Quoc V. Le:
    ["Learning Transferable Architectures for Scalable Image
    Recognition"](https://arxiv.org/abs/1707.07012), 2017.

PNASNets come in various sizes. This TF-Hub module uses the TF-Slim
implementation `pnasnet_large` of PNASNet-5 for ImageNet
that uses 12 cells (plus 2 for the "ImageNet stem"),
starting with 216 convolutional filters (after the stem).
It has an input size of 331x331 pixels.

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/pnasnet_large/classification/1`](https://tfhub.dev/google/imagenet/pnasnet_large/classification/1)
instead.


## Training

The checkpoint exported into this module was `pnasnet-5_large_2017_12_13/model.ckpt` downloaded
from
[TF-Slim's pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/README.md#pre-trained-models).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("ImageNet").

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/pnasnet_large/feature_vector/1")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
features = module(images)  # Features with shape [batch_size, num_features].
```

...or using the signature name `image_feature_vector`. The output for each image
in the batch is a feature vector of size `num_features` = 4320.

For this module, the size of the input image is fixed to
`height` x `width` = 331 x 331 pixels.
The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.


## Fine-tuning

Consumers of this module can [fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.

Fine-tuning requires to import the graph version with tag set `{"train"}`
in order to operate batch normalization and dropout in training mode.
The dropout probability in NASNet path dropout is not scaled with
the training steps of fine-tuning and remains at the final (maximal) value
from the initial training.