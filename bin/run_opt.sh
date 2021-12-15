#!/bin/bash

source setup.sh

export PYTHONPATH=$PYTHONPATH:/w/hallb-scshelf2102/clas12/users/costantini/RICH_alignment/

python scripts/gp_minimize.py spaces/space.yaml 1 test

swif -output