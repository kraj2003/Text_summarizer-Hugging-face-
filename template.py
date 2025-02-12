# 
import os
import pathlib
from pathlib import Path
import logging

logging.basicConfig(format='%(asctime)s,%(msecs)03d %(name)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG)

project_name="text_summarizer"

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/contants/__init__.py",
    "params.yaml", # parameters required for models
    "config/config.yaml", #all the configuration details
    "schema.yaml", # 
    "main.py",
    "Dockerfile",
    "setup.py", #create the entire project as a package
    "research/research.ipynb",
    "templates/index.html","app.py"

]

for file_path in list_of_files:
    file_path=Path(file_path)
    filedir,filename=os.path.split(file_path)

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory {filedir} for the file: {filename} ")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path,"w") as file:
            pass
            logging.info(f"Creating emptyy file {file_path}")

    else:
        logging.info(f" {file_path} already exists")