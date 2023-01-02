#! /bin/bash

# update and install requirements
sudo apt update -y
sudo apt install -y gvfs snapd libllvm6.0 subversion
sudo snap install blender --classic

# alias our snap-blender to "blender"
alias blender=/snap/bin/blender

# this ends up being used as a "/tmp"
sudo mkdir -p /run/user/1000/gvfs


