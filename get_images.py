import os
import gdown
import shutil
import zipfile

folder_url = input("Enter URL: ")

destination_directory = 'code'

def download_folder(folder_url, destination_directory):
    zip_file_path = os.path.join(destination_directory, 'folder.zip')
    gdown.download(folder_url, zip_file_path, quiet=False)    
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(destination_directory)    
    os.remove(zip_file_path)   

download_folder(folder_url, destination_directory)