# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import
import os
import tensorflow as tf

# ------------------------------------------------
VERSION = 'RSDD-Cascade_FPN_Res101_60000_30000_40000_0.1'
NET_NAME = 'resnet_v1_101'
ADD_BOX_IN_TENSORBOARD = True
USE_ATTENTION=False

# ---------------------------------------- System_config
ROOT_PATH =os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
print(ROOT_PATH)
GPU_GROUP = "0"
NUM_GPU = len(GPU_GROUP.strip().split(','))
SHOW_TRAIN_INFO_INTE = 10
SMRY_ITER = 50
SAVE_WEIGHTS_INTE = 5000

SUMMARY_PATH = os.path.join(ROOT_PATH,'output','summary',NET_NAME )
TEST_SAVE_PATH = ROOT_PATH + '/tools/test_result'
INFERENCE_IMAGE_PATH = ROOT_PATH + '/tools/inference_image'
INFERENCE_SAVE_PATH = ROOT_PATH + '/tools/inference_results'

if NET_NAME.startswith("resnet"):
    weights_name = NET_NAME
elif NET_NAME.startswith("MobilenetV2"):
    weights_name = "mobilenet/mobilenet_v2_1.0_224"
else:
    raise NotImplementedError



FLAGS2={}
FLAGS2["root_dir"] = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', '..', '..' ))
#预训练权重地址
PRETRAINED_CKPT = os.path.join(FLAGS2["root_dir"],'Module','LJModule',weights_name + '.ckpt') 
#ckpt权重保存地址
TRAINED_CKPT = os.path.join(FLAGS2["root_dir"],'Module','LJModule','cascade-RCNN')            
if not os.path.exists(TRAINED_CKPT):
    os.makedirs(TRAINED_CKPT)

EVALUATE_DIR = ROOT_PATH + '/output/evaluate_result_pickle/'

# ------------------------------------------ Train config
RESTORE_FROM_RPN = False
IS_FILTER_OUTSIDE_BOXES = False
FIXED_BLOCKS = 0  # allow 0~3
FREEZE_BLOCKS = [True, False, False, False, False]  # for gluoncv backbone
USE_07_METRIC = False
CUDA9 = True
EVAL_THRESHOLD = 0.5

RPN_LOCATION_LOSS_WEIGHT = 1.
RPN_CLASSIFICATION_LOSS_WEIGHT = 1.0

FAST_RCNN_LOCATION_LOSS_WEIGHT = 1.0
FAST_RCNN_CLASSIFICATION_LOSS_WEIGHT = 1.0
RPN_SIGMA = 3.0
FASTRCNN_SIGMA = 1.0

MUTILPY_BIAS_GRADIENT = None   # 2.0  # if None, will not multipy
GRADIENT_CLIPPING_BY_NORM = None   # 10.0  if None, will not clip

EPSILON = 1e-5
MOMENTUM = 0.9
BATCH_SIZE = 1

LR = 0.001  # 0.001  # 0.0003
DECAY_STEP = [30000, 40000]  # 50000, 70000
MAX_ITERATION = 60000
'''
WARM_SETP = int(0.25 * SAVE_WEIGHTS_INTE)
LR = 5e-4 * 2 * 1.25 * NUM_GPU * BATCH_SIZE
DECAY_STEP = [40000,60000,80000]  # 50000, 70000
MAX_ITERATION = 100000
'''
# -------------------------------------------- Data_preprocess_config
DATASET_NAME = 'RSDD'  # 'pascal', 'coco'
PIXEL_MEAN = [123.68, 116.779, 103.939]  # R, G, B. In tf, channel is RGB. In openCV, channel is BGR
PIXEL_MEAN_ = [0.485, 0.456, 0.406]
PIXEL_STD = [0.229, 0.224, 0.225]  # R, G, B. In tf, channel is RGB. In openCV, channel is BGR
IMG_SHORT_SIDE_LEN = 600
IMG_MAX_LENGTH = 1000
CLASS_NUM = 1


# --------------------------------------------- Network_config
INITIALIZER = tf.random_normal_initializer(mean=0.0, stddev=0.01)
BBOX_INITIALIZER = tf.random_normal_initializer(mean=0.0, stddev=0.001)
WEIGHT_DECAY = 0.00004 if NET_NAME.startswith('Mobilenet') else 0.0001
IS_ASSIGN = True

# ---------------------------------------------Anchor config
USE_CENTER_OFFSET = False
LEVLES = ['P2', 'P3', 'P4', 'P5', 'P6']
BASE_ANCHOR_SIZE_LIST = [32, 64, 128, 256, 512]
ANCHOR_STRIDE_LIST = [4, 8, 16, 32, 64]
ANCHOR_SCALES = [1.0]
ANCHOR_RATIOS = [0.5, 1., 2.0]
#ROI_SCALE_FACTORS = [10., 10., 5.0, 5.0]
ROI_SCALE_FACTORS = [[10., 10., 5.0, 5.0], [20., 20., 10.0, 10.0], [30., 30., 15.0, 15.0]]
ANCHOR_SCALE_FACTORS = None  # [10., 10., 5.0, 5.0]

# --------------------------------------------FPN config
SHARE_HEADS = True
KERNEL_SIZE = 3
RPN_IOU_POSITIVE_THRESHOLD = 0.7
RPN_IOU_NEGATIVE_THRESHOLD = 0.3
TRAIN_RPN_CLOOBER_POSITIVES = False

RPN_MINIBATCH_SIZE = 256
RPN_POSITIVE_RATE = 0.5
RPN_NMS_IOU_THRESHOLD = 0.7
RPN_TOP_K_NMS_TRAIN = 12000
RPN_MAXIMUM_PROPOSAL_TARIN = 2000

RPN_TOP_K_NMS_TEST = 6000
RPN_MAXIMUM_PROPOSAL_TEST = 1000

# -------------------------------------------Fast-RCNN config
ROI_SIZE = 14
ROI_POOL_KERNEL_SIZE = 2
USE_DROPOUT = False
KEEP_PROB = 1.0
SHOW_SCORE_THRSHOLD = 0.6  # only show in tensorboard

FAST_RCNN_NMS_IOU_THRESHOLD = 0.5  # 0.6
FAST_RCNN_NMS_MAX_BOXES_PER_CLASS = 100
FAST_RCNN_IOU_POSITIVE_THRESHOLD = 0.5
FAST_RCNN_IOU_NEGATIVE_THRESHOLD = 0.0   # 0.1 < IOU < 0.5 is negative
FAST_RCNN_MINIBATCH_SIZE = 256  # if is -1, that is train with OHEM
FAST_RCNN_POSITIVE_RATE = 0.25

ADD_GTBOXES_TO_TRAIN = False



