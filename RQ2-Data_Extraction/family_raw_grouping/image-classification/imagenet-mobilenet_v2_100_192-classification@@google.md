There are `4` versions in total.

# _4.md_
## TF2 SavedModel

This is a [SavedModel in TensorFlow 2
format](https://www.tensorflow.org/hub/tf2_saved_model).
Using it requires TensorFlow 2 (or 1.15) and TensorFlow Hub 0.5.0 or newer.

## Overview

MobileNet V2 is a family of neural network architectures for efficient
on-device image classification and related tasks, originally published by

  * Mark Sandler, Andrew Howard, Menglong Zhu, Andrey Zhmoginov,
    Liang-Chieh Chen: ["Inverted Residuals and Linear Bottlenecks:
    Mobile Networks for Classification, Detection and
    Segmentation"](https://arxiv.org/abs/1801.04381), 2018.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.

This TF Hub model uses the TF-Slim implementation of
`mobilenet_v2`
with a depth multiplier of 1.0 and an input size of
192x192 pixels.


The model contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use
[`google/imagenet/mobilenet_v2_100_192/feature_vector/4`](https://tfhub.dev/google/imagenet/mobilenet_v2_100_192/feature_vector/4)
instead, and save the space occupied by the classification layer.


## Training

The checkpoint exported into this model was `mobilenet_v2_1.0_192/mobilenet_v2_1.0_192.ckpt` downloaded
from
[MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This model can be used with the `hub.KerasLayer` as follows.
It *cannot* be used with the `hub.Module` API for TensorFlow 1.

```python
m = tf.keras.Sequential([
    hub.KerasLayer("https://tfhub.dev/google/imagenet/mobilenet_v2_100_192/classification/4")
])
m.build([None, 192, 192, 3])  # Batch input shape.
```

The output is a batch of logits vectors. The indices into the logits
are the `num_classes` = 1001 classes of the classification from
the original training (see above). The mapping from indices to class labels
can be found in the file at [download.tensorflow.org/data/ImageNetLabels.txt](https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt).

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this model, the size of the input images is fixed to
`height` x `width` = 192 x 192 pixels.


## Fine-tuning

In principle, consumers of this model can
[fine-tune](https://www.tensorflow.org/hub/fine_tuning) it
by passing `trainable=True` to `hub.KerasLayer`.

However, fine-tuning through a large classification might be prone to overfit.

The momentum (a.k.a. decay coefficient) of batch norm's exponential moving
averages defaults to 0.99 for this model, in order to accelerate training
on small datasets (or with huge batch sizes).
Advanced users can set another value (say, 0.997) by loading this model like

```python
hub.KerasLayer("https://tfhub.dev/google/imagenet/mobilenet_v2_100_192/classification/4",
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

MobileNet V2 is a family of neural network architectures for efficient
on-device image classification and related tasks, originally published by

  * Mark Sandler, Andrew Howard, Menglong Zhu, Andrey Zhmoginov,
    Liang-Chieh Chen: ["Inverted Residuals and Linear Bottlenecks:
    Mobile Networks for Classification, Detection and
    Segmentation"](https://arxiv.org/abs/1801.04381), 2018.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.

This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v2`
with a depth multiplier of 1.0 and an input size of
192x192 pixels.


The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v2_100_192/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v2_100_192/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Training

The checkpoint exported into this module was `mobilenet_v2_1.0_192/mobilenet_v2_1.0_192.ckpt` downloaded
from
[MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used with the `hub.Module` API like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_100_192/classification/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
logits = module(images)  # Logits with shape [batch_size, num_classes].
```

...or using the signature name `image_classification`.
For use with TF2 APIs, see TF Hub's [migration
guide](https://github.com/tensorflow/hub/blob/master/docs/migration_tf2.md).

The indices into logits
are the `num_classes` = 1001 classes of the classification from
the original training (see above). The mapping from indices to class labels
can be found in the file at [download.tensorflow.org/data/ImageNetLabels.txt](https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt).

This module can also be used to compute [image feature
vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector),
using the signature name `image_feature_vector`.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 192 x 192 pixels.


## Fine-tuning

In principle, consumers of this module can
[fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.
However, fine-tuning through a large classification might be prone to overfit.

Fine-tuning requires importing the graph version with tag set `{"train"}`
in order to operate batch normalization in training mode, and setting
`trainable=True`.

The momentum (a.k.a. decay coefficient) of batch norm's exponential moving
averages defaults to 0.99 for this module, in order to accelerate training
on small datasets (or with huge batch sizes).
Advanced users can set another value (say, 0.997) by calling this module like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_100_192/classification/3",
                    trainable=True, tags={"train"})
logits = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                signature="image_classification_with_bn_hparams")
```

...or analogously for signature `image_feature_vector_with_bn_hparams`.


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

MobileNet V2 is a family of neural network architectures for efficient
on-device image classification and related tasks, originally published by

  * Mark Sandler, Andrew Howard, Menglong Zhu, Andrey Zhmoginov,
    Liang-Chieh Chen: ["Inverted Residuals and Linear Bottlenecks:
    Mobile Networks for Classification, Detection and
    Segmentation"](https://arxiv.org/abs/1801.04381), 2018.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.

This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v2`
with a depth multiplier of 1.0 and an input size of
192x192 pixels.


The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v2_100_192/feature_vector/2`](https://tfhub.dev/google/imagenet/mobilenet_v2_100_192/feature_vector/2)
instead, and save the space occupied by the classification layer.


## Training

The checkpoint exported into this module was `mobilenet_v2_1.0_192/mobilenet_v2_1.0_192.ckpt` downloaded
from
[MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_100_192/classification/2")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
logits = module(images)  # Logits with shape [batch_size, num_classes].
```

...or using the signature name `image_classification`. The indices into logits
are the `num_classes` = 1001 classes of the classification from
the original training (see above). The mapping from indices to class labels
can be found in the file at [download.tensorflow.org/data/ImageNetLabels.txt](https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt).

This module can also be used to compute [image feature
vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector),
using the signature name `image_feature_vector`.

For this module, the size of the input image is fixed to
`height` x `width` = 192 x 192 pixels.
The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.


## Fine-tuning

In principle, consumers of this module can
[fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.
However, fine-tuning through a large classification might be prone to overfit.

Fine-tuning requires importing the graph version with tag set `{"train"}`
in order to operate batch normalization in training mode.


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed broken UPDATE_OPS for fine-tuning,
    [GitHub issue 86](https://github.com/tensorflow/hub/issues/86).

# _1.md_
## Overview

MobileNet V2 is a family of neural network architectures for efficient
on-device image classification and related tasks, originally published by

  * Mark Sandler, Andrew Howard, Menglong Zhu, Andrey Zhmoginov,
    Liang-Chieh Chen: ["Inverted Residuals and Linear Bottlenecks:
    Mobile Networks for Classification, Detection and
    Segmentation"](https://arxiv.org/abs/1801.04381), 2018.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.

This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v2`
with a depth multiplier of 1.0 and an input size of
192x192 pixels.


The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v2_100_192/feature_vector/1`](https://tfhub.dev/google/imagenet/mobilenet_v2_100_192/feature_vector/1)
instead, and save the space occupied by the classification layer.


## Training

The checkpoint exported into this module was `mobilenet_v2_1.0_192/mobilenet_v2_1.0_192.ckpt` downloaded
from
[MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_100_192/classification/1")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
logits = module(images)  # Logits with shape [batch_size, num_classes].
```

...or using the signature name `image_classification`. The indices into logits
are the `num_classes` = 1001 classes of the classification from
the original training (see above).

This module can also be used to compute [image feature
vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector),
using the signature name `image_feature_vector`.

For this module, the size of the input image is fixed to
`height` x `width` = 192 x 192 pixels.
The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.


## Fine-tuning

In principle, consumers of this module can
[fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.
However, fine-tuning through a large classification might be prone to overfit.

Fine-tuning requires importing the graph version with tag set `{"train"}`
in order to operate batch normalization in training mode.