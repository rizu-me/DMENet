import tensorflow as tf
import tensorlayer as tl
import numpy as np
from tensorlayer.layers import *

def UNet_down(image_in, is_train=False, reuse=False, scope = 'unet_down'):
    w_init_relu = tf.contrib.layers.variance_scaling_initializer()
    w_init_sigmoid = tf.contrib.layers.xavier_initializer()
    g_init = tf.random_normal_initializer(1., 0.02)
    lrelu = lambda x: tl.act.lrelu(x, 0.2)
    with tf.variable_scope(scope, reuse=reuse) as vs:
        n = InputLayer(image_in, name='image_in')
        n = PadLayer(n, [[0, 0], [1, 1], [1, 1], [0, 0]], "Symmetric", name='d0/pad1')
        n = Conv2d(n, 64, (3, 3), (1, 1), act=None, padding='VALID', W_init=w_init_relu, name='d0/c1')
        n = InstanceNormLayer(n, act=lrelu, name='d0/b1')
        n = PadLayer(n, [[0, 0], [1, 1], [1, 1], [0, 0]], "Symmetric", name='d0/pad2')
        n = Conv2d(n, 64, (3, 3), (1, 1), act=None, padding='VALID', W_init=w_init_relu, name='d0/c2')
        n = InstanceNormLayer(n, act=lrelu, name='d0/b2')
        d0 = n

        #n = MaxPool2d(n, (2, 2), (2, 2), padding='VALID', name='d1/pool1')
        n = Conv2d(n, 64, (2, 2), (2, 2), act=None, padding='VALID', W_init=w_init_relu, name='d1/pool1')
        n = PadLayer(n, [[0, 0], [1, 1], [1, 1], [0, 0]], "Symmetric", name='d1/pad1')
        n = Conv2d(n, 128, (3, 3), (1, 1), act=None, padding='VALID', W_init=w_init_relu, name='d1/c1')
        n = InstanceNormLayer(n, act=lrelu, name='d1/b1')
        n = PadLayer(n, [[0, 0], [1, 1], [1, 1], [0, 0]], "Symmetric", name='d1/pad2')
        n = Conv2d(n, 128, (3, 3), (1, 1), act=None, padding='VALID', W_init=w_init_relu, name='d1/c2')
        n = InstanceNormLayer(n, act=lrelu, name='d1/b2')
        n = PadLayer(n, [[0, 0], [1, 1], [1, 1], [0, 0]], "Symmetric", name='d1/pad3')
        n = Conv2d(n, 128, (3, 3), (1, 1), act=None, padding='VALID', W_init=w_init_relu, name='d1/c3')
        n = InstanceNormLayer(n, act=lrelu, name='d1/b3')
        d1 = n

        #n = MaxPool2d(n, (2, 2), (2, 2), padding='VALID', name='d2/pool1')
        n = Conv2d(n, 128, (2, 2), (2, 2), act=None, padding='VALID', W_init=w_init_relu, name='d2/pool1')
        n = PadLayer(n, [[0, 0], [1, 1], [1, 1], [0, 0]], "Symmetric", name='d2/pad1')
        n = Conv2d(n, 256, (3, 3), (1, 1), act=None, padding='VALID', W_init=w_init_relu, name='d2/c1')
        n = InstanceNormLayer(n, act=lrelu, name='d2/b1')
        n = PadLayer(n, [[0, 0], [1, 1], [1, 1], [0, 0]], "Symmetric", name='d2/pad2')
        n = Conv2d(n, 256, (3, 3), (1, 1), act=None, padding='VALID', W_init=w_init_relu, name='d2/c2')
        n = InstanceNormLayer(n, act=lrelu, name='d2/b2')
        n = PadLayer(n, [[0, 0], [1, 1], [1, 1], [0, 0]], "Symmetric", name='d2/pad3')
        n = Conv2d(n, 256, (3, 3), (1, 1), act=None, padding='VALID', W_init=w_init_relu, name='d2/c3')
        n = InstanceNormLayer(n, act=lrelu, name='d2/b3')
        d2 = n

        #n = MaxPool2d(n, (2, 2), (2, 2), padding='VALID', name='d3/pool1')
        n = Conv2d(n, 256, (2, 2), (2, 2), act=None, padding='VALID', W_init=w_init_relu, name='d3/pool1')
        n = PadLayer(n, [[0, 0], [1, 1], [1, 1], [0, 0]], "Symmetric", name='d3/pad1')
        n = Conv2d(n, 512, (3, 3), (1, 1), act=None, padding='VALID', W_init=w_init_relu, name='d3/c1')
        n = InstanceNormLayer(n, act=lrelu, name='d3/b1')
        n = PadLayer(n, [[0, 0], [1, 1], [1, 1], [0, 0]], "Symmetric", name='d3/pad2')
        n = Conv2d(n, 512, (3, 3), (1, 1), act=None, padding='VALID', W_init=w_init_relu, name='d3/c2')
        n = InstanceNormLayer(n, act=lrelu, name='d3/b2')
        n = PadLayer(n, [[0, 0], [1, 1], [1, 1], [0, 0]], "Symmetric", name='d3/pad3')
        n = Conv2d(n, 512, (3, 3), (1, 1), act=None, padding='VALID', W_init=w_init_relu, name='d3/c3')
        n = InstanceNormLayer(n, act=lrelu, name='d3/b3')
        d3 = n

        #n = MaxPool2d(n, (2, 2), (2, 2), padding='VALID', name='d4/pool1')
        n = Conv2d(n, 512, (2, 2), (2, 2), act=None, padding='VALID', W_init=w_init_relu, name='d4/pool1')
        n = PadLayer(n, [[0, 0], [1, 1], [1, 1], [0, 0]], "Symmetric", name='d4/pad1')
        n = Conv2d(n, 1024, (3, 3), (1, 1), act=None, padding='VALID', W_init=w_init_relu, name='d4/c1')
        n = InstanceNormLayer(n, act=lrelu, name='d4/b1')
        n = PadLayer(n, [[0, 0], [1, 1], [1, 1], [0, 0]], "Symmetric", name='d4/pad2')
        n = Conv2d(n, 1024, (3, 3), (1, 1), act=None, padding='VALID', W_init=w_init_relu, name='d4/c2')
        n = InstanceNormLayer(n, act=lrelu, name='d4/b2')
        n = PadLayer(n, [[0, 0], [1, 1], [1, 1], [0, 0]], "Symmetric", name='d4/pad3')
        n = Conv2d(n, 1024, (3, 3), (1, 1), act=None, padding='VALID', W_init=w_init_relu, name='d4/c3')
        n = InstanceNormLayer(n, act=lrelu, name='d4/b3')
        d4 = n

        return [d0.outputs, d1.outputs, d2.outputs, d3.outputs, d4.outputs]

