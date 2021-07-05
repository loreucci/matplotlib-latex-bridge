#!/bin/bash

# make sure to be in the example folder
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
pushd $SCRIPT_DIR > /dev/null

# find all dirs
for d in $(find . -mindepth 1 -maxdepth 1 -type d); do

    echo $d

    cd $d

    # generate images
    python generate_images.py

    # silently generate pdf
    pdflatex *.tex > /dev/null

    # copy pdf and delete auxiliary files
    cp *.pdf ..
    rm *.aux *.log *.pdf *.png

    cd ..

done

popd > /dev/null