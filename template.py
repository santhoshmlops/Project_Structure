import os
from pathlib import Path
import logging

logging.basicConfig(
    level= logging.INFO,
    filename="template_structure.log",
    filemode='w',
    format= '%(asctime)s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S'
)

while True:
    Project_name = input("Enter your project name: ")
    if Project_name !='':
        break

logging.info(f"Creating project by name: {Project_name}")

list_of_files = [
    f"src/{Project_name}/__init__.py",
    f"src/{Project_name}/components/__init__.py",
    f"src/{Project_name}/components/data_ingestion.py",
    f"src/{Project_name}/components/data_transformation.py",
    f"src/{Project_name}/components/model_trainer.py",
    f"src/{Project_name}/components/model_evaluation.py",
    f"src/{Project_name}/components/model_pusher.py", 
    f"src/{Project_name}/configuration/__init__.py",
    f"src/{Project_name}/configuration/config.py",
    f"src/{Project_name}/constant/__init__.py",
    f"src/{Project_name}/entity/__init__.py",
    f"src/{Project_name}/entity/artifact_entity.py",
    f"src/{Project_name}/entity/config_entity.py",
    f"src/{Project_name}/pipeline/__init__.py",
    f"src/{Project_name}/pipeline/predict_pipeline.py",
    f"src/{Project_name}/pipeline/train_pipeline.py",
    f"src/{Project_name}/exception/__init__.py",
    f"src/{Project_name}/exception/exception.py",
    f"src/{Project_name}/logger/__init__.py",
    f"src/{Project_name}/logger/logger.py",
    f"src/{Project_name}/utils/__init__.py",
    f"src/{Project_name}/utils/utils.py",
    "notebook/project.ipynb",
    "setup.py",
    "requirements.txt",
    "app.py",
    "main.py"
]

for filepath in list_of_files:
    filepath = Path(filepath) 
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath) or (os.path.getsize(filepath) == 0)):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")

logging.info("Project Structure is completed") 