def UNet_up(feats, is_train=False, reuse=False, scope = 'unet_up'):
    w_init_relu = tf.contrib.layers.variance_scaling_initializer()
    w_init_sigmoid = tf.contrib.layers.xavier_initializer()
    g_init = tf.random_normal_initializer(1., 0.02)
    lrelu = lambda x: tl.act.lrelu(x, 0.2)
    with tf.variable_scope(scope, reuse=reuse) as vs:
        d0 = InputLayer(feats[0], name='d0')
        d1 = InputLayer(feats[1], name='d1')
        d2 = InputLayer(feats[2], name='d2')
        d3 = InputLayer(feats[3], name='d3')
        d4 = InputLayer(feats[4], name='d4')
        
        n = UpSampling2dLayer(d4, (2, 2), is_scale = True, method = 1, align_corners=False, name='u3/u')
        n = ConcatLayer([n, d3], concat_dim = 3, name='u3/concat')
        n = PadLayer(n, [[0, 0], [1, 1], [1, 1], [0, 0]], "Symmetric", name='u3/pad1')
        n = Conv2d(n, 512, (3, 3), (1, 1), act=None, padding='VALID', W_init=w_init_relu, name='u3/c1')
        n = InstanceNormLayer(n, act=lrelu, name='u3/b1')
        n = PadLayer(n, [[0, 0], [1, 1], [1, 1], [0, 0]], "Symmetric", name='u3/pad2')
        n = Conv2d(n, 512, (3, 3), (1, 1), act=None, padding='VALID', W_init=w_init_relu, name='u3/c2')
        n = InstanceNormLayer(n, act=lrelu, name='u3/b2')
        n = PadLayer(n, [[0, 0], [1, 1], [1, 1], [0, 0]], "Symmetric", name='u3/pad3')
        n = Conv2d(n, 512, (3, 3), (1, 1), act=None, padding='VALID', W_init=w_init_relu, name='u3/c3')
        n = InstanceNormLayer(n, act=lrelu, name='u3/b3')
        u3 = n

        n = UpSampling2dLayer(n, (2, 2), is_scale = True, method = 1, align_corners=False, name='u2/u')
        n = ConcatLayer([n, d2], concat_dim = 3, name='u2/concat')
        n = PadLayer(n, [[0, 0], [1, 1], [1, 1], [0, 0]], "Symmetric", name='u2/pad1')
        n = Conv2d(n, 256, (3, 3), (1, 1), act=None, padding='VALID', W_init=w_init_relu, name='u2/c1')
        n = InstanceNormLayer(n, act=lrelu, name='u2/b1')
        n = PadLayer(n, [[0, 0], [1, 1], [1, 1], [0, 0]], "Symmetric", name='u2/pad3')
        n = Conv2d(n, 256, (3, 3), (1, 1), act=None, padding='VALID', W_init=w_init_relu, name='u2/c2')
        n = InstanceNormLayer(n, act=lrelu, name='u2/b2')
        n = PadLayer(n, [[0, 0], [1, 1], [1, 1], [0, 0]], "Symmetric", name='u2/pad3')
        n = Conv2d(n, 256, (3, 3), (1, 1), act=None, padding='VALID', W_init=w_init_relu, name='u2/c3')
        n = InstanceNormLayer(n, act=lrelu, name='u2/b3')
        u2 = n

        n = UpSampling2dLayer(n, (2, 2), is_scale = True, method = 1, align_corners=False, name='u1/u')
        n = ConcatLayer([n, d1], concat_dim = 3, name='u1/concat')
        n = PadLayer(n, [[0, 0], [1, 1], [1, 1], [0, 0]], "Symmetric", name='u1/pad1')
        n = Conv2d(n, 128, (3, 3), (1, 1), act=None, padding='VALID', W_init=w_init_relu, name='u1/c1')
        n = InstanceNormLayer(n, act=lrelu, name='u1/b1')
        n = PadLayer(n, [[0, 0], [1, 1], [1, 1], [0, 0]], "Symmetric", name='u1/pad2')
        n = Conv2d(n, 128, (3, 3), (1, 1), act=None, padding='VALID', W_init=w_init_relu, name='u1/c2')
        n = InstanceNormLayer(n, act=lrelu, name='u1/b2')
        n = PadLayer(n, [[0, 0], [1, 1], [1, 1], [0, 0]], "Symmetric", name='u1/pad3')
        n = Conv2d(n, 128, (3, 3), (1, 1), act=None, padding='VALID', W_init=w_init_relu, name='u1/c3')
        n = InstanceNormLayer(n, act=lrelu, name='u1/b3')
        u1 = n

        n = UpSampling2dLayer(n, (2, 2), is_scale = True, method = 1, align_corners=False, name='u0/u')
        n = ConcatLayer([n, d0], concat_dim = 3, name='u0/concat')
        n = PadLayer(n, [[0, 0], [1, 1], [1, 1], [0, 0]], "Symmetric", name='u0/pad1')
        n = Conv2d(n, 64, (3, 3), (1, 1), act=None, padding='VALID', W_init=w_init_relu, name='u0/c1')
        n = InstanceNormLayer(n, act=lrelu, name='u0/b1')
        n = PadLayer(n, [[0, 0], [1, 1], [1, 1], [0, 0]], "Symmetric", name='u0/pad_relu')
        n = Conv2d(n, 64, (3, 3), (1, 1), act=None, padding='VALID', W_init=w_init_relu, name='u0/c2')
        n = InstanceNormLayer(n, act=lrelu, name='u0/b2')
        n = PadLayer(n, [[0, 0], [1, 1], [1, 1], [0, 0]], "Symmetric", name='u0/pad3')
        n = Conv2d(n, 64, (3, 3), (1, 1), act=None, padding='VALID', W_init=w_init_relu, name='u0/c3')
        n = InstanceNormLayer(n, act=lrelu, name='u0/b3')
        u0 = n

        n = PadLayer(n, [[0, 0], [1, 1], [1, 1], [0, 0]], "Symmetric", name='uf/pad3')
        n_1c = Conv2d(n, 1, (3, 3), (1, 1), act=None, padding='VALID', W_init=w_init_sigmoid, name='uf/1c')

        return n.outputs, tf.nn.sigmoid(n_1c.outputs), [u0.outputs, u1.outputs, u2.outputs, u3.outputs, d4.outputs]

