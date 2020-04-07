import os
import pandas

ROOTDIR = "/global/scratch/akashgokul/mined_scannet_chairs/"

chair_id_dict = {}
number_of_chair_cad_models = 236778 #from shapenet
for root, scene_paths, filenames in os.walk(ROOTDIR):
    print(scene_paths)
    for scene_path in scene_paths:
        for chair_path, chair_dir_name, chair_files in os.walk(scene_path):
            chair_dir_files = os.listdir(chair_path)
            print("SCENE: " + scene_path + " | CHAIR PATH: " + chair_path)
            cad_id_file = open(chair_path + "/id_cad.txt", "r")
            cad_id = cad_id_file.readline()
            print("CAD ID: " + cad_id)
            chair_id_dict[chair_path + "/model_normalized.ply"] = cad_id


