

nvidia-run: nvidia-image
	nvidia-docker run -it --rm --env="DISPLAY" --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
unrealcv/nvidia
# https://askubuntu.com/questions/541343/problems-with-libgl-fbconfigs-swrast-through-each-update

run: base-image
	# docker run --rm unrealcv/base
	docker run -it --rm --env="DISPLAY" --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
--device=/dev/dri:/dev/dri --privileged unrealcv/base
	# This one uses intel graphics card

base-image: ./base-image/Dockerfile
	docker build base-image -t unrealcv/base

nvidia-image: ./nvidia-docker/Dockerfile
	docker build nvidia-docker -t unrealcv/nvidia
