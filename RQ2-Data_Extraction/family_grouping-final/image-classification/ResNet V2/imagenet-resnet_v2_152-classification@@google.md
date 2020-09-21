There are `3` versions in total.

# _4.md_
## TF2 SavedModel

This is a [SavedModel in TensorFlow 2
format](https://www.tensorflow.org/hub/tf2_saved_model).
Using it requires TensorFlow 2 (or 1.15) and TensorFlow Hub 0.5.0 or newer.

## Overview

ResNet V2 is a family of network architectures for image classification
with a variable number of layers. It builds on the ResNet architecture
originally published by

  * Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun: ["Deep Residual Learning
    for Image Recognition"](https://arxiv.org/abs/1512.03385), 2015.

The full preactivation 'V2' variant of ResNet used in this module was
introduced by

  * Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun: ["Identity Mappings in
    Deep Residual Networks"](https://arxiv.org/abs/1603.05027), 2016.

The key difference compared to ResNet V1 is the use of batch normalization
before every weight layer.

This TF Hub model uses the TF-Slim implementation of `resnet_v2_152`
with 152 layers.
The model contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use
[`google/imagenet/resnet_v2_152/feature_vector/4`](https://tfhub.dev/google/imagenet/resnet_v2_152/feature_vector/4)
instead, and save the space occupied by the classification layer.


## Training

The checkpoint exported into this model was `resnet_v2_152_2017_04_14/resnet_v2_152.ckpt` downloaded
from
[TF-Slim's pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/README.md#pre-trained-models).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").


## Usage

This model can be used with the `hub.KerasLayer` as follows.
It *cannot* be used with the `hub.Module` API for TensorFlow 1.

```python
m = tf.keras.Sequential([
    hub.KerasLayer("https://tfhub.dev/google/imagenet/resnet_v2_152/classification/4")
])
m.build([None, 224, 224, 3])  # Batch input shape.
```

The output is a batch of logits vectors. The indices into the logits
are the `num_classes` = 1001 classes of the classification from
the original training (see above). The mapping from indices to class labels
can be found in the file at [download.tensorflow.org/data/ImageNetLabels.txt](https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt).

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
The expected size of the input images is
`height` x `width` = 224 x 224 pixels
by default, but other input sizes are possible (within limits).


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
hub.KerasLayer("https://tfhub.dev/google/imagenet/resnet_v2_152/classification/4",
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

ResNet V2 is a family of network architectures for image classification
with a variable number of layers. It builds on the ResNet architecture
originally published by

  * Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun: ["Deep Residual Learning
    for Image Recognition"](https://arxiv.org/abs/1512.03385), 2015.

The full preactivation 'V2' variant of ResNet used in this module was
introduced by

  * Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun: ["Identity Mappings in
    Deep Residual Networks"](https://arxiv.org/abs/1603.05027), 2016.

The key difference compared to ResNet V1 is the use of batch normalization
before every weight layer.

This TF-Hub module uses the TF-Slim implementation of `resnet_v2_152`
with 152 layers.
The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/resnet_v2_152/feature_vector/3`](https://tfhub.dev/google/imagenet/resnet_v2_152/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Training

The checkpoint exported into this module was `resnet_v2_152_2017_04_14/resnet_v2_152.ckpt` downloaded
from
[TF-Slim's pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/README.md#pre-trained-models).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").


## Usage

This module implements the common signature for
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used with the `hub.Module` API like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/resnet_v2_152/classification/3")
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
The expected size of the input images is
`height` x `width` = 224 x 224 pixels
by default, but other input sizes are possible (within limits).


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
module = hub.Module("https://tfhub.dev/google/imagenet/resnet_v2_152/classification/3",
                    trainable=True, tags={"train"})
logits = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                signature="image_classification_with_bn_hparams")
```

...or analogously for signature `image_feature_vector_with_bn_hparams`.


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

ResNet V2 is a family of network architectures for image classification
with a variable number of layers. It builds on the ResNet architecture
originally published by

  * Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun: ["Deep Residual Learning
    for Image Recognition"](https://arxiv.org/abs/1512.03385), 2015.

The full preactivation 'V2' variant of ResNet used in this module was
introduced by

  * Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun: ["Identity Mappings in
    Deep Residual Networks"](https://arxiv.org/abs/1603.05027), 2016.

The key difference compared to ResNet V1 is the use of batch normalization
before every weight layer.

This TF-Hub module uses the TF-Slim implementation of `resnet_v2_152`
with 152 layers.
The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/resnet_v2_152/feature_vector/1`](https://tfhub.dev/google/imagenet/resnet_v2_152/feature_vector/1)
instead, and save the space occupied by the classification layer.


## Training

The checkpoint exported into this module was `resnet_v2_152_2017_04_14/resnet_v2_152.ckpt` downloaded
from
[TF-Slim's pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/README.md#pre-trained-models).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").


## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/resnet_v2_152/classification/1")
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
`height` x `width` = 224 x 224 pixels.
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