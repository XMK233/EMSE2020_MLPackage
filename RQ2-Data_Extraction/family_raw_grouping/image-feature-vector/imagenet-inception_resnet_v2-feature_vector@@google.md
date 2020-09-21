There are `3` versions in total.

# _4.md_
## TF2 SavedModel

This is a [SavedModel in TensorFlow 2
format](https://www.tensorflow.org/hub/tf2_saved_model).
Using it requires TensorFlow 2 (or 1.15) and TensorFlow Hub 0.5.0 or newer.

## Overview

Inception ResNet V2 is a neural network architecture for image classification,
originally published by

  * Christian Szegedy, Sergey Ioffe, Vincent Vanhoucke, Alex Alemi:
    ["Inception-v4, Inception-ResNet and the Impact of Residual Connections
    on Learning"](https://arxiv.org/abs/1602.07261), 2016.

This TF Hub model uses the TF-Slim implementation of `inception_resnet_v2`.
The model contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use
[`google/imagenet/inception_resnet_v2/classification/4`](https://tfhub.dev/google/imagenet/inception_resnet_v2/classification/4)
instead.


## Training

The checkpoint exported into this model was `inception_resnet_v2_2016_08_30/inception_resnet_v2_2016_08_30.ckpt` downloaded
from
[TF-Slim's pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/README.md#pre-trained-models).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").


## Usage

This model can be used with the `hub.KerasLayer` as follows.
It *cannot* be used with the `hub.Module` API for TensorFlow 1.

```python
m = tf.keras.Sequential([
    hub.KerasLayer("https://tfhub.dev/google/imagenet/inception_resnet_v2/feature_vector/4",
                   trainable=False),  # Can be True, see below.
    tf.keras.layers.Dense(num_classes, activation='softmax')
])
m.build([None, 299, 299, 3])  # Batch input shape.
```

The output is a batch of feature vectors. For each input image,
the feature vector has size `num_features` = 1536. The feature
vectors can then be used further, e.g., for classification as above.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
The expected size of the input images is
`height` x `width` = 299 x 299 pixels
by default, but other input sizes are possible (within limits).


## Fine-tuning

Consumers of this model can [fine-tune](https://www.tensorflow.org/hub/fine_tuning) it
by passing `trainable=True` to `hub.KerasLayer`.

The momentum (a.k.a. decay coefficient) of batch norm's exponential moving
averages defaults to 0.99 for this model, in order to accelerate training
on small datasets (or with huge batch sizes).
Advanced users can set another value (say, 0.997) by loading this model like

```python
hub.KerasLayer("https://tfhub.dev/google/imagenet/inception_resnet_v2/feature_vector/4",
               trainable=True, arguments=dict(batch_norm_momentum=0.997))
```


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Support for variable input size.
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

Inception ResNet V2 is a neural network architecture for image classification,
originally published by

  * Christian Szegedy, Sergey Ioffe, Vincent Vanhoucke, Alex Alemi:
    ["Inception-v4, Inception-ResNet and the Impact of Residual Connections
    on Learning"](https://arxiv.org/abs/1602.07261), 2016.

This TF-Hub module uses the TF-Slim implementation of `inception_resnet_v2`.
The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/inception_resnet_v2/classification/3`](https://tfhub.dev/google/imagenet/inception_resnet_v2/classification/3)
instead.


## Training

The checkpoint exported into this module was `inception_resnet_v2_2016_08_30/inception_resnet_v2_2016_08_30.ckpt` downloaded
from
[TF-Slim's pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/README.md#pre-trained-models).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").


## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used with the `hub.Module` API like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/inception_resnet_v2/feature_vector/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
features = module(images)  # Features with shape [batch_size, num_features].
```

...or using the signature name `image_feature_vector`.
For use with TF2 APIs, see TF Hub's [migration
guide](https://github.com/tensorflow/hub/blob/master/docs/migration_tf2.md).

The output for each image
in the batch is a feature vector of size `num_features` = 1536.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
The expected size of the input images is
`height` x `width` = 299 x 299 pixels
by default, but other input sizes are possible (within limits).


## Fine-tuning

Consumers of this module can [fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.
This requires importing the graph version with tag set `{"train"}`
in order to operate batch normalization in training mode, and setting
`trainable=True`.

The momentum (a.k.a. decay coefficient) of batch norm's exponential moving
averages defaults to 0.99 for this module, in order to accelerate training
on small datasets (or with huge batch sizes).
Advanced users can set another value (say, 0.997) by calling this module like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/inception_resnet_v2/feature_vector/3",
                    trainable=True, tags={"train"})
features = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                  signature="image_feature_vector_with_bn_hparams")
```


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Support for variable input size.
  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.

# _1.md_
## Overview

Inception ResNet V2 is a neural network architecture for image classification,
originally published by

  * Christian Szegedy, Sergey Ioffe, Vincent Vanhoucke, Alex Alemi:
    ["Inception-v4, Inception-ResNet and the Impact of Residual Connections
    on Learning"](https://arxiv.org/abs/1602.07261), 2016.

This TF-Hub module uses the TF-Slim implementation of `inception_resnet_v2`.
The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/inception_resnet_v2/classification/1`](https://tfhub.dev/google/imagenet/inception_resnet_v2/classification/1)
instead.


## Training

The checkpoint exported into this module was `inception_resnet_v2_2016_08_30/inception_resnet_v2_2016_08_30.ckpt` downloaded
from
[TF-Slim's pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/README.md#pre-trained-models).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").


## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/inception_resnet_v2/feature_vector/1")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
features = module(images)  # Features with shape [batch_size, num_features].
```

...or using the signature name `image_feature_vector`. The output for each image
in the batch is a feature vector of size `num_features` = 1536.

For this module, the size of the input image is fixed to
`height` x `width` = 299 x 299 pixels.
The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.


## Fine-tuning

Consumers of this module can [fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.
This requires importing the graph version with tag set `{"train"}`
in order to operate batch normalization in training mode.