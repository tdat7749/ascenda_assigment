#!/bin/bash

python3 main.py $1 $2


# TODO :
#   INSTALL 'request' dependency: python3 -m pip install requests


# RUN examples: 
# - sh runner.sh iJhz,SjyX,f8c9 5432,1122
# - sh runner.sh iJhz,SjyX 5432
# - sh runner.sh f8c9 1122
# - sh runner.sh iJhz,SjyX,f8c9 none
# - sh runner.sh none 5432,1122
# - sh runner.sh none none