import os
import pandas

ROOTDIR = "/global/scratch/akashgokul/mined_scannet_chairs/"

chair_id_dict = {}
number_of_chair_cad_models = 236778 #from shapenet
for root, scene_paths, filenames in os.walk(ROOTDIR):
    for scene_path in scene_paths:
        for chair_dir in os.listdir(root + scene_path):
            chair_dir_path = root + scene_path + "/" + chair_dir
            chair_dir_contents = os.listdir(chair_dir_path)
            cad_id_file = open(chair_dir_path + "/id_cad.txt", "r")
            cad_id = cad_id_file.readline()
            pointcloud_dir = chair_dir_path + "/model_normalized.ply"
            print(pointcloud_dir)
            print(cad_id)
            chair_id_dict[pointcloud_dir] = cad_id

            break
        break
    break

