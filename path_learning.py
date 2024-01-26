# base research/ path
import os
path = os.path.dirname(__file__)
print(path)
path_to_artifacts = path + "research/"
print(path_to_artifacts)

# get relative path for research/ folder

path = os.path.dirname(__file__)
path_to_artifacts = path + "/research/"
print(path_to_artifacts)