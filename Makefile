run-nvidia: nvidia-image
	nvidia-docker run -it --rm --env="DISPLAY" --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
unrealcv/nvidia
# https://askubuntu.com/questions/541343/problems-with-libgl-fbconfigs-swrast-through-each-update

run-intel: intel-image
	# docker run --rm unrealcv/base
	docker run -it --rm --env="DISPLAY" --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
--device=/dev/dri:/dev/dri --privileged unrealcv/base
	# This one uses intel graphics card

.PHONY: all base-image nvidia-image intel-image rr-image ue414-image
# The order matters
all: base-image rr-image nvidia-image intel-image

base-image:
	docker build base-image -t unrealcv/base

nvidia-image:
	docker build nvidia-image -t qiuwch/nvidia

intel-image:
	docker build intel-image -t unrealcv/intel

rr-image:
	docker build rr-image -t unrealcv/rr
