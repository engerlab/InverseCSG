import pymesh

INVERSE_CSG_MAIN_DIR = '/home/jonathan/Software/InverseCSG/'
INVERSE_CSG_BUILD_DIR = '/home/jonathan/Software/InverseCSG/build/'

APPLICATOR_DIR = '/workspace/'

APPLICATOR_OFF_DIR = APPLICATOR_DIR + "Applicator_OFF/"


COMPONENTS = ("cyl", "plastic","shield", "overmold")

for component in COMPONENTS:
    #try to center the mesh around the origin
    #bounding_box = mesh.get_attribute("bbox")
    #mesh.add_attribute("bbox")'
    mesh = pymesh.load_mesh( APPLICATOR_OFF_DIR + f"{component}.off")
    bbox_min, bbox_max = mesh.bbox
    #print(bbox)
    mesh_center = 0.5 * (bbox_min + bbox_max)
    mesh_vertices = mesh.vertices.copy()
    mesh_faces = mesh.faces.copy()
    mesh_vertices -= mesh_center
    new_mesh = pymesh.form_mesh(mesh_vertices, mesh_faces)
    pymesh.save_mesh(APPLICATOR_OFF_DIR + f"{component}_centered.off", new_mesh)