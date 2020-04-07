import os
import pandas
import open3d as o3d
import numpy as np

ROOTDIR = "/global/scratch/akashgokul/mined_scannet_chairs/"

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
number_of_chair_cad_models = 236778 #from shapenet
for root, scene_paths, filenames in os.walk(ROOTDIR):
    for scene_path in scene_paths:
        for chair_dir in os.listdir(root + scene_path):
            chair_dir_path = root + scene_path + "/" + chair_dir
            chair_dir_contents = os.listdir(chair_dir_path)
            cad_id_file = open(chair_dir_path + "/id_cad.txt", "r")
            cad_id = cad_id_file.readline()
            pointcloud_dir = chair_dir_path + "/model_normalized.ply"
            np_transform_mat_dir = chair_dir_path + "/cad2points_transfo.npy"
            orig_np_dir, transformed_np_dir = transform_pcd(chair_dir_path, pointcloud_dir,np_transform_mat_dir)
            chair_id_dict[chair_dir_path + "/" + orig_np_dir] = [chair_dir_path + "/" + transformed_np_dir,  cad_id]


