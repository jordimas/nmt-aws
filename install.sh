#sudo apt-get update -y
#sudo apt-get upgrade -y
pip install tensorflow-gpu --ignore-installed wrapt
pip install tensorflow-addons
pip install OpenNMT-tf --ignore-installed PyYAML


git clone https://github.com/OpenNMT/OpenNMT-py.git
cd OpenNMT-py
git checkout -b 0.9.0

cd ..
mkdir model1
cd model1

