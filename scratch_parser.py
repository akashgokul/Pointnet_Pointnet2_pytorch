import os
import pandas

ROOTDIR = "/global/scratch/akashgokul/mined_scannet_chairs"

chair_id_dict = {}
number_of_chair_cad_models = 236778 #from shapenet
for scene_path, scene_name, filenames in os.walk(ROOTDIR):
    for chair_path, chair_dir_name, chair_files in os.walk(scene_path):
        chair_dir_files = os.listdir(chair_path)
        print("CHAIR PATH: " + chair_path)
        cad_id_file = open(chair_path + "/id_cad.txt", "r")
        cad_id = cad_id_file.readline()
        print("CAD ID: " + cad_id)
        chair_id_dict[chair_path + "/model_normalized.ply"] = cad_id


