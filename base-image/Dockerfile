FROM ubuntu:16.04
RUN apt-get update
RUN apt-get install -y mesa-utils
# RUN apt-get install -y libgl1-mesa-dri
RUN apt-get install -y libgl1-mesa-glx libgl1-mesa-dri
# This is software renderer
ENV vblank_mode 0
CMD ["glxgears"]
# https://askubuntu.com/questions/541343/problems-with-libgl-fbconfigs-swrast-through-each-update
# export LIBGL_DEBUG=verbose
# glxgears
