# PnP-CASSI
Python(pytorch) code for the paper: **Siming Zheng, Yang Liu, Ziyi Meng, Mu Qiao, Zhishen Tong, Xiaoyu Yang, Shensheng Han, and Xin Yuan, "Deep plug-and-play priors for spectral snapshot compressive imaging," Photon. Res. 9, B18-B29 (2021)**[[pdf]](https://www.osapublishing.org/DirectPDFAccess/8F3FF94D-1923-4729-B5048D3D356BAA22_446778/prj-9-2-B18.pdf?da=1&id=446778&seq=0&mobile=no) 


## Paper Abstract
We propose a plug-and-play (PnP) method, which uses deep-learning-based denoisersas regularization priors for spectral snapshot compressive imaging (SCI). Our method is efficient in terms of reconstruction quality and speed trade-off, and flexible to be ready-to-use for differentcompressive coding mechanisms.


## Repo Infomation

**English**

The repository has fixed some bugs in the original paper author's code. The original author's ADMM method had some issues and couldn't run properly. The main modifications are as follows:

- Added the "nc" parameter for the number of channels to adapt to both 31-channel and 28-channel data testing.
- Modified all dispersion steps to 1. You can adjust it to other values as needed, but make sure to maintain consistency.
- Added batch testing on the CAVE dataset. It reads all scenes in a folder for testing and saves the final PSNR and SSIM results.

> The main branch is original code from the paper's authors. In the dev branch, you will find the modified version with fixes and changes applied.

**Chinese**:

本仓库修复了原论文作者代码的一些BUG，原作者ADMM方法出现了一些问题，无法运行。主要修改如下：
- 加入nc通道数参数，以同时适应31通道和28通道数据的测试
- 修改所有色散step为1，可根据需要自行修改为其他值，但要注意前后统一
- 加入CAVE数据集批量测试，读取文件夹中所有场景进行测试并保存最终PSNR和SSIM


> main分支为原代码，dev分支为修改版本

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
