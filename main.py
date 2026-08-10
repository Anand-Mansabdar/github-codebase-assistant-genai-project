# from repository.clone_repo import clone_repository
# from repository.file_loader import load_repository_files
# from chunking.splitter import split_file


# repo_path = clone_repository(
#     "https://github.com/Anand-Mansabdar/github-codebase-assistant-genai-project.git"
# )

# files = load_repository_files(repo_path)

# print(f"Files discovered: {len(files)}")

# first_file = files[0]

# chunks = split_file(first_file)

# print(f"Chunks generated: {len(chunks)}")

# for chunk in chunks[:3]:
#     print("\n" + "=" * 80)
#     print(f"File: {chunk.source_file}")
#     print(f"Language: {chunk.language}")
#     print(f"Lines: {chunk.start_line}-{chunk.end_line}")
#     print("=" * 80)
#     print(chunk.content)


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