def feature_discriminator(feats, is_train=True, reuse=False, scope = 'feature_discriminator'):
    w_init = tf.contrib.layers.variance_scaling_initializer()
    w_init_sigmoid = tf.contrib.layers.xavier_initializer()
    b_init = None # tf.constant_initializer(value=0.0)
    gamma_init=tf.random_normal_initializer(1., 0.02)
    
    lrelu = lambda x: tl.act.lrelu(x, 0.2)
    with tf.variable_scope(scope, reuse=reuse):
        d0 = InputLayer(feats[0], name='d0')
        d1 = InputLayer(feats[1], name='d1')
        d2 = InputLayer(feats[2], name='d2')
        d3 = InputLayer(feats[3], name='d3')
        d4 = InputLayer(feats[4], name='d4')
        
        n = Conv2d(d0, 64, (3, 3), (1, 1), act=None, padding='SAME', W_init=w_init, b_init=b_init, name='h0/c1')
        n = InstanceNormLayer(n, act=lrelu, name='h0/bn1')
        n = Conv2d(d0, 64, (3, 3), (1, 1), act=None, padding='SAME', W_init=w_init, b_init=b_init, name='h0/c2')
        n = InstanceNormLayer(n, act=lrelu, name='h0/bn2')
        n = Conv2d(n, 128, (3, 3), (2, 2), act=None, padding='SAME', W_init=w_init, b_init=b_init, name='h0/c3')
        n = InstanceNormLayer(n, act=lrelu, name='h0/bn3')

        n = ElementwiseLayer([n, d1], tf.add, name='add1')
        n = Conv2d(n, 128, (3, 3), (1, 1), act=None, padding='SAME', W_init=w_init, b_init=b_init, name='h1/c1')
        n = InstanceNormLayer(n, act=lrelu, name='h1/bn1')
        n = Conv2d(n, 128, (3, 3), (1, 1), act=None, padding='SAME', W_init=w_init, b_init=b_init, name='h1/c2')
        n = InstanceNormLayer(n, act=lrelu, name='h1/bn2')
        n = Conv2d(n, 256, (3, 3), (2, 2), act=None, padding='SAME', W_init=w_init, b_init=b_init, name='h1/c3')
        n = InstanceNormLayer(n, act=lrelu, name='h1/bn3')

        n = ElementwiseLayer([n, d2], tf.add, name='add2')
        n = Conv2d(n, 256, (3, 3), (1, 1), act=None, padding='SAME', W_init=w_init, b_init=b_init, name='h2/c1')
        n = InstanceNormLayer(n, act=lrelu, name='h2/bn1')
        n = Conv2d(n, 256, (3, 3), (1, 1), act=None, padding='SAME', W_init=w_init, b_init=b_init, name='h2/c2')
        n = InstanceNormLayer(n, act=lrelu, name='h2/bn2')
        n = Conv2d(n, 512, (3, 3), (2, 2), act=None, padding='SAME', W_init=w_init, b_init=b_init, name='h2/c3')
        n = InstanceNormLayer(n, act=lrelu, name='h2/bn3')

        n = ElementwiseLayer([n, d3], tf.add, name='add3')
        n = Conv2d(n, 512, (3, 3), (1, 1), act=None, padding='SAME', W_init=w_init, b_init=b_init, name='h3/c1')
        n = InstanceNormLayer(n, act=lrelu, name='h3/bn1')
        n = Conv2d(n, 512, (3, 3), (1, 1), act=None, padding='SAME', W_init=w_init, b_init=b_init, name='h3/c2')
        n = InstanceNormLayer(n, act=lrelu, name='h3/bn2')
        n = Conv2d(n, 1024, (3, 3), (2, 2), act=None, padding='SAME', W_init=w_init, b_init=b_init, name='h3/c3')
        n = InstanceNormLayer(n, act=lrelu, name='h3/bn3')

        n = ElementwiseLayer([n, d4], tf.add, name='add4')
        n = Conv2d(n, 1024, (3, 3), (1, 1), act=None, padding='SAME', W_init=w_init, b_init=b_init, name='h4/c1')
        n = InstanceNormLayer(n, act=lrelu, name='h4/bn1')
        n = Conv2d(n, 1024, (3, 3), (2, 2), act=None, padding='SAME', W_init=w_init, b_init=b_init, name='h4/c2')
        n = InstanceNormLayer(n, act=lrelu, name='h4/bn2')

        n = FlattenLayer(n, name='hf/flatten')
        n = DenseLayer(n, n_units=1, act=tf.identity, W_init=w_init_sigmoid, name='hf/dense')
        logits = n.outputs

    return logits, tf.nn.sigmoid(logits)

