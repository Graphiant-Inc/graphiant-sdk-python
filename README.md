## Build & Install the GRAPHIANT-SDK-PYTHON

This guide explains how to build and install the GRAPHIANT-SDK-PYTHON.

---

### Install Python 3.12+

### Create and activate python virtual environment
```sh
python3.12 -m venv venv
source venv/bin/activate
```

### Install the requirement packages
```sh
pip install --upgrade pip setuptools wheel
```

### Clone the graphiant-sdk-python repo
```sh
git clone git@github.com:Graphiant-Inc/graphiant-sdk-python.git
```

### Build the SDK Distribution
```sh
cd graphiant-sdk-python/client
python setup.py sdist bdist_wheel
```

This will create the below files,
- dist/swagger_client-&lt;version&gt;.tar.gz
- dist/swagger_client-&lt;version&gt;-py3-none-any.whl

### Install the SDK locally

Install using the source archive:

```sh
pip install dist/*.tar.gz
```
