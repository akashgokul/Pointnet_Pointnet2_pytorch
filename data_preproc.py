import os
import pandas as pd
import open3d as o3d
import numpy as np

ROOTDIR = "/global/scratch/akashgokul/mined_scannet_chairs/"

print("------"*10)
print("This code generates a csv file containing the directory of np pointcloud, np transformed pointcloud, and CAD id.")
print("------"*10)

def transform_pcd(root_dir, pcd_dir, transform_dir):
    pcd = o3d.io.read_point_cloud(pcd_dir)
    transform_matrix = np.load(transform_dir)
    pcd_transformed = pcd.transform(transform_matrix)
    np_pcd = np.asarray(pcd.points)
    np_pcd_transformed = np.asarray(pcd_transformed.points)
    orig_pcd_np_dir = root_dir + '/model_normalized_np'
    transformed_pcd_np_dir = root_dir + '/model_normalized_transformed_np'
    np.save(orig_pcd_np_dir,np_pcd)
    np.save(transformed_pcd_np_dir,np_pcd_transformed)
    return orig_pcd_np_dir, transformed_pcd_np_dir

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

        pointcloud_dir = chair_dir_path + "/model_normalized.ply"
        np_transform_mat_dir = chair_dir_path + "/cad2points_trafo.npy"

        orig_np_dir, transformed_np_dir = transform_pcd(chair_dir_path, pointcloud_dir,np_transform_mat_dir)
        chair_id_dict[chair_dir_path + "/" + orig_np_dir] = [chair_dir_path + "/" + transformed_np_dir,  cad_id]

data = pd.DataFrame.from_dict(chair_id_dict, orient='index')
data_dir = ROOTDIR + "data.csv"
data.to_csv(path_or_buf=data_dir)
print("------"*10)
print("Done! \n Data can be found at: " + data_dir + "/n")


