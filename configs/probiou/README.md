# ProbIoU

> [Probabilistic Intersection-Over-Union for Training and Evaluation of Oriented Object Detectors](https://ieeexplore.ieee.org/document/10382963)

<!-- [ALGORITHM] -->

## Abstract

Oriented object detection is a challenging and relatively new problem. Most existing approaches are based on deep learning and explore Oriented Bounding Boxes (OBBs) to represent the objects. They are typically based on adaptations of traditional detectors that work with Horizontal Bounding Boxes (HBBs), which have been exploring IoU-like loss functions to regress the HBBs. However, extending this idea for OBBs is challenging due to complex formulations or requirement for customized backpropagation implementations. Furthermore, using OBBs presents limitations for irregular or roughly circular objects, since the definition of the ideal OBB is an ambiguous and ill-posed problem. In this work, we jointly tackle the problem of training, representing, and evaluating oriented detectors. We explore Gaussian distributions–called Gaussian Bounding Boxes (GBBs)–as fuzzy representations for oriented objects and propose using a similarity metric between two GBBs based on the Hellinger distance. We show that this metric leads to a differentiable closed-form expression that can be directly used as a localization loss term to train OBB object detectors. We also show that GBBs present a natural representation as elliptical regions (called EBBs), which inherently mitigate ambiguity representation for circular objects. Finally, we empirically show that the proposed similarity metric computed between two GBBs strongly correlates with the IoU between the corresponding EBBs, motivating the name Probabilistic Intersection-over-Union (ProbIoU). Our experiments show that results using ProbIoU as a regression loss are competitive with state-of-the-art alternatives without requiring additional hyperparameters or customized implementations, and that ProbIoU is a promising alternative to evaluate oriented object detectors. Our code is available at https://github.com/ProbIOU/ .

## Results and models

DOTA1.0

|         Backbone         |  mAP  | Angle | lr schd | Aug | Batch Size |                                                   Configs                                                   |  Download   |
| :----------------------: | :---: | :---: | :-----: | :-: | :--------: | :---------------------------------------------------------------------------------------------------------: | :---------: |
| ResNet50 (1024,1024,200) | 68.27 |  oc   |   1x    |  -  |     2      | [rotated-retinanet-hbox-oc_r50_fpn_probiou_1x_dota](./rotated-retinanet-hbox-oc_r50_fpn_probiou_1x_dota.py) | [model](<>) |
| ResNet50 (1024,1024,200) | 71.68 |  oc   |   1x    |  -  |     2      |                  [r3det-oc_r50_fpn_probiou_1x_dota](./r3det-oc_r50_fpn_probiou_1x_dota.py)                  | [model](<>) |

HRSC

|      Backbone      | AP50  | AP75  | Angle | lr schd | Aug | Batch Size |                                                    Configs                                                     |  Download   |
| :----------------: | :---: | :---: | :---: | :-----: | :-: | :--------: | :------------------------------------------------------------------------------------------------------------: | :---------: |
| ResNet50 (800,512) | 84.79 | 59.50 |  oc   |   6x    | RR  |     2      | [rotated-retinanet-hbox-oc_r50_fpn_probiou_rr-6x_hrsc](./rotated-retinanet-hbox-oc_r50_fpn_probiou_rr-6x_hrsc) | [model](<>) |

## Citation

```
@article{murrugarra2024probabilistic,
  title={Probabilistic Intersection-Over-Union for Training and Evaluation of Oriented Object Detectors},
  author={Murrugarra-Llerena, Jeffri and Kirsten, Lucas N and Zeni, Luis Felipe and Jung, Claudio R},
  journal={IEEE Transactions on Image Processing},
  year={2024},
  publisher={IEEE}
}
```
