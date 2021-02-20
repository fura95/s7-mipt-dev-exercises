python3.8 -m venv venv 
PYPI_PASSWORD=$(cat ~/.secrets/pypi_password.b64 | base64 -d )
source ./venv/bin/activate
./venv/bin/pip3 install --upgrade pip --index-url https://nexus.s7.aero/repository/nexus-pypi-proxy/simple
./venv/bin/pip3 install  --index-url https://nexus.s7.aero/repository/nexus-pypi-proxy/simple -r ./requirements.txt
./venv/bin/pip3 install  --index-url https://nexus.s7.aero/repository/nexus-pypi-proxy/simple -r ./host-requirements.txt
