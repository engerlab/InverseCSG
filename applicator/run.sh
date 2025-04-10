#!/bin/bash
./scripts/convert_all_meshes_to_off.sh
./scripts/center_all_meshes.sh
python3 ./scripts/convert_off_to_csg.py