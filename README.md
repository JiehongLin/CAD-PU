# CAD-PU: A Curvature-Adaptive Deep Learning Solution for Point Set Upsampling
Created by Jiehong Lin, Xian Shi, Yuan Gao, Ke Chen, Kui Jia.

### Introduciton 
This repository is for our paper '[CAD-PU: A Curvature-Adaptive Deep LearningSolution for Point Set Upsampling](https://arxiv.org/abs/2009.04660)'.

### Installation

**Install Tensorflow.** This code is tested with [Tensorflow 1.11.0](https://www.tensorflow.org) GPU version and [Python 3.6.5](https://www.python.org/downloads/release/python-365/) on Ubuntu 16.04. There are also some dependencies for a few Python libraries for data processing and visualizations like cv2, h5py etc.

**Compile Customized TF Operators.** The TF operators are included in ```tf_ops``` folder. You need to run ```./tf_*_compile.sh``` under each ops subfolder to compile them. Note that you may update ```nvcc``` and ```python``` path if necessary.

### Usage

1、 Download training and test mesh files from [GoogleDrive](https://drive.google.com/open?id=1BNqjidBVWP0_MUdMTeGy1wZiR6fqyGmC). Unzip and organize these files in ```data``` folder as follows:
```
data
├── CAD_model
│   ├── complex
│   ├── medium
│   ├── simple
│   └── test
...
```
2、 Prepare training and test data.
```
python data_processing.py
```
3、 Train the model.
```
python cad_pu.py --phase train
```
4、 Evaluate the model.
```
python cad_pu.py --phase test
```

### Evaluation
1、Reconstruct the point sets of testing outputs of in ```log/test_point_cloud_results``` folder to meshes. We use Screened Poisson Reconstruction algorithm in [MeshLab](https://www.meshlab.net/) for reconstruciton.
Save the reconstructed meshes in ```.off``` format and organize them in ```log/test_mesh_results``` folder as follows:

```
log
├── test_point_cloud_results
│   ├── 11509_Panda_v4.xyz
│   ├── 13770_Tiger_V1.xyz
│   └── ...
├── test_mesh_results
│   ├── 11509_Panda_v4.off
│   ├── 13770_Tiger_V1.off
│   └── ...
...
```

2、Evaluation.
```
python evaluation.py
```


### Citation
If you find our work useful in your research, please consider citing:
```
@article{lin2020cad,
  title={CAD-PU: A Curvature-Adaptive Deep Learning Solution for Point Set Upsampling},
  author={Lin, Jiehong and Shi, Xian and Gao, Yuan and Chen, Ke and Jia, Kui},
  journal={arXiv preprint arXiv:2009.04660},
  year={2020}
}
```


### License
Our code is released under MIT License (see LICENSE file for details).

### Acknowledgement
The structure of this codebase is modified from [PU-GAN](https://github.com/liruihui/PU-GAN).

