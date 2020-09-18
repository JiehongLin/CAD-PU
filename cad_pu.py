import tensorflow as tf
from upsampling.model import Model
from upsampling.configs import FLAGS
from datetime import datetime
import os
import logging
import pprint
pp = pprint.PrettyPrinter()

def run():
    if FLAGS.phase=='train':
        if not os.path.exists(FLAGS.log_dir):
            os.makedirs(FLAGS.log_dir)
    else:
        FLAGS.test_dir = os.path.join(FLAGS.log_dir, 'test_point_cloud_results')
        if not os.path.exists(FLAGS.test_dir):
            os.makedirs(FLAGS.test_dir)
    pp.pprint(FLAGS)
    
    # open session
    run_config = tf.ConfigProto()
    run_config.gpu_options.allow_growth = True
    with tf.Session(config=run_config) as sess:
        model = Model(FLAGS,sess)
        if FLAGS.phase == 'train':
            model.train()
        else:
            model.test()


def main(unused_argv):
  run()

if __name__ == '__main__':
  logging.basicConfig(level=logging.INFO)
  tf.app.run()
