import tensorflow as tf
import tensorlayer as tl
import numpy as np
from tensorlayer.layers import *

def UNet_down(t_image, is_train=False, reuse=False, scope = 'unet_down'):
    w_init1 = tf.random_normal_initializer(stddev=0.02)
    w_init2 = tf.random_normal_initializer(stddev=0.01)
    w_init3 = tf.random_normal_initializer(stddev=0.005)
    w_init4 = tf.random_normal_initializer(stddev=0.002)
    b_init = None # tf.constant_initializer(value=0.0)
    g_init = tf.random_normal_initializer(1., 0.02)
    hrg = t_image.get_shape()[1]
    wrg = t_image.get_shape()[2]
    with tf.variable_scope(scope, reuse=reuse) as vs:
        tl.layers.set_name_reuse(reuse)
        n = InputLayer(t_image, name='in')
        n_init = InputLayer(t_image, name='in2')
        n = Conv2d(n, 64, (3, 3), (1, 1), act=None, padding='SAME', W_init=w_init1, name='f0/c')
        n = BatchNormLayer(n, is_train=is_train, gamma_init=g_init, name='f0/b')
        f0 = n
        n = Conv2d(n, 64, (3, 3), (2, 2), act=None, padding='SAME', W_init=w_init2, name='d1/c1')
        n = BatchNormLayer(n, act=tf.nn.relu, is_train=is_train, gamma_init=g_init, name='d1/b1')
        n = Conv2d(n, 64, (3, 3), (1, 1), act=None, padding='SAME', W_init=w_init2, name='d1/c2')
        n = BatchNormLayer(n, act=tf.nn.relu, is_train=is_train, gamma_init=g_init, name='d1/b2')
        n = Conv2d(n, 128, (3, 3), (1, 1), act=None, padding='SAME', W_init=w_init2, name='d1/c3')
        n = BatchNormLayer(n, is_train=is_train, gamma_init=g_init, name='d1/b3')
        f1_2 = n
        n = Conv2d(n, 128, (3, 3), (2, 2), act=None, padding='SAME', W_init=w_init3, name='d2/c1')
        n = BatchNormLayer(n, act=tf.nn.relu, is_train=is_train, gamma_init=g_init, name='d2/b1')
        n = Conv2d(n, 128, (3, 3), (1, 1), act=None, padding='SAME', W_init=w_init3, name='d2/c2')
        n = BatchNormLayer(n, act=tf.nn.relu, is_train=is_train, gamma_init=g_init, name='d2/b2')
        n = Conv2d(n, 128, (3, 3), (1, 1), act=None, padding='SAME', W_init=w_init3, name='d2/c3')
        n = BatchNormLayer(n, act=tf.nn.relu, is_train=is_train, gamma_init=g_init, name='d2/b3')
        n = Conv2d(n, 128, (3, 3), (1, 1), act=None, padding='SAME', W_init=w_init3, name='d2/c4')
        n = BatchNormLayer(n, is_train=is_train, gamma_init=g_init, name='d2/b4')
        f2_3 = n
        n = Conv2d(n, 256, (3, 3), (2, 2), act=None, padding='SAME', W_init=w_init4, name='d3/c1')
        n = BatchNormLayer(n, act=tf.nn.relu, is_train=is_train, gamma_init=g_init, name='d3/b1')
        n = Conv2d(n, 256, (3, 3), (1, 1), act=None, padding='SAME', W_init=w_init4, name='d3/c2')
        n = BatchNormLayer(n, act=tf.nn.relu, is_train=is_train, gamma_init=g_init, name='d3/b2')
        n = Conv2d(n, 256, (3, 3), (1, 1), act=None, padding='SAME', W_init=w_init4, name='d3/c3')
        n = BatchNormLayer(n, act=tf.nn.relu, is_train=is_train, gamma_init=g_init, name='d3/b3')
        n = Conv2d(n, 256, (3, 3), (1, 1), act=None, padding='SAME', W_init=w_init4, name='d3/c4')
        n = BatchNormLayer(n, act=tf.nn.relu, is_train=is_train, gamma_init=g_init, name='d3/b4')
        
        f3_4 = n
        n = Conv2d(n, 256, (3, 3), (2, 2), act=None, padding='SAME', W_init=w_init4, name='d4/c1')
        n = BatchNormLayer(n, act=tf.nn.relu, is_train=is_train, gamma_init=g_init, name='d4/b1')
        n = Conv2d(n, 256, (3, 3), (1, 1), act=None, padding='SAME', W_init=w_init4, name='d4/c2')
        n = BatchNormLayer(n, act=tf.nn.relu, is_train=is_train, gamma_init=g_init, name='d4/b2')
        n = Conv2d(n, 512, (3, 3), (1, 1), act=None, padding='SAME', W_init=w_init4, name='d4/c3')
        n = BatchNormLayer(n, act=tf.nn.relu, is_train=is_train, gamma_init=g_init, name='d4/b3')
        n = Conv2d(n, 512, (3, 3), (1, 1), act=None, padding='SAME', W_init=w_init4, name='d4/c4')
        n = BatchNormLayer(n, act=tf.nn.relu, is_train=is_train, gamma_init=g_init, name='d4/b4')
        
        return f0.outputs, f1_2.outputs, f2_3.outputs, f3_4.outputs, n.outputs

