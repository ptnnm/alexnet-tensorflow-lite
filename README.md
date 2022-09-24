# alexnet-tensorflow-lite

Repository provides pretrained **AlexNet** model for TensorFlow Lite. The AlexNet model is designed to perform image 
classification. Model has been pretrained on the **ImageNet** dataset.

## Model

| Metric      | Value                                                            |
|-------------|------------------------------------------------------------------|
| **Type**    | Classification                                                   |
| **Size**    | 232 MB                                                           |
| **SHA-256** | 4e884db8603212651519b3de2ebed24904d855602a5ca171dd3a679eb0ac9c7c |

Download:

```text
curl -Lo alexnet.tflite https://github.com/ptnnm/alexnet-tensorflow-lite/releases/latest/download/alexnet.tflite
```

## Original model

[ONNX AlexNet](https://github.com/onnx/models/blob/main/vision/classification/alexnet/model/bvlcalexnet-12.onnx)
==> TensorFlow AlexNet ==> TensorFlow Lite AlexNet

```python
python convert.py
```

## Accuracy

| Metric    | Value  |
|-----------|--------|
| **Top-1** | 54.80% |
| **Top-5** | 78.23% |

The accuracy in the table depends on the preprocessing method provided [here](https://github.com/intel/neural-compressor/blob/master/examples/onnxrt/image_recognition/onnx_model_zoo/alexnet/quantization/ptq/main.py#L52).

## Dataset

ImageNet ([ILSVRC2012](https://image-net.org/challenges/LSVRC/2012/))

## Input

| Detail            | Value                                       |
|-------------------|---------------------------------------------|
| **Input**         | Image                                       |
| **Shape**         | float[1, 3, 224, 224] - [B, C, H, W]        |
| **Mean Values**   | float[123.68, 116.779, 103.939] - [R, G, B] |
| **Channel Order** | BGR                                         |

* [B, C, H, W] - Batch size, Channel, Height, Width
* [R, G, B] - Red, Green, Blue

## Output

| Detail     | Value              |
|------------|--------------------|
| **Output** | ImageNet classes   |
| **Shape**  | [1, 1000] - [B, C] |

* [B, C] - Batch size, Predicted probabilities for each class in [0, 1] range

## Reference

1. [ONNX AlexNet models](https://github.com/onnx/models/tree/main/vision/classification/alexnet)
2. [ImageNet Classification with Deep Convolutional Neural Networks](https://proceedings.neurips.cc/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf)
