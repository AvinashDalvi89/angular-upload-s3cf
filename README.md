[![Build Status](https://travis-ci.com/aviboy2006/angular-upload-s3cf.svg?branch=master)](https://travis-ci.com/aviboy2006/angular-upload-s3cf)
<img src="https://img.shields.io/badge/made%20with-python-blue.svg" alt="made with python">

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
pythonrequest = {
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
