# Created by alanhu at 8/30/23
import sys
import os
from pathlib import Path

# Get the directory of the current script
current_script_directory = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory
parent_directory = os.path.dirname(current_script_directory)

# Append the parent directory to sys.path
sys.path.append(parent_directory)

list_project_folders = ["app", "config", "tests", "log", "documentation"]
list_vcs_folders = ["git", "gitlab", "github", "space"]
list_end_folders = ["Documents", "documents"]
list_source_extension = ['py']
list_documentation_extension = ['md', 'txt', 'pdf', 'docx', 'doc', 'pptx', 'ppt']
list_config_extension = ['json', 'yaml', 'yml', 'ini', 'cfg', 'conf', 'xlsx', 'xls']
list_diagram_extension = ['puml', 'uml', 'svg', 'png', 'jpg', 'jpeg', 'gif', 'bmp', 'tiff', 'tif', 'eps', 'raw',
                          'dot']  # share diagram and picture extensions in the documentation folder
list_log_extension = ['log']

list_file_types = ["source", "documentation", "config", "diagram", "log"]


def search_directories(search_path, search_term):
    for root, dirs, files in os.walk(search_path):
        if search_term in files:
            return root
    return None


def search_files(search_path, search_term):
    for root, dirs, files in os.walk(search_path):
        if search_term in files:
            return files
    return None


class file_organization_module:
    class file_class:
        def __init__(self, file_name, file_extension, file_path, file_size, file_created, file_modified):
            self.file_name = file_name
            self.file_extension = file_extension
            self.file_path = file_path
            self.file_type = ""


def search_main_directory():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    while True:
        # Check if any of the project folders are present in the current directory
        if any(folder in os.listdir(current_directory) for folder in list_project_folders):
            return current_directory

        # Check if we have reached the 'Documents' directory
        if os.path.basename(current_directory) == 'Documents':
            return None

        # Move up the directory hierarchy
        current_directory = os.path.dirname(current_directory)


class pathing_module:
    def __init__(self, path_main_directory=None):
        self.base_path = None
        self.project_folders_dict = {}

        if path_main_directory is None:
            self.pre_search_main_directory()
        else:
            self.base_path = path_main_directory
            self.project_folders_dict["base"] = self.base_path

        # search for existing files first
        # create project folders in the main directory
        self.generate_project_folders(list_project_folders)

    def pre_search_main_directory(self):
        # Get the directory of the current script
        current_directory = os.path.dirname(os.path.abspath(__file__))
        # Search for main directory
        self.base_path = search_main_directory()
        while self.base_path is None:
            self.base_path = search_main_directory()
        else:
            self.base_path = Path(self.base_path)
        # Convert to Path object for easier handling
        self.base_path = Path(self.base_path)
        self.project_folders_dict["base"] = self.base_path

    def generate_project_folders(self, project_folders):

        for project in project_folders:
            path_project = os.path.join(self.base_path, project)
            if not os.path.exists(path_project):
                os.makedirs(path_project)
                # add project folder to dict
                self.project_folders_dict[project] = os.path.join(self.base_path, project)
            else:
                print(f"Project {project} folder already exists!")
    def get_path(self, path_name):

        # get path of project folder
        if path_name in self.project_folders_dict:
            return self.project_folders_dict[path_name]
        # get path of other folders
        else:
            return None

    def set_path(self, path_name: object, path: object) -> object:
        # set path of project folder
        if path_name in self.project_folders_dict:
            self.project_folders_dict[path_name] = path
        # set path of other folders
        else:
            print("Path name not found!")


pathing = pathing_module()
print(pathing.get_path("base"))
print(pathing.get_path("app"))
print(pathing.get_path("config"))
print(pathing.get_path("tests"))
print(pathing.get_path("log"))
