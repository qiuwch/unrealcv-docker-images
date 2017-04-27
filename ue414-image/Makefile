editor:
	nvidia-docker run -it --rm --env="DISPLAY" --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" -v ${PWD}/UnrealEngine:/UE4 unrealcv/ue4-dependency /UE4/Engine/Binaries/Linux/UE4Editor
	# docker run -it --rm --env="DISPLAY" --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" -v ${PWD}/UnrealEngine:/UE4 unrealcv/ue4-dependency glxgears

build:
	# Download this from dockerhub should be enough
	# After compile the /UE4 folder, it is possible to use it to compile and package further binary and also start the editor within the container
	docker run -it --rm -v ${PWD}/UnrealEngine:/UE4 unrealcv/ue4-dependency make -C /UE4

dependency:
	docker build ./build/ -t base-image
	docker run -it -v ${PWD}/UnrealEngine:/UE4 --name install-runner base-image sudo /UE4/Setup.sh
	docker commit install-runner unrealcv/ue4-dependency
	docker rm install-runner

run-test:
	docker build ./build/ -t base-image
	docker run -it --rm -v ${PWD}/UnrealEngine:/UE4 unrealcv/ue4-dependency bash