def UNet_up(f0_in, f1_2_in, f2_3_in, f3_4_in, last_in, hrg, wrg, is_train=False, reuse=False, scope = 'unet_up'):
    w_init1 = tf.random_normal_initializer(stddev=0.02)
    w_init2 = tf.random_normal_initializer(stddev=0.01)
    w_init3 = tf.random_normal_initializer(stddev=0.005)
    w_init4 = tf.random_normal_initializer(stddev=0.002)
    b_init = None # tf.constant_initializer(value=0.0)
    g_init = tf.random_normal_initializer(1., 0.02)
    with tf.variable_scope(scope, reuse=reuse) as vs:
        tl.layers.set_name_reuse(reuse)
        f0 = InputLayer(f0_in, name='f0')
        f1_2 = InputLayer(f1_2_in, name='f1_2')
        f2_3 = InputLayer(f2_3_in, name='f2_3')
        f3_4 = InputLayer(f3_4_in, name='f3_4')
        last = InputLayer(last_in, name='last')
        
        n = DeConv2d(last, 256, (3, 3), (hrg/8, wrg/8), (2, 2), act=None, padding='SAME', W_init=w_init3, name='u4/d')
        n = BatchNormLayer(n, is_train=is_train, gamma_init=g_init, name='u4/b')
        n = ElementwiseLayer([n, f3_4], tf.add, name='s5')
        n.outputs = tf.nn.relu(n.outputs, name = 'relu5')
        
        n = Conv2d(n, 256, (3, 3), (1, 1), act=None, padding='SAME', W_init=w_init3, name='u4/c1')
        n = BatchNormLayer(n, act=tf.nn.relu, is_train=is_train, gamma_init=g_init, name='u4/b1')
        n = Conv2d(n, 256, (3, 3), (1, 1), act=None, padding='SAME', W_init=w_init3, name='u4/c2')
        n = BatchNormLayer(n, act=tf.nn.relu, is_train=is_train, gamma_init=g_init, name='u4/b2')
        n = Conv2d(n, 256, (3, 3), (1, 1), act=None, padding='SAME', W_init=w_init3, name='u4/c3')
        n = BatchNormLayer(n, act=tf.nn.relu, is_train=is_train, gamma_init=g_init, name='u4/b3')
        n = DeConv2d(n, 128, (3, 3), (hrg/4, wrg/4), (2, 2), act=None, padding='SAME', W_init=w_init3, name='u3/d')
        n = BatchNormLayer(n, is_train=is_train, gamma_init=g_init, name='u3/b')
        n = ElementwiseLayer([n, f2_3], tf.add, name='s4')
        n.outputs = tf.nn.relu(n.outputs, name = 'relu4')

        n = Conv2d(n, 128, (3, 3), (1, 1), act=None, padding='SAME', W_init=w_init3, name='u3/c1')
        n = BatchNormLayer(n, act=tf.nn.relu, is_train=is_train, gamma_init=g_init, name='u3/b1')
        n = Conv2d(n, 128, (3, 3), (1, 1), act=None, padding='SAME', W_init=w_init3, name='u3/c2')
        n = BatchNormLayer(n, act=tf.nn.relu, is_train=is_train, gamma_init=g_init, name='u3/b2')
        n = Conv2d(n, 128, (3, 3), (1, 1), act=None, padding='SAME', W_init=w_init3, name='u3/c3')
        n = BatchNormLayer(n, act=tf.nn.relu, is_train=is_train, gamma_init=g_init, name='u3/b3')

        n = DeConv2d(n, 128, (3, 3), (hrg/2, wrg/2), (2, 2), act=None, padding='SAME', W_init=w_init2, name='u2/d')
        n = BatchNormLayer(n, is_train=is_train, gamma_init=g_init, name='u2/b')
        n = ElementwiseLayer([n, f1_2], tf.add, name='s3')
        n.outputs = tf.nn.relu(n.outputs, name = 'relu3')
        
        n = Conv2d(n, 128, (3, 3), (1, 1), act=None, padding='SAME', W_init=w_init2, name='u2/c1')
        n = BatchNormLayer(n, act=tf.nn.relu, is_train=is_train, gamma_init=g_init, name='u2/b1')
        n = Conv2d(n, 64, (3, 3), (1, 1), act=None, padding='SAME', W_init=w_init2, name='u2/c2')
        n = BatchNormLayer(n, act=tf.nn.relu, is_train=is_train, gamma_init=g_init, name='u2/b2')

        n = DeConv2d(n, 64, (3, 3), (hrg, wrg), (2, 2), act=None, padding='SAME', W_init=w_init1, name='u1/d')
        n = BatchNormLayer(n, is_train=is_train, gamma_init=g_init, name='u1/b')
        n = ElementwiseLayer([n, f0], tf.add, name='s2')
        n.outputs = tf.nn.relu(n.outputs, name = 'relu2')
        n = Conv2d(n, 15, (3, 3), (1, 1), act=None, padding='SAME', W_init=w_init1, name='u1/c1')
        n = BatchNormLayer(n, act=tf.nn.relu, is_train=is_train, gamma_init=g_init, name='u1/b1')
        n = Conv2d(n, 1, (3, 3), (1, 1), act=None, padding='SAME', W_init=w_init1, name='u1/c2')
        logits = n.outputs
        n.outputs = tf.nn.sigmoid(n.outputs)

        return logits, n.outputs

