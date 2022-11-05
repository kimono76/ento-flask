```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

bash Anaconda3-2022.10-Linux-x86_64.sh -u

conda create--name qimono-virtual python=3.7 -y

conda activate qimono-virtual

pip list

pip install -r requirements.txt

pip install flask

touch server.py

py server.py

python server.py

pip install pymongo

echo 'run this command to enable requests from nightgale'
checknetisolation loopbackexempt -a -p=S-1-15-2-2472482401-1297737560-3464812208-2778208509-1273584065-1826830168-474783446

echo 'install this for making API request from the terminal'
pip install http-prompt

mongod & sleep 5 && cls

```