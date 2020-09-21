There are `1` versions in total.

# _1.md_
## Overview

ResNet19 generator and discriminator.

For the details of the setup, please refer to [1].
The code used to train these models is available on
[GitHub](https://github.com/google/compare_gan).
View all available compare_gan modules in the [Colab notebook](https://colab.research.google.com/github/google/compare_gan/blob/v2/compare_gan/src/tfhub_models.ipynb).

#### Details

* Dataset: CelebA HQ
* Model: Non-saturating GAN
* Architecture: ResNet19
* Optimizer: Adam (lr=1.000e-04, beta1=0.500, beta2=0.900)
* Discriminator iterations per generator iteration: 5
* Discriminator normalizaton: Layer normalization
* Discriminator regularization: DRAGAN Gradient Penalty (lambda=1.000)

#### Scores

* FID: 29.13
* Inception: 2.34
* MS-SSIM: 0.30

#### Example use
```python
# Declare the module
gan = hub.Module("https://tfhub.dev/google/compare_gan/model_9_celebahq128_resnet19/1")

# Use the generator signature
z_values = tf.random_uniform(minval=-1, maxval=1, shape=[64, 128])
images = gan(z_values, signature="generator")

# Use the discriminator signature
logits = gan(images, signature="discriminator")

# Drive execution with tf.Session
session.run([images, logits])
```

## References

[1] Karol Kurach*, Mario Lucic*, Xiaohua Zhai, Marcin Michalski, Sylvain Gelly.
[The GAN Landscape: Losses, Architectures, Regularization, and Normalization](https://arxiv.org/abs/1807.04720).