There are `1` versions in total.

# _1.md_
## Overview

EfficientNets are a family of image classification models, which achieve
state-of-the-art accuracy, yet being an order-of-magnitude smaller and faster
than previous models.

*   Mingxing Tan and Quoc V. Le:
    [EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks](https://arxiv.org/abs/1905.11946),
    ICML 2019.

We develop EfficientNets based on AutoML and Compound Scaling. In particular, we
first use
[AutoML MNAS Mobile framework](https://ai.googleblog.com/2018/08/mnasnet-towards-automating-design-of.html)
to develop a mobile-size baseline network, named as `EfficientNet-B3`; Then, we
use the compound scaling method to scale up this baseline to obtain
`EfficientNet-B1` to `EfficientNet-B7`.

This TF-Hub module uses the TF-estimator based implementation of
`EfficientNet-B3`. The default signature is used to get
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[https://tfhub.dev/google/efficientnet/b3/classification/1](https://tfhub.dev/google/efficientnet/b3/classification/1)
instead.

## Training

The weights for this module were obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet") with
[AutoAugment](https://arxiv.org/abs/1805.09501) preprocessing.

Please check out the
[official EfficientNet repository](https://github.com/tensorflow/tpu/tree/master/models/official/efficientnet)
for model training.

## Usage

This module implements the common signature for
[image feature-vector](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/efficientnet/b3/feature-vector/1")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
features = module(images)  # Features with shape [batch_size, num_features].
```

...or using the signature name `image_feature-vector`.

For this module, the size of the input image is flexible, but it would be best
to match the model training input. For `EffientNet-B3`, `height` x `width` = 300
x 300 pixels. The input `images` are expected to have color values in the range
[0,1], following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.

## Fine-tuning

In principle, consumers of this module can
[fine-tune](https://www.tensorflow.org/hub/fine_tuning) it. However, fine-tuning
through a large classification might be prone to overfit.

Fine-tuning requires importing the graph version with tag set `{"train"}` in
order to operate batch normalization in training mode.

## EfficientNet collection
See the collection of all EfficientNet models:
https://tfhub.dev/google/collections/efficientnet/1