FROM ubuntu:16.04
# FROM mono
RUN apt-get update
RUN apt-get install -y sudo tzdata
VOLUME /UE4
# If this CMD failed, do it manually
# CMD /UE4/Setup.sh && /UE4/GenerateProjectFiles.sh && cd /UE4 && make

# Configure user account, because UE4 binary will refuse to run as root
RUN useradd unrealcv -m -p ''
# No password for unrealcv account
RUN usermod -aG sudo unrealcv
RUN echo "unrealcv ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
USER unrealcv
RUN sudo apt-get install -y x11-xserver-utils

LABEL com.nvidia.volumes.needed="nvidia_driver"
ENV PATH /usr/local/nvidia/bin:${PATH}
ENV LD_LIBRARY_PATH /usr/local/nvidia/lib:/usr/local/nvidia/lib64:${LD_LIBRARY_PATH}
ENV __GL_SYNC_TO_VBLANK 0
RUN sudo apt-get install -y mesa-utils
