import tensorflow as tf
x1 = tf.constant(6)
y1 = tf.constant(113)

result = tf.multiply(x1,y1)

print(result)

with tf.Session() as sess:
    print(sess.run(result))
