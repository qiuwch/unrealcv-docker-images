The docker images of unrealcv are used to solve three challenges.

1. How to use UnrealCV binaries easily in a Linux server
2. How to run UE4 editor with the installation of a lot of dependencies
3. How to automatically run tests of UnrealCV

Usage
=====

:code:`make all` to make all images.

:code:`make run-nvidia` to start nvidia container. Make sure `nvidia-docker` has been installed.

:code:`make run-intel` to start Intel container

Run RealisticRendering demo
===========================

In host:

:code:`make run-nvidia`

In container

:code:`sh ./run-rr.sh`

Images
======

- base: Basic tools and configuration
- intel: For intel GPU
- nvidia: For nvidia GPU
