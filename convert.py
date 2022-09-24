import urllib.request
import onnx
from onnx_tf.backend import prepare
import tensorflow as tf

url = 'https://github.com/onnx/models/raw/main/vision/classification/alexnet/model/bvlcalexnet-12.onnx'
urllib.request.urlretrieve(url, 'bvlcalexnet-12.onnx')

model = onnx.load('bvlcalexnet-12.onnx')
prepare(model).export_graph('alexnet')

converter = tf.lite.TFLiteConverter.from_saved_model('alexnet')
tfliteModel = converter.convert()

with open('alexnet.tflite', 'wb') as f:
    f.write(tfliteModel)
