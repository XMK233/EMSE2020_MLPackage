There are `1` versions in total.

# _1.md_
## Overview
Encoder obtained by training a Wasserstein Autoencoder using the RAM-MC method
of [1] as a distribution matching penalty that upper bounds the KL divergence
(UKL stands for Upper-bound KL).

#### Usage

```python
module = hub.Module("https://tfhub.dev/vtab/wae-ukl/1")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
features = module(images)  # Features with shape [batch_size, num_features].
```

The input `images` are expected to have color values in the range [0,1], following
the [common image input](https://www.tensorflow.org/hub/common_signatures/images#input) conventions.
This module is suitable to be fine tuned.

#### References
[1] Paul K Rubenstein, Olivier Bousquet, Josip Djolonga, Carlos Riquelme, and Ilya Tolstikhin.
[Practical and Consistent Estimation of f-divergences](https://arxiv.org/abs/1905.11112).
In Advances in Neural Information Processing Systems, 2019.