#!/bin/bash
for part in plastic shield overmold; do
    input_path="/workspace/Applicator_OFF/${part}.off"
    output_path="/workspace/Applicator_OFF_Fixed/${part}.off"
    detail="high"
    docker run -it -v /home/jonathan/Documents/RectalIMBTApplicator_MeshtoCSG:/workspace pymesh/pymesh python /workspace/fix_mesh.py --detail "$detail" "$input_path" "$output_path"
done
