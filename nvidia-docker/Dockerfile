FROM ubuntu:16.04
RUN apt-get update
RUN apt-get install -y mesa-utils
LABEL com.nvidia.volumes.needed="nvidia_driver"
ENV PATH /usr/local/nvidia/bin:${PATH}
ENV LD_LIBRARY_PATH /usr/local/nvidia/lib:/usr/local/nvidia/lib64:${LD_LIBRARY_PATH}
# from: https://github.com/NVIDIA/nvidia-docker/issues/327
# CMD ["glxgears"]
ENV __GL_SYNC_TO_VBLANK 0
CMD ["__GL_SYNC_TO_VBLANK=0 glxgears"]
