# nmt-aws

We use a instance AWS EC2 <em>p3.2xlarge</em> instance with the following
that has a Tesla V100-SXM2-16GB. We use the following image:

Deep Learning AMI (Ubuntu 18.04) Version 36.0 - ami-096a6497745975f89


# Steps

## Check Cuda version

Tensorflow requires specific versions of CUDA drives. Check that the CUDA
drives are properly supported by you Tensorflow version.

execute ```./install-cuda.sh``` if it is necessary.

Reboot 

## Install OpenNMT and necessary dependencies

execute ```./install.sh ```

