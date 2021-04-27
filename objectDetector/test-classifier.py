# Import the required modules
from skimage.transform import pyramid_gaussian
from skimage.io import imread
from skimage.feature import hog
from sklearn.externals import joblib
import cv2
import argparse as ap
from objectDetector.nms import nms
from data.config.config import *

def sliding_window(image, window_size, step_size):
    '''
    This function returns a patch of the input image `image` of size equal
    to `window_size`. The first image returned top-left co-ordinates (0, 0) 
    and are increment in both x and y directions by the `step_size` supplied.
    So, the input parameters are -
    * `image` - Input Image
    * `window_size` - Size of Sliding Window
    * `step_size` - Incremented Size of Window

    The function returns a tuple -
    (x, y, im_window)
    where
    * x is the top-left x co-ordinate
    * y is the top-left y co-ordinate
    * im_window is the sliding window image
    '''
    for y in range(0, image.shape[0], step_size[1]):
        for x in range(0, image.shape[1], step_size[0]):
            yield (x, y, image[y:y + window_size[1], x:x + window_size[0]])

if __name__ == "__main__":
    # Parse the command line arguments
    parser = ap.ArgumentParser()
    parser.add_argument('-i', "--image", default="../data/dataset/valid/pos/8aaa11f0-ad62-69bd-8fa8-e00e30b67814.jpg", help="Path to the test image")
    # parser.add_argument('-i', "--image", default="../data/dataset/valid/neg/1a927c85-33ec-5fca-806b-05ab045a62ad.jpg", help="Path to the test image")
    parser.add_argument('-v', '--visualize', help="Visualize the sliding window", default=visualize,
            action="store_true")
    args = vars(parser.parse_args())

    # Read the image
    im = imread(args["image"], as_grey=False)
    # min_wdw_sz = (100, 40)
    # step_size = (10, 10)
    visualize_det = args['visualize']

    # Load the classifier
    clf = joblib.load(model_path)

    # List to store the detections
    detections = []

    fd = hog(im, orientations, pixels_per_cell, cells_per_block, visualise=visualize, transform_sqrt=transform_sqrt).reshape(1, -1)
    pred = clf.predict(fd)
    print(pred)
