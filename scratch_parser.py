import os
import pandas

ROOTDIR = "/global/scratch/akashgokul/mined_scannet_chairs/"

chair_id_dict = {}
number_of_chair_cad_models = 236778 #from shapenet
for root, scene_paths, filenames in os.walk(ROOTDIR):
    for scene_path in scene_paths:
        for chair_folder in os.listdir(root + scene_path):
            print(os.listdir(root + scene_path + "/" + chair_folder))
            break
        break
    break

