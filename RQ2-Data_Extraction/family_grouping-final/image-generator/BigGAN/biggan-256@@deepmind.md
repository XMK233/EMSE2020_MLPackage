There are `2` versions in total.

# _2.md_
## Overview

This is the 256x256 *BigGAN* image generator described in [1], corresponding to
Row 4 in Table 2 (res. 256).

#### Example use
```python
# Load BigGAN 256 module.
module = hub.Module('https://tfhub.dev/deepmind/biggan-256/2')

# Sample random noise (z) and ImageNet label (y) inputs.
batch_size = 8
truncation = 0.5  # scalar truncation value in [0.02, 1.0]
z = truncation * tf.random.truncated_normal([batch_size, 140])  # noise sample
y_index = tf.random.uniform([batch_size], maxval=1000, dtype=tf.int32)
y = tf.one_hot(y_index, 1000)  # one-hot ImageNet label

# Call BigGAN on a dict of the inputs to generate a batch of images with shape
# [8, 256, 256, 3] and range [-1, 1].
samples = module(dict(y=y, z=z, truncation=truncation))
```

#### Note from the authors

This work was conducted to advance the state of the art in
generative adversarial networks for image generation.
We are releasing the pre-trained generator to allow our work to be
verified, which is standard practice in academia.
It does not include the discriminator to minimize the potential for
exploitation.

## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed race condition causing batch statistics for previous truncation value
    to be used on the first run call for a new truncation value.

## References

[1] Andrew Brock, Jeff Donahue, and Karen Simonyan.
[Large Scale GAN Training for High Fidelity Natural Image Synthesis](https://arxiv.org/abs/1809.11096).
*arxiv:1809.11096*, 2018.

# _1.md_
## Overview

This is the 256x256 *BigGAN* image generator described in [1], corresponding to
Row 4 in Table 2 (res. 256).

#### Example use
```python
# Load BigGAN 256 module.
module = hub.Module('https://tfhub.dev/deepmind/biggan-256/1')

# Sample random noise (z) and ImageNet label (y) inputs.
batch_size = 8
truncation = 0.5  # scalar truncation value in [0.02, 1.0]
z = truncation * tf.random.truncated_normal([batch_size, 140])  # noise sample
y_index = tf.random.uniform([batch_size], maxval=1000, dtype=tf.int32)
y = tf.one_hot(y_index, 1000)  # one-hot ImageNet label

# Call BigGAN on a dict of the inputs to generate a batch of images with shape
# [8, 256, 256, 3] and range [-1, 1].
samples = module(dict(y=y, z=z, truncation=truncation))
```

#### Note from the authors

This work was conducted to advance the state of the art in
generative adversarial networks for image generation.
We are releasing the pre-trained generator to allow our work to be
verified, which is standard practice in academia.
It does not include the discriminator to minimize the potential for
exploitation.

## References

[1] Andrew Brock, Jeff Donahue, and Karen Simonyan.
[Large Scale GAN Training for High Fidelity Natural Image Synthesis](https://arxiv.org/abs/1809.11096).
*arxiv:1809.11096*, 2018.