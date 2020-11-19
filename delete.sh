#!/bin/bash
echo Deletes unnecessary files before training
sudo rm -r -f /var/cache/apt/archives/
sudo rm -r -f /usr/local/cuda-11.0
sudo rm -r -f /home/ubuntu/anaconda3/envs/aws_neuron* 
sudo rm -r -f /home/ubuntu/anaconda3/envs/pytor* 
