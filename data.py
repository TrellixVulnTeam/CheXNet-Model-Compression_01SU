"""
Python script used for downloading all the datasets used in this
project. 
Data is downloaded to root folder
"""
import academictorrents as at
from torch.utils import data
import tarfile
import os


data_hash_dict = {'NIH': "e615d3aebce373f1dc8bd9d11064da55bdadede0",
                  'RSNA': "95588a735c9ae4d123f3ca408e56570409bcf2a9",
                  'Pad-Chest': "96ebb4f92b85929eadfb16761f310a6d04105797",
                  'Openi': "5a3a439df24931f410fac269b87b050203d9467d"}


def get_nih_data_paths():
    '''
    returns the path to the nih images,
    patient csv file and bbox csv file
    '''
    # path = at.get(data_hash_dict.get('NIH'))
    cwd = os.getcwd()
    path = os.path.join(cwd, "NIH")
    to_path = os.path.dirname(path)
    path_to_tar= os.path.join(path, "images-224.tar")

    with tarfile.open(path_to_tar, 'r') as tar:
            def is_within_directory(directory, target):
                
                abs_directory = os.path.abspath(directory)
                abs_target = os.path.abspath(target)
            
                prefix = os.path.commonprefix([abs_directory, abs_target])
                
                return prefix == abs_directory
            
            def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
            
                for member in tar.getmembers():
                    member_path = os.path.join(path, member.name)
                    if not is_within_directory(path, member_path):
                        raise Exception("Attempted Path Traversal in Tar File")
            
                tar.extractall(path, members, numeric_owner=numeric_owner) 
                
            
            safe_extract(tar, path=to_path)
            tar.close()
    
    x_ray_data_path = os.path.join(path, "Data_Entry_2017.csv")
    bbox_data_path = os.path.join(path, "BBox_List_2017.csv")
    image_path = os.path.join(to_path, "images-224")

    return image_path, x_ray_data_path, bbox_data_path
