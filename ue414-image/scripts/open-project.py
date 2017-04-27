import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('project_file')

args = parser.parse_args()

path = args.project_file
folder = os.path.dirname(path)
filename = os.path.basename(path)

cmd = 'nvidia-docker run -it --rm\
    --env="DISPLAY" --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    -p 9000:9000 \
    -v {PWD}/scripts:/scripts \
    -v {PWD}/UnrealEngine:/UE4 \
    -v {folder}:/project \
    unrealcv/ue4-dependency \
    /UE4/Engine/Binaries/Linux/UE4Editor /project/{filename}'

cmd = cmd.format(
    PWD = os.path.abspath('.'),
    folder = folder,
    filename = filename,
)
print(cmd)
os.system(cmd)
