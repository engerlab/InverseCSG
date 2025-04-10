import json
import itertools
import pymesh

INVERSE_CSG_MAIN_DIR = '/home/jonathan/Software/InverseCSG/'
INVERSE_CSG_BUILD_DIR = '/home/jonathan/Software/InverseCSG/build/'

APPLICATOR_DIR = '/workspace/'

applicators_json = json.load(open(APPLICATOR_DIR + "applicators.json"))

for applicator in applicators_json.keys():
    for component in applicators_json[applicator]:
        # Try to center the mesh around the origin
        off_dir = APPLICATOR_DIR + f"{applicator}/Applicator_OFF/"
        off_file = off_dir + f"{component}.off"
        mesh = pymesh.load_mesh(off_file)
        bbox_min, bbox_max = mesh.bbox
        mesh_center = 0.5 * (bbox_min + bbox_max)
        
        # Save the transform so we can recover it later
        with open(off_dir + f"{component}_transform.txt", "w") as transform_file:
            transform = f"{mesh_center[0]} {mesh_center[1]} {mesh_center[2]}"
            transform_file.write(transform)
        
        mesh_vertices = mesh.vertices.copy()
        mesh_faces = mesh.faces.copy()
        mesh_vertices -= mesh_center
        new_mesh = pymesh.form_mesh(mesh_vertices, mesh_faces)
        pymesh.save_mesh(off_dir + f"{component}_centered.off", new_mesh)