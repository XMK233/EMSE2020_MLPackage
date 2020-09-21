There are `1` versions in total.

# _1.md_
## Overview

SSGAN generator and discriminator.

For the details of the setup, please refer to [1]. The code used to train these
models is available on [GitHub](https://github.com/google/compare_gan).

#### Scores

*   FID: 20.6
*   Inception Score: 24.9

#### Example use

```python
# Load module.
module = hub.Module("https://tfhub.dev/google/compare_gan/ssgan_128x128/1")

batch_size = 8
z_dim = 120

# Sample random noise (z) and ImageNet label (y) inputs.
z = tf.random.normal([batch_size, z_dim])  # noise sample
labels = tf.random.uniform([batch_size], maxval=1000, dtype=tf.int32)
inputs = dict(z=z, labels=labels)

samples = module(inputs)
```

## References

[1] Ting Chen, Xiaohua Zhai, Marvin Ritter, Mario Lucic, Neil Houlsby
[Self-Supervised GANs via Auxiliary Rotation Loss](https://arxiv.org/abs/1811.11212)