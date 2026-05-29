cd day3-4/k8s/extra/load
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python load.py --url http://127.0.0.1:8081/ --users 500 --requests 200000 --delay 0.005




##############
# defaults
python load.py

# custom
python load.py --url http://127.0.0.1:8081/ --users 100 --requests 200 --delay 0.05

# help
python load.py --help
################