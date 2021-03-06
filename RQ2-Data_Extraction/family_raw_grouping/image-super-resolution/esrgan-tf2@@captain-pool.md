There are `1` versions in total.

# _1.md_
### NOTE
- The image must be a float32 image, converted using `tf.cast(image, tf.float32)`.
- The image must be of 4 dimensions, `[batch_size, height, width, 3]`.
  To perform super resolution on a single image, use `tf.expand_dims(image, 0)` to add
  the batch dimension.
- To display the image, don't forget to convert back to `uint8` using  
`tf.cast(tf.clip_by_value(image[index_of_image_to_display], 0, 255), tf.uint8)`

### Example Use

The SavedModel can be loaded directly
```python3
import tensorflow_hub as hub
import tensorflow as tf
model = hub.load("https://tfhub.dev/captain-pool/esrgan-tf2/1")
# To add an extra dimension for batch, use tf.expand_dims()
low_resolution_image = load_image() # Low Resolution Image of shape [batch_size, height, width, 3]
low_resolution_image = tf.cast(low_resolution_image, tf.float32)
super_resolution = model(low_resolution_image) # Perform Super Resolution here
```

References
--------------
[1] [ESRGAN: Enhanced Super-Resolution Generative Adversarial Networks](https://arxiv.org/abs/1809.00219)