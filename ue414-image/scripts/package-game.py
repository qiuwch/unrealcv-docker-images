import os, sys, shutil
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('project_file')
parser.add_argument('--output', default='./output')
parser.add_argument('--no-unrealcv', action='store_true')

args = parser.parse_args()
if not os.path.isdir(args.output):
    print('Output folder "%s" does not exist' % args.output)
    sys.exit(-1)
output_folder = args.output
output_folder = os.path.abspath(output_folder)

path = args.project_file
project_folder = os.path.dirname(path)
project_filename = os.path.basename(path)

if not args.no_unrealcv:
    print('Copy unrealcv to project folder')
    if not os.path.isdir(os.path.join(project_folder, 'Plugins')):
        shutil.copytree('unrealcv/Plugins', os.path.join(project_folder, 'Plugins'))

cmd = 'docker run -it --rm\
    -v {PWD}/scripts:/scripts \
    -v {PWD}/UnrealEngine:/UE4 \
    -v {project_folder}:/project \
    -v {output_folder}:/output \
    unrealcv/ue4-dependency \
    /UE4/Engine/Build/BatchFiles/RunUAT.sh BuildCookRun \
    -project=/project/{project_filename} \
    -archivedirectory=/output \
    -noP4 -platform=Linux -clientconfig=Development -serverconfig=Development -allmaps -stage -pak -archive -cook -build \
    '

cmd = cmd.format(
    PWD = os.path.abspath('.'),
    project_folder = project_folder,
    project_filename = project_filename,
    output_folder = output_folder
)

print(cmd)
os.system(cmd)
