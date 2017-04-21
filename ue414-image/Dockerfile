FROM unrealcv/base
ARG github_username
ARG github_password

RUN git clone -b 4.14 https://${github_username}:${github_password}@github.com/EpicGames/UnrealEngine.git
RUN cd UnrealEngine
RUN ./Setup.sh
RUN ./GenerateProjectFiles.sh
RUN make
