There are `1` versions in total.

# _1.md_
## Overview
ResNet50-v2 representation obtained by supervised training on ImageNet.

#### Usage

```python
module = hub.Module("https://tfhub.dev/vtab/sup-100/1")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
features = module(images)  # Features with shape [batch_size, num_features].
```

The input `images` are expected to have color values in the range [0,1], following
the [common image input](https://www.tensorflow.org/hub/common_signatures/images#input) conventions.
This module is suitable to be fine tuned.