def defocus_discriminator(t_image, is_train=False, reuse=False, scope='defocus_discriminator'):
    w_init = tf.contrib.layers.variance_scaling_initializer()
    w_init_sigmoid = tf.contrib.layers.xavier_initializer()
    b_init = None
    g_init = tf.random_normal_initializer(1., 0.02)
    lrelu = lambda x : tl.act.lrelu(x, 0.2)
    with tf.variable_scope(scope, reuse=reuse) as vs:
        tl.layers.set_name_reuse(reuse)
        n = InputLayer(t_image, name='in')

        n = Conv2d(n, 64, (3, 3), (1, 1), act=None, padding='SAME', W_init=w_init, name='h0/c1')
        n = InstanceNormLayer(n, act=lrelu, name='h0/b1')
        n = Conv2d(n, 64, (3, 3), (1, 1), act=None, padding='SAME', W_init=w_init, b_init=b_init, name='h0/c2')
        n = InstanceNormLayer(n, act=lrelu, name='h0/b2')
        n = Conv2d(n, 128, (3, 3), (2, 2), act=None, padding='SAME', W_init=w_init, b_init=b_init, name='h0/c3')
        n = InstanceNormLayer(n, act=lrelu, name='h0/b3')

        n = Conv2d(n, 128, (3, 3), (1, 1), act=None, padding='SAME', W_init=w_init, b_init=b_init, name='h1/c1')
        n = InstanceNormLayer(n, act=lrelu, name='h1/b1')
        n = Conv2d(n, 128, (3, 3), (1, 1), act=None, padding='SAME', W_init=w_init, b_init=b_init, name='h1/c2')
        n = InstanceNormLayer(n, act=lrelu, name='h1/b2')
        n = Conv2d(n, 256, (3, 3), (2, 2), act=None, padding='SAME', W_init=w_init, b_init=b_init, name='h1/c3')
        n = InstanceNormLayer(n, act=lrelu, name='h1/b3')

        n = Conv2d(n, 256, (3, 3), (1, 1), act=None, padding='SAME', W_init=w_init, b_init=b_init, name='h2/c1')
        n = InstanceNormLayer(n, act=lrelu, name='h2/b1')
        n = Conv2d(n, 256, (3, 3), (1, 1), act=None, padding='SAME', W_init=w_init, b_init=b_init, name='h2/c2')
        n = InstanceNormLayer(n, act=lrelu, name='h2/b2')
        n = Conv2d(n, 512, (3, 3), (2, 2), act=None, padding='SAME', W_init=w_init, b_init=b_init, name='h2/c3')
        n = InstanceNormLayer(n, act=lrelu, name='h2/b3')

        n = Conv2d(n, 512, (3, 3), (1, 1), act=None, padding='SAME', W_init=w_init, b_init=b_init, name='h3/c1')
        n = InstanceNormLayer(n, act=lrelu, name='h3/b1')
        n = Conv2d(n, 512, (3, 3), (1, 1), act=None, padding='SAME', W_init=w_init, b_init=b_init, name='h3/c2')
        n = InstanceNormLayer(n, act=lrelu, name='h3/b2')
        n = Conv2d(n, 1024, (3, 3), (2, 2), act=None, padding='SAME', W_init=w_init, b_init=b_init, name='h3/c3')
        n = InstanceNormLayer(n, act=lrelu, name='h3/b3')

        n = Conv2d(n, 1024, (3, 3), (1, 1), act=None, padding='SAME', W_init=w_init, b_init=b_init, name='h4/c1')
        n = InstanceNormLayer(n, act=lrelu, name='h4/b1')
        n = Conv2d(n, 1024, (3, 3), (1, 1), act=None, padding='SAME', W_init=w_init, b_init=b_init, name='h4/c2')
        n = InstanceNormLayer(n, act=lrelu, name='h4/b2')

        n = FlattenLayer(n, name='hf/flatten')
        n = DenseLayer(n, n_units=1, act=tf.identity, W_init=w_init_sigmoid, name='hf/dense')

        logits = n.outputs

        return logits, tf.nn.sigmoid(logits)

