#sudo apt-get update -y
#sudo apt-get upgrade -y
pip install tensorflow==2.3.1
#pip install tensorflow-addons
pip install OpenNMT-tf==2.13.0
sudo apt-get install zip -y


git clone https://github.com/OpenNMT/OpenNMT-py.git
cd OpenNMT-py
git checkout -b 0.9.0

git config --global user.name "Jordi Mas"
git config --global user.email jmas@softcatala.org

bash versions.sh
