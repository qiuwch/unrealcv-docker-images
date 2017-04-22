FROM ubuntu:16.04
RUN apt-get update
RUN apt-get install -y wget tmux sudo unzip vim git aptitude
RUN apt-get install -y mesa-utils x11-xserver-utils

# Configure python
RUN apt-get install -y python python-pip
RUN pip install --upgrade pip
# The ipython from pip is newer than the ubuntu version
RUN pip install ipython
RUN pip install unrealcv
# Fix the issue that ipython is not in ${PATH}
RUN ln -s /usr/local/bin/ipython /usr/bin/ipython

# Configure user account, because UE4 binary will refuse to run as root
RUN useradd unrealcv -m -p ''
# No password for unrealcv account
RUN usermod -aG sudo unrealcv
RUN echo "unrealcv ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

USER unrealcv
WORKDIR /home/unrealcv
COPY *.sh /home/unrealcv/
COPY .tmux.conf /home/unrealcv/

CMD ["tmux"]
