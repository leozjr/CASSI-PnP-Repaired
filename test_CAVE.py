# author: Leo date: 2023/7/21

# This code is used for batch testing on the CAVE dataset using 28-channel CAVE data.You can adjust it to 31 channels if needed. 
# All test results are saved in the "cave_results.txt" file. 
# Please make sure that the CAVE data is in .mat format, with raw data ranging from 0 to 255 and containing mask information.

import os
import time
import numpy as np
import scipy.io as sio
from statistics import mean
from numpy import *
from dvp_linear_inv_cassi import (gap_denoise, admm_denoise)
from utils import (A, At,shift_back)

def test_all(filepath, method):
    matfile = sio.loadmat(filepath)
    truth = matfile['orig']/255
    mask256 = matfile['mask']

    r, c, nC, step = 256, 256, 28, 1
    mask=np.zeros((r, c + step * (nC - 1)))
    mask_3d = np.tile(mask[:, :, np.newaxis], (1, 1, nC))
    random.seed(5)
    for i in range(nC):
        mask_3d[:, i:i+256, i]=mask256[:,:,i]

    truth_shift = np.zeros((r, c + step * (nC - 1), nC))
    for i in range(nC):
        truth_shift[:,i*step:i*step+256,i]=truth[:,:,i]

    meas = np.sum(mask_3d*truth_shift,2)
    Phi = mask_3d
    Phi_sum = np.sum(mask_3d**2,2)
    Phi_sum[Phi_sum==0]=1

    if method == 'GAP':
        _lambda = 1 # regularization factor
        accelerate = True # enable accelerated version of GAP
        denoiser = 'hsicnn' # total variation (TV); deep denoiser(hsicnn)
        iter_max = 20 # maximum number of iterations
        tv_weight = 6 # TV denoising weight (larger for smoother but slower)
        tv_iter_max = 5 # TV denoising maximum number of iterations each
        begin_time = time.time()
        vgaptv,psnr_, ssim_ = gap_denoise(meas,Phi,A,At,_lambda, 
                            accelerate, denoiser, iter_max, 
                            tv_weight=tv_weight, 
                            tv_iter_max=tv_iter_max,
                            X_orig=truth,sigma=[130,130,130,130,130,130,130,130],
                            nc=nC)
        end_time = time.time()
        vrecon = shift_back(vgaptv,step=1)
        tgaptv = end_time - begin_time
    elif method == 'ADMM': 
        _lambda = 1 # regularization factor
        gamma = 0.01 # Parameter in the ADMM projection
        denoiser = 'hsicnn' # total variation (TV)
        iter_max = 50 # maximum number of iterations
        tv_weight = 0.1 # TV denoising weight (larger for smoother but slower)
        tv_iter_max = 5 # TV denoising maximum number of iterations each
        begin_time = time.time()
        vadmmtv,psnr_,ssim_ = admm_denoise(meas,Phi,A,At,_lambda,
                            gamma, denoiser, iter_max, 
                            tv_weight=tv_weight, 
                            tv_iter_max=tv_iter_max,
                            X_orig=truth,
                            sigma=[100,100,80,70,60,90],
                            nc=nC)
        end_time = time.time()
        vrecon = shift_back(vadmmtv,step=1)
        tadmmtv = end_time - begin_time
    return psnr_[-1], ssim_[-1] #return the last psnr and ssim, you can also return the whole list or mean value

# puts your data path here
imgs_path = '/home/leo/Code/PnP/SCI-TV-FFDNet/data/CAVE/'
data_pairs = []
for filename in sorted(os.listdir(imgs_path)):
    file_path = os.path.join(imgs_path, filename)
    psnr_, ssim_ = test_all(file_path, 'GAP')
    data_pairs.append((psnr_, ssim_))
    print(file_path, psnr_, ssim_)

# save all imgs results
output_file = "cave_results.txt"
with open(output_file, "a") as file:
    line = " ".join([f"({psnr:.2f}, {ssim:.2f})" for psnr, ssim in data_pairs])
    file.write(line + "\n")