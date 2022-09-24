# alexnet-tensorflow-lite

Repository provides pretrained **AlexNet** model for TensorFlow Lite. The AlexNet model is designed to perform image 
classification. Model has been pretrained on the **ImageNet** dataset.

## Original model

[ONNX AlexNet](https://github.com/onnx/models/blob/main/vision/classification/alexnet/model/bvlcalexnet-12.onnx)
==> TensorFlow AlexNet ==> TensorFlow Lite AlexNet

## Accuracy

| Metric    | Value  |
|-----------|--------|
| **Top-1** | 54.80% |
| **Top-5** | 78.23% |

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
