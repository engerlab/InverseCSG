import json
import pymesh

import json
import itertools
import pymesh

APPLICATOR_DIR = '/workspace/'

applicators_json = json.load(open(APPLICATOR_DIR + "applicators.json"))

for applicator in applicators_json.keys():
    for component in applicators_json[applicator]:
        # Try to center the mesh around the origin
        stl_dir = APPLICATOR_DIR + f"{applicator}/Applicator_STL/"
        off_dir = APPLICATOR_DIR + f"{applicator}/Applicator_OFF/"
        stl_file = stl_dir + f"{component}.stl"
        off_file = off_dir + f"{component}.off"
        mesh = pymesh.load_mesh(stl_file)
        pymesh.save_mesh(off_file, mesh)