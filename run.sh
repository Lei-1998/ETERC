#! /bin/bash
# ==============================================================================
# Copyright (C) 2021 Intel Corporation
# SPDX-License-Identifier: Apache-2.0
# ==============================================================================
echo "Running inference with OpenVINO-TensorFlow"
echo "Running inference with OpenVINO-TensorFlow" > /app/result/with_ov-tf.txt
python3 -c 'From MaskDetection.yolo import YOLO; image = Image.open('test.png'); r_image = yolo.detect_image(image); r_image.save(image_path.split('.')[0] + '_result.png');'
# python3 MaskDetection/yolo.py
# echo "Running inference with TensorFlow"
# echo "Running inference with TensorFlow" > /app/result/without_ov-tf.txt
# python3 MaskDetection/yolo.py --disable_ovtf