def Binary_Net(input_defocus, is_train=False, reuse=False, scope = 'Binary_Net'):
    w_init_relu = tf.contrib.layers.variance_scaling_initializer()
    w_init_sigmoid = tf.contrib.layers.xavier_initializer()
    b_init = None # tf.constant_initializer(value=0.0)
    g_init = tf.random_normal_initializer(1., 0.02)
    lrelu = lambda x: tl.act.lrelu(x, 0.2)
    with tf.variable_scope(scope, reuse=reuse) as vs:
        n = InputLayer(input_defocus, name='input_defocus')
        
        n = Conv2d(n, 64, (1, 1), (1, 1), act=None, padding='VALID', W_init=w_init_relu, name='l1/c1')
        n = InstanceNormLayer(n, act=lrelu, name='l1/b1')
        n = Conv2d(n, 64, (1, 1), (1, 1), act=None, padding='VALID', W_init=w_init_relu, name='l1/c2')
        n = InstanceNormLayer(n, act=lrelu, name='l1/b2')
        n = Conv2d(n, 64, (1, 1), (1, 1), act=None, padding='VALID', W_init=w_init_relu, name='l1/c3')
        n = InstanceNormLayer(n, act=lrelu, name='l1/b3')

        n = Conv2d(n, 32, (1, 1), (1, 1), act=None, padding='VALID', W_init=w_init_relu, name='l2/c1')
        n = InstanceNormLayer(n, act=lrelu, name='l2/b1')
        n = Conv2d(n, 32, (1, 1), (1, 1), act=None, padding='VALID', W_init=w_init_relu, name='l2/c2')
        n = InstanceNormLayer(n, act=lrelu, name='l2/b2')
        n = Conv2d(n, 32, (1, 1), (1, 1), act=None, padding='VALID', W_init=w_init_relu, name='l2/c3')
        n = InstanceNormLayer(n, act=lrelu, name='l2/b3')

        n = Conv2d(n, 16, (1, 1), (1, 1), act=None, padding='VALID', W_init=w_init_relu, name='l3/c1')
        n = InstanceNormLayer(n, act=lrelu, name='l3/b1')
        n = Conv2d(n, 16, (1, 1), (1, 1), act=None, padding='VALID', W_init=w_init_relu, name='l3/c2')
        n = InstanceNormLayer(n, act=lrelu, name='l3/b2')
        n = Conv2d(n, 16, (1, 1), (1, 1), act=None, padding='VALID', W_init=w_init_relu, name='l3/c3')
        n = InstanceNormLayer(n, act=lrelu, name='l3/b3')

        n = Conv2d(n, 1, (1, 1), (1, 1), act=None, padding='VALID', W_init=w_init_sigmoid, name='l4/c1')
        logits = n.outputs

        return logits, tf.nn.sigmoid(logits)
