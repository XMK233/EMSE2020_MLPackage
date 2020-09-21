There are `1` versions in total.

# _1.md_
## Overview

ResNet CIFAR generator and discriminator.

For the details of the setup, please refer to [1].
The code used to train these models is available on
[GitHub](https://github.com/google/compare_gan).
View all available compare_gan modules in the [Colab notebook](https://colab.research.google.com/github/google/compare_gan/blob/v2/compare_gan/src/tfhub_models.ipynb).

#### Details

* Dataset: CIFAR-10
* Model: Non-saturating GAN
* Architecture: ResNet CIFAR
* Optimizer: Adam (lr=1.000e-04, beta1=0.500, beta2=0.999)
* Discriminator iterations per generator iteration: 5
* Discriminator normalizaton: none
* Discriminator regularization: none

#### Scores

* FID: 30.08
* Inception: 7.47
* MS-SSIM: N/A

#### Example use
```python
# Declare the module
gan = hub.Module("https://tfhub.dev/google/compare_gan/model_12_cifar10_resnet_cifar/1")

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