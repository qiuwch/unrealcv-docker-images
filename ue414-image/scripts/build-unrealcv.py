import os, sys

cmd = 'docker run -it --rm\
    -v {PWD}/unrealcv:/unrealcv \
    -v {PWD}/UnrealEngine:/UE4 \
    -e UE4=/UE4 \
    unrealcv/ue4-dependency \
    /bin/sh -c "cd /unrealcv && ./build.sh"'

cmd = cmd.format(
    PWD = os.path.abspath('.')
)

os.system(cmd)
