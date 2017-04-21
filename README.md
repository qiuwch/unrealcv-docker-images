## Usage
`make all` to make all images.

`make run-nvidia` to start nvidia container. Make sure `nvidia-docker` has been installed.

`make run-intel` to start Intel container

## Run RealisticRendering demo

In host:

`make run-nvidia`

In container

`sh ./run-rr.sh`

## Images

- base: Basic tools and configuration
- intel: For intel GPU
- nvidia: For nvidia GPU
