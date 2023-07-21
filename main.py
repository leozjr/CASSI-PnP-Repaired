#%%
import time
import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt
from statistics import mean
from numpy import *
from dvp_linear_inv_cassi import (gap_denoise, admm_denoise)
from utils import (A, At, shift_back)


datasetdir = './Datasets' # dataset
resultsdir = './results' # results
# datname = 'kaist_crop256_01' # name of the dataset
datname = 'icvl_crop256_10'
matfile = datasetdir + '/' + datname + '.mat' # path of the .mat data file
method = 'GAP'  # 'GAP' or 'ADMM'

## data opeartions
r, c, nC, step = 256, 256, 31, 1
random.seed(5)
mask=np.zeros((r, c + step * (nC - 1)))
mask_3d = np.tile(mask[:, :, np.newaxis], (1, 1, nC))
mask256=sio.loadmat(r'./mask/mask256.mat')['mask']
#mask512=sio.loadmat(r'.mask/mask512.mat')['mask']
#mask1024=sio.loadmat(r'.mask/mask1024.mat')['mask']
for i in range(nC):
     mask_3d[:, i:i+256, i]=mask256
truth = sio.loadmat(matfile)['img']

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
    vgaptv,psnr_gaptv,ssim_gaptv = gap_denoise(meas,Phi,A,At,_lambda, 
                        accelerate, denoiser, iter_max, 
                        tv_weight=tv_weight, 
                        tv_iter_max=tv_iter_max,
                        X_orig=truth,
                        sigma=[130,130,130,130,130,130,130,130],
                        nc=nC)
    end_time = time.time()
    vrecon = shift_back(vgaptv,step=1)
    tgaptv = end_time - begin_time
    print('GAP-{} PSNR {:2.2f} dB, running time {:.1f} seconds.'.format(
        denoiser.upper(), mean(psnr_gaptv), tgaptv))
        
elif method == 'ADMM':
    ## [2.1] ADMM [for baseline reference]
    _lambda = 1 # regularization factor
    gamma = 0.01 # Parameter in the ADMM projection
    denoiser = 'hsicnn' # total variation (TV)
    iter_max = 50 # maximum number of iterations
    tv_weight = 0.1 # TV denoising weight (larger for smoother but slower)
    tv_iter_max = 5 # TV denoising maximum number of iterations each
    begin_time = time.time()
    vadmmtv,psnr_admmtv,ssim_admmtv = admm_denoise(meas,Phi,A,At,_lambda,
                        gamma, denoiser, iter_max, 
                        tv_weight=tv_weight, 
                        tv_iter_max=tv_iter_max,
                        X_orig=truth,
                        sigma=[100,100,80,70,60,90],
                        nc=nC)
    end_time = time.time()
    vrecon = shift_back(vadmmtv,step=1)
    tadmmtv = end_time - begin_time
    print('ADMM-{} PSNR {:2.2f} dB, running time {:.1f} seconds.'.format(
        denoiser.upper(), mean(psnr_admmtv), tadmmtv))
else:
    print('please input correct method.')
sio.savemat('./result_img/{}_result.mat'.format(datname),{'img':vrecon})
fig = plt.figure(figsize=(10, 10))
for i in range(9):
    plt.subplot(3, 3, i+1)
    plt.imshow(vrecon[:,:,(i+1)*3], cmap=plt.cm.gray, vmin=0, vmax=1)
    plt.axis('off')
    plt.savefig('./result_img/{}_result.png'.format(datname))

# %%
