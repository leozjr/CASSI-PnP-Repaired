# PnP-CASSI
Python(pytorch) code for the paper: **Siming Zheng, Yang Liu, Ziyi Meng, Mu Qiao, Zhishen Tong, Xiaoyu Yang, Shensheng Han, and Xin Yuan, "Deep plug-and-play priors for spectral snapshot compressive imaging," Photon. Res. 9, B18-B29 (2021)**[[pdf]](https://www.osapublishing.org/DirectPDFAccess/8F3FF94D-1923-4729-B5048D3D356BAA22_446778/prj-9-2-B18.pdf?da=1&id=446778&seq=0&mobile=no) 


## Paper Abstract
We propose a plug-and-play (PnP) method, which uses deep-learning-based denoisersas regularization priors for spectral snapshot compressive imaging (SCI). Our method is efficient in terms of reconstruction quality and speed trade-off, and flexible to be ready-to-use for differentcompressive coding mechanisms.


## Repo Infomation

**English**:

This repository is primarily used for fixing bugs in the original paper author's code. The original author's ADMM method has encountered some issues and cannot run properly. This work is still in progress. Additionally, adaptation testing and other tasks will be conducted on the dev branch.

**Chinese**:

本仓库主要用于修复原论文作者代码的一些BUG，原作者ADMM方法出现了一些问题，无法运行，该工作还在进行中。 此外，还将进行它的改编测试等工作，位于dev 分支下。

## Citation
```
@article{Zheng:21,
author = {Siming Zheng and Yang Liu and Ziyi Meng and Mu Qiao and Zhishen Tong and Xiaoyu Yang and Shensheng Han and Xin Yuan},
journal = {Photon. Res.},
keywords = {Compressive imaging; Hyperspectral imaging; Multispectral imaging; Reconstruction algorithms; Remote sensing; Spatial light modulators},
number = {2},
pages = {B18--B29},
publisher = {OSA},
title = {Deep plug-and-play priors for spectral snapshot compressive imaging},
volume = {9},
month = {Feb},
year = {2021},
url = {http://www.osapublishing.org/prj/abstract.cfm?URI=prj-9-2-B18},
doi = {10.1364/PRJ.411745},
abstract = {We propose a plug-and-play (PnP) method that uses deep-learning-based denoisers as regularization priors for spectral snapshot compressive imaging (SCI). Our method is efficient in terms of reconstruction quality and speed trade-off, and flexible enough to be ready to use for different compressive coding mechanisms. We demonstrate the efficiency and flexibility in both simulations and five different spectral SCI systems and show that the proposed deep PnP prior could achieve state-of-the-art results with a simple plug-in based on the optimization framework. This paves the way for capturing and recovering multi- or hyperspectral information in one snapshot, which might inspire intriguing applications in remote sensing, biomedical science, and material science. Our code is available at: https://github.com/zsm1211/PnP-CASSI.},
}
```
