# python bot_criador.py --path ./files
import os
import argparse
import random

parser = argparse.ArgumentParser(
    description="Create random docs"
)

parser.add_argument(
    "--path",
    type=str,
    default=".",
    help="Directory path where the docs will be created",
)

# parse the arguments given by the user and extract the path
args = parser.parse_args()
path = args.path

print(f"Creating docs in {path}")

# get all files from given directory
dir_content = os.listdir(path)

# create a relative path from the path to the file and the document name
path_dir_content = [os.path.join(path, doc) for doc in dir_content]

# filter our directory content into a documents and folders list
docs = [doc for doc in path_dir_content if os.path.isfile(doc)]
folders = [folder for folder in path_dir_content if os.path.isdir(folder)]

# counter to keep track of amount of created files 
# and list of already created docs to avoid multiple creations
created = 0
created_docs = []
doc_names = ["lightning", "foggy", "gear", "eclipse", "vibrant", "pinwheel", "spontaneous", "maze", "fragment", "dew", "horizon", "intriguing", "maritime", "abstract", "enigmatic"]
doc_types = ["html", "css", "js", "cs"]

# create the files according to the name and type list
while created <= 10:
    full_name = random.choice(doc_names)+"."+random.choice(doc_types)

    # includes a path to the files, otherwise they would be created in the same folder
    # select the path in the command or line 13
    doc_path = os.path.join(path, full_name)

    if doc_path not in created_docs:
        f = open(doc_path, "w")
        created_docs.append(doc_path)
        print(f"Doc {doc_path} created.")  
        created += 1

print(f"Created {created} files.")