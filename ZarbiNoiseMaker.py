from cv2 import cv2
import numpy as np

noise_types = ['blur', 'gauss', 'poisson', 'speckle']

class ZarbiNoiseMaker:
    """
    class ZarbiNoiseMaker
    ----------
    Add noise to an image. The noise can be blur, gauss, poisson or speckle
    """
    def process(self, img, noise_type='blur'):
        """
        Parameters
        ----------
        img : numpy.ndarray
            image to process

        noise_type : string => [blur, gauss, poisson, speckle]
            type of noise to be applied
        ----------
        Add a noise to an image
        """
        if noise_type in noise_types:
            if noise_type == 'blur':
                return self._makeGaussianBlur(img)
            if noise_type == 'gauss':
                return self._makeGaussianNoise(img)
            if noise_type == 'poisson':
                return self._makePoissonNoise(img)
            if noise_type == 'speckle':
                return self._makeSpeckleNoise(img)

    def _makeGaussianBlur(self, img):
        """
        Parameters
        ----------
        img: numpy.ndarray
            image to process
        ----------
        Add a Gaussian blur to the image

        return the  post-processed image
        """
        return cv2.GaussianBlur(img, (5, 5), 0)

    def _makeGaussianNoise(self, img):
        """
        Parameters
        ----------
        img: numpy.ndarray
            image to process
        ----------
        Add a Gaussian noise to the image

        return the post-processed image
        """
        mean = 127
        var = 0.4
        sigma = var ** 0.5
        gauss = np.random.normal(mean, sigma, img.shape)
        gauss = gauss.reshape(img.shape[0], img.shape[1], img.shape[2]).astype('uint8')
        noisy = img + gauss
        return noisy

    def _makePoissonNoise(self, img):
        """
        Parameters
        ----------
        img: numpy.ndarray
            image to process
        ----------
        Add a Poisson noise to the image

        return the post-processed image
        """
        img = img.astype('uint8')
        poissonNoise = np.random.poisson(img).astype('uint8')
        noisy = img + poissonNoise
        return noisy

    def _makeSpeckleNoise(self, img):
        """
        Parameters
        ----------
        img: numpy.ndarray
            image to process
        ----------
        Add a speckle noise to the image

        return the post-processed image
        """
        gauss = np.random.normal(0, 1, img.shape)
        gauss = gauss.reshape(img.shape[0], img.shape[1], img.shape[2]).astype('uint8')
        noisy = img * gauss + img 
        return noisy