from cv2 import cv2
import numpy as np

noise_types = ['blur', 'gauss', 'poisson', 'speckle']

class ZarbiNoiseMaker:
    def process(self, img, noise_type='blur'):
        if noise_type in noise_types:
            #if noise_type == 'blur':
            #    return self._makeGaussianBlur(img)
            if noise_type == 'gauss':
                return self._makeGaussianNoise(img)
            if noise_type == 'poisson':
                return self._makePoissonNoise(img)
            if noise_type == 'speckle':
                return self._makeSpeckleNoise(img)

    def _makeGaussianBlur(self, img):
        return cv2.GaussianBlur(img, (5, 5), 0)

    def _makeGaussianNoise(self, img):
        mean = 127
        var = 0.4
        sigma = var ** 0.5
        gauss = np.random.normal(mean, sigma, img.shape)
        gauss = gauss.reshape(img.shape[0], img.shape[1], img.shape[2]).astype('uint8')
        noisy = img + gauss
        return noisy

    def _makePoissonNoise(self, img):
        img = img.astype('uint8')
        poissonNoise = np.random.poisson(img).astype('uint8')
        noisy = img + poissonNoise
        return noisy

    def _makeSpeckleNoise(self, img):
        gauss = np.random.normal(0, 1, img.shape)
        gauss = gauss.reshape(img.shape[0], img.shape[1], img.shape[2]).astype('uint8')
        noisy = img * gauss + img 
        return noisy