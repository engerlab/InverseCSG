import os
import trimesh

INVERSE_CSG_MAIN_DIR = '/home/jonathan/Software/InverseCSG/'
INVERSE_CSG_BUILD_DIR = '/home/jonathan/Software/InverseCSG/build/'

APPLICATOR_DIR = '/home/jonathan/Documents/RectalIMBTApplicator_MeshtoCSG/'

APPLICATOR_OFF_DIR = APPLICATOR_DIR + "Applicator_OFF/"

APPLICATOR_OFF_COARSENED_DIR = APPLICATOR_DIR + "Applicator_OFF_Fixed/"
OUTPUT_DIR = APPLICATOR_DIR + "Applicator_CSG_Trees/"

#COMPONENTS = ("cyl", "plastic","shield", "overmold")
COMPONENTS = ("shield", "overmold")

for component in COMPONENTS:
    #off_file = APPLICATOR_OFF_COARSENED_DIR + f"{component}.off"
    #off_file = APPLICATOR_OFF_DIR + f"{component}.off"
    off_file = APPLICATOR_OFF_DIR + f"{component}_centered.off"
    main_file = INVERSE_CSG_MAIN_DIR + "main.py"
    out_dir = OUTPUT_DIR + component + '/'
    exit_code = os.system(f'python3 {main_file} \
                          --builddir {INVERSE_CSG_BUILD_DIR} \
                          --outdir {out_dir} \
                          --mesh {off_file} \
                          --eps 1\
                           --surfacedensity 50 \
                           --volumedensity 15 \
                           --initsample 200 \
                            ')
    if exit_code != 0:
        print(f"Error processing {off_file}")
        break
    print(f"Processed {off_file}")