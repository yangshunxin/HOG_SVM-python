import configparser
import os

configName = "config.cfg"
configPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), configName)
print(configPath)
cf = configparser.ConfigParser()
cf.read(configPath)

secs = cf.sections()
# print(secs)

options = cf.options("paths")
# print(options)

items = cf.items("paths")
# print(items)
for i in secs:
    it = cf.items(i)
    for x in it:
        print(x)


# [hog]
min_wdw_sz = eval(cf.get("hog", "min_wdw_sz"))
step_size = eval(cf.get("hog", "step_size"))
orientations = eval(cf.get("hog", "orientations"))
pixels_per_cell = eval(cf.get("hog", "pixels_per_cell"))
cells_per_block = eval(cf.get("hog", "cells_per_block"))
visualize = eval(cf.get("hog", "visualize"))
transform_sqrt = eval(cf.get("hog", "transform_sqrt"))

# [nms]
threshold = eval(cf.get("nms", "threshold"))

# [paths]
pos_feat_ph = cf.get("paths", "pos_feat_ph")
neg_feat_ph = cf.get("paths", "neg_feat_ph")
model_path = cf.get("paths", "model_path")

