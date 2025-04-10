import os
import json

INVERSE_CSG_MAIN_DIR = '/home/jonathan/Software/InverseCSG/'
INVERSE_CSG_BUILD_DIR = '/home/jonathan/Software/InverseCSG/build/'

APPLICATOR_DIR = '/home/jonathan/Software/InverseCSG/applicator/'

APPLICATOR_OFF_DIR = APPLICATOR_DIR + "Applicator_OFF/"



applicators_json = json.load(open(APPLICATOR_DIR + "applicators.json"))

for applicator in applicators_json.keys():
    for component in applicators_json[applicator]:
        main_file = INVERSE_CSG_MAIN_DIR + "main.py"
        off_dir = APPLICATOR_DIR + f"{applicator}/Applicator_OFF/"
        off_file = off_dir +  f"{component}_centered.off"
        out_dir = APPLICATOR_DIR +  f"{applicator}/csg/{component}/"
        exit_code = os.system(f'python3 {main_file} \
                            --builddir {INVERSE_CSG_BUILD_DIR} \
                            --outdir {out_dir} \
                            --mesh {off_file} \
                            --eps 0.01\
                            --surfacedensity 50 \
                            --volumedensity 15 \
                            --initsample 200 \
                            --seg 2 \
                                ')
        if exit_code != 0:
            print(f"Error processing {off_file}")
            break
        print(f"Processed {off_file}")