def SRGAN_d(input_images, is_train=True, reuse=False, scope = 'Discriminator'):
    w_init = tf.random_normal_initializer(stddev=0.02)
    b_init = None # tf.constant_initializer(value=0.0)
    gamma_init=tf.random_normal_initializer(1., 0.02)
    df_dim = 16
    lrelu = lambda x: tl.act.lrelu(x, 0.2)
    with tf.variable_scope(scope, reuse=reuse):
        tl.layers.set_name_reuse(reuse)
        net_in = InputLayer(input_images, name='input/images')
        net_h0 = Conv2d(net_in, df_dim, (4, 4), (2, 2), act=lrelu,
                padding='SAME', W_init=w_init, name='h0/c')

        net_h1 = Conv2d(net_h0, df_dim*2, (4, 4), (2, 2), act=None,
                padding='SAME', W_init=w_init, b_init=b_init, name='h1/c')
        net_h1 = BatchNormLayer(net_h1, act=lrelu, is_train=is_train,
                gamma_init=gamma_init, name='h1/bn')
        net_h2 = Conv2d(net_h1, df_dim*4, (4, 4), (2, 2), act=None,
                padding='SAME', W_init=w_init, b_init=b_init, name='h2/c')
        net_h2 = BatchNormLayer(net_h2, act=lrelu, is_train=is_train,
                gamma_init=gamma_init, name='h2/bn')
        net_h3 = Conv2d(net_h2, df_dim*8, (4, 4), (2, 2), act=None,
                padding='SAME', W_init=w_init, b_init=b_init, name='h3/c')
        net_h3 = BatchNormLayer(net_h3, act=lrelu, is_train=is_train,
                gamma_init=gamma_init, name='h3/bn')
        net_h4 = Conv2d(net_h3, df_dim*16, (4, 4), (2, 2), act=None,
                padding='SAME', W_init=w_init, b_init=b_init, name='h4/c')
        net_h4 = BatchNormLayer(net_h4, act=lrelu, is_train=is_train,
                gamma_init=gamma_init, name='h4/bn')
        net_h5 = Conv2d(net_h4, df_dim*32, (4, 4), (2, 2), act=None,
                padding='SAME', W_init=w_init, b_init=b_init, name='h5/c')
        net_h5 = BatchNormLayer(net_h5, act=lrelu, is_train=is_train,
                gamma_init=gamma_init, name='h5/bn')
        net_h6 = Conv2d(net_h5, df_dim*16, (1, 1), (1, 1), act=None,
                padding='SAME', W_init=w_init, b_init=b_init, name='h6/c')
        net_h6 = BatchNormLayer(net_h6, act=lrelu, is_train=is_train,
                gamma_init=gamma_init, name='h6/bn')
        net_h7 = Conv2d(net_h6, df_dim*8, (1, 1), (1, 1), act=None,
                padding='SAME', W_init=w_init, b_init=b_init, name='h7/c')
        net_h7 = BatchNormLayer(net_h7, is_train=is_train,
                gamma_init=gamma_init, name='h7/bn')

        net = Conv2d(net_h7, df_dim*2, (1, 1), (1, 1), act=None,
                padding='SAME', W_init=w_init, b_init=b_init, name='res/c')
        net = BatchNormLayer(net, act=lrelu, is_train=is_train,
                gamma_init=gamma_init, name='res/bn')
        net = Conv2d(net, df_dim*2, (3, 3), (1, 1), act=None,
                padding='SAME', W_init=w_init, b_init=b_init, name='res/c2')
        net = BatchNormLayer(net, act=lrelu, is_train=is_train,
                gamma_init=gamma_init, name='res/bn2')
        net = Conv2d(net, df_dim*8, (3, 3), (1, 1), act=None,
                padding='SAME', W_init=w_init, b_init=b_init, name='res/c3')
        net = BatchNormLayer(net, is_train=is_train,
                gamma_init=gamma_init, name='res/bn3')
        net_h8 = ElementwiseLayer([net_h7, net], tf.add, name='res/add')
        net_h8.outputs = tl.act.lrelu(net_h8.outputs, 0.2)

        net_ho = FlattenLayer(net_h8, name='ho/flatten')
        net_ho = DenseLayer(net_ho, n_units=1, act=tf.identity,
                W_init = w_init, name='ho/dense')
        logits = net_ho.outputs
        net_ho.outputs = tf.nn.sigmoid(net_ho.outputs)

    return logits
