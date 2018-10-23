#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 19:54:02 2018

@author: niravshah
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

class ImageProcess:
    
    def segment():
        img = cv2.imread("59.png")
        img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        img_hsv = cv2.cvtColor(img_rgb,cv2.COLOR_RGB2HSV)
        color_range_up=np.array([1, 190, 200])
        color_range_down=np.array([18, 255, 255])
        
        light_orange = (1, 190, 200)
        dark_orange = (18, 255, 255)
        
        mask = cv2.inRange(img_hsv,color_range_up,color_range_down)
        result = cv2.bitwise_and(img_rgb,img_rgb, mask=mask)
        
        plt.imshow(result)
        
    def intensity_slicing():
        img=cv2.imread("59.png")
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #img_arr = np.array(img)
        plt.subplot(1,2,1)
        plt.imshow(gray_image,cmap="gray")
        img_arr = gray_image
        
        for i in range(img_arr.shape[0]):
            for j in range(img_arr.shape[1]):
                    if(img_arr[i][j] >100 and img_arr[i][j]<200):
                        img_arr[i][j] = 255
        
        #i = Image.fromarray(img_arr, 'RGB')
    
        plt.subplot(1,2,2)
        plt.imshow(img_arr,cmap="gray")
                    
    
    def laplacian():
        
        img = cv2.imread("test1.jpg")
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        laplacian = cv2.Laplacian(img,cv2.CV_64F)
        
        plt.subplot(1,2,1)
        plt.imshow(img,cmap="gray")
        
        plt.subplot(1,2,2)
        plt.imshow(laplacian,cmap="gray")
        
    def image_neg():
        
        img = cv2.imread("59.png")
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        
        neg=np.array(gray)
        
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                neg[i][j] = 255-int(gray[i][j])
                
        plt.subplot(1,2,1)
        plt.imshow(gray,cmap="gray")
        
        plt.subplot(1,2,2)
        plt.imshow(neg,cmap="gray")
                
    def brightness_contrast():
        img = cv2.imread("59.png")
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        img_orig=img
        brightness = 0
        contrast = 30
        img = np.int16(img)
        img = img * (contrast/127+1) - contrast + brightness
        img = np.clip(img, 0, 255)
        img = np.uint8(img)
        
        plt.subplot(1,2,1)
        plt.imshow(img_orig)
        
        plt.subplot(1,2,2)
        plt.imshow(img)
      