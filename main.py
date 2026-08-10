from repository.clone_repo import clone_repository
from repository.file_loader import load_repository_files
from chunking.splitter import split_file
from parsing.parser import analyze_file


repo_path = clone_repository(
    "https://github.com/Anand-Mansabdar/github-codebase-assistant-genai-project.git"
)

files = load_repository_files(repo_path)
python_files = [
    file
    for file in files
    if file.language == "Python"
]

structure = analyze_file(python_files[0])

print(structure)



from parsing.parser import parse_source, walk_tree, extract_functions, extract_classes


source = """
import os
import json


class UserService:

    def create_user(self, username):
        return username

    def delete_user(self, username):
        return True


def helper_function():
    print("Hello")
"""


tree = parse_source(
    source,
    "Python",
)

root = tree.root_node

print(root.type)
print(root.start_point)
print(root.end_point)

print(tree.root_node)

for child in tree.root_node.children:
    print(
        child.type,
        child.start_point,
        child.end_point,
    )
    

for node in walk_tree(tree.root_node):
    print(node.type)
    
    
functions = extract_functions(tree)
for function in functions:
    print(function)
    
classes = extract_classes(tree)
for c in classes:
    print(c)