import os
import pandas as pd
import open3d as o3d
import numpy as np

ROOTDIR = "/global/scratch/akashgokul/mined_scannet_chairs/"

print("------"*10)
print("This code generates a csv file containing the directory of np pointcloud, np transformed pointcloud, and CAD id.")
print("------"*10)

def transform_pcd(root_dir, ply_dir):
    mesh = o3d.io.read_triangle_mesh(ply_dir)
    obj_dir = root_dir + "model.obj"
    o3d.io.write_triangle_mesh(root_dir + "model.obj", mesh)
    print(obj_dir)

chair_id_dict = {}
i = 0
number_of_chair_cad_models = 236778 #from shapenet
scenes = os.listdir(ROOTDIR)
for scene in scenes:
    i += 1
    print("Processing Scene: " + str(i) + " / " + str(len(scenes)))
    for chair_dir in os.listdir(ROOTDIR + "/" + scene):
        chair_dir_path = ROOTDIR + scene + "/" + chair_dir
        chair_dir_contents = os.listdir(chair_dir_path)
        cad_id_file = open(chair_dir_path + "/id_cad.txt", "r")
        cad_id = cad_id_file.readline()

        ply_dir = chair_dir_path + "/model_normalized.ply"
        transform_pcd(chair_dir_path, ply_dir)
        #chair_id_dict = 
        

# data = pd.DataFrame.from_dict(chair_id_dict, orient='index')
# data_dir = ROOTDIR + "data.csv"
# data.to_csv(path_or_buf=data_dir)
# print("------"*10)
# print("Done! \n Data can be found at: " + data_dir)


