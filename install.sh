#sudo apt-get update -y
#sudo apt-get upgrade -y
sudo apt-get install zip -y
pip install tensorflow-gpu --ignore-installed wrapt
pip install tensorflow-addons
pip install OpenNMT-tf==2.0.0 --ignore-installed PyYAML


git clone https://github.com/OpenNMT/OpenNMT-py.git
cd OpenNMT-py
git checkout -b 0.9.0

cd ..
mkdir model1
cd model1
git config --global user.name "Jordi Mas"
git config --global user.email jmas@softcatala.org

