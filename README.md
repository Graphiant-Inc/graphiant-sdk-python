# Graphiant-SDK-Python

Python SDK for [Graphiant NaaS](https://www.graphiant.com).

Refer [Graphiant Documentation](https://docs.graphiant.com/) to get started with our services.

## Install

Graphiant-SDK package can be installed using pip. Refer [graphiant-sdk](https://pypi.org/project/graphiant-sdk/) package on public PyPi server.

```sh
pip install graphiant-sdk
```

## Build

Steps to build and install Graphiant-SDK package from source code.

### Prerequisites

python version 3.12+

### Create and activate python virtual environment
```sh
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies
```sh
pip install --upgrade pip setuptools wheel
```

### Clone the graphiant-sdk-python repository
```sh
git clone git@github.com:Graphiant-Inc/graphiant-sdk-python.git
```

### Build graphiant-sdk distribution
```sh
cd graphiant-sdk-python
pip install -r requirements.txt
python setup.py sdist bdist_wheel
```

### Install graphiant-sdk locally

Install using the source archive:

```sh
pip install dist/*.tar.gz
```

## Generate

Steps to generate Graphiant-SDK-Python locally using Graphiant API docs. 

```sh
openapi-generator generate -i graphiant_api_docs_v25.6.2.json -g python --git-user-id Graphiant-Inc --git-repo-id graphiant-sdk-python --package-name graphiant_sd
```
Note: Latest version of Graphiant API docs can be downloaded from Graphiant portal under "Support Hub" > "Developer Tools".

## Usage

Refer [graphiant-playbooks](https://github.com/Graphiant-Inc/graphiant-playbooks) repo for usage examples.

## License

Copyright (c) 2025 Graphiant-Inc

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
