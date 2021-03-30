from cv2 import cv2
import numpy as np

noise_types = ['blur', 'gauss', 'poisson']

class ZarbiNoiseMaker:
    def process(self, img, noise_type='blur'):
        if noise_type in noise_types:
            if noise_type == 'blur':
                return self._makeGaussianBlur(img)
            if noise_type == 'gauss':
                return self._makeGaussianNoise(img)
            if noise_type == 'poisson':
                return self._makePoissonNoise(img)

    def _makeGaussianBlur(self, img):
        return cv2.GaussianBlur(img, (5, 5), 0)

    def _makeGaussianNoise(self, img):
        row, col, ch = img.shape
        mean = 0
        var = 0.1
        sigma = var**0.5
        gauss = np.random.normal(mean, sigma, (row, col, ch))
        gauss = gauss.reshape(row, col, ch)
        return img+gauss

    def _makePoissonNoise(self, img):
        vals = len(np.unique(img))
        vals = 2 ** np.ceil(np.log2(vals))
        noisy = np.random.poisson(img * vals) / float(vals)
        return noisy