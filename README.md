[![Build Status](https://travis-ci.com/aviboy2006/angular-build-upload-s3-cloudfront.svg?branch=master)](https://travis-ci.com/aviboy2006/angular-build-upload-s3-cloudfront)
# Angular Build Upload to AWS S3 + Cloudfront

This will help to automated uploading Angular project build code to AWS S3 and CloudFront cached invalidation part. This will ensure to take backup of existing code for rollback operation if required.

## Installation

`pip` is not available. You can download or clone repository for installation purpose. 


## Prerequisites

* `python3`  - You can use `python2.x` also you need to modify `print` function calls
* `pip` - installation of other dependant `python`library 
* `boto3` - `pip3 install boto3`  or `pip install boto3`
* [pygit2](https://pypi.org/project/pygit2/0.16.2/) - Fetch repository update and merge inside project.
* `mimetypes`
* `aws-cli` - to configure `aws creditional` basesd on environment specific 

## Usage

```python
from deployment_angular_s3_cloudfront import *

from constants import REQUEST_PARAMS

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--env', help="Select Environment PROD/STAGE/DEV")
parser.add_argument('--codepath', help="Code path of UI code")
parser.add_argument('--buildpath', help="Build path of UI code")
args = parser.parse_args()
if args.env:
    env = args.env
else:
    env = "STAGE"
if args.codepath:
    code_path = args.codepath
else:
    code_path = REQUEST_PARAMS.get(env).get('repositoryPath')

if args.buildpath:
    build_path = args.buildpath
else:
    build_path = REQUEST_PARAMS.get(env).get('buildPath')

print("Starting process for %s environment" %env)
request = {
    'bucketName': REQUEST_PARAMS.get(env).get('bucketName'), 
    'buildPath': build_path,
    'repositoryPath': code_path,
    'envName':  env,  # 'DEV, STAGE,PROD'
    'distributionId': REQUEST_PARAMS.get(env).get('distributionId'),
    'portal': 'PROJECTNAME',
    'buildCommand': REQUEST_PARAMS.get(env).get('buildCommand')
}
obj = DeploymentService(request)
obj.start_process()
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
