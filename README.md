# HOG_SVM-python
this project we use hog feature to classify and detect in images
# HOG_SVM-python
this project we use hog feature to classify and detect in images
ref: https://github.com/bikz05/object-detector.git

这个demo是概括了svm算法在图像领域的应用
在图像检测的步骤：
1. 将有汽车的图片作为正样本，将无汽车的图片作为负样本；然后提取图片的HOG特征，对SVM进行训练；生成SVM的模型文件并保存成文件；
对模型的预测：
1. 加载图片，然后做高斯金字塔，之后通过放缩比例计算出不同尺度下，在原图中相同位置的概率，通过NMS排除位置相同的位置，就可以得到结果。

图像的分类：
其实每一个svm都是一个分类器，直接根据特征获取类别和概率。
