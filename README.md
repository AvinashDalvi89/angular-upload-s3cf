[![Build Status](https://travis-ci.com/aviboy2006/angular-upload-s3cf.svg?branch=master)](https://travis-ci.com/aviboy2006/angular-upload-s3cf)
<img src="https://img.shields.io/badge/made%20with-python-blue.svg" alt="made with python">
<img src="https://img.shields.io/github/license/mashape/apistatus.svg" alt="MIT License">

# Angular Build Upload to AWS S3 + CloudFront 🚀🚀🚀

This will help to automated uploading Angular project build code to AWS S3 and CloudFront cached invalidation part. This will ensure to take backup of existing code for rollback operation if required.

![Feature Image](https://repository-images.githubusercontent.com/288531197/2da1e700-099e-11eb-84a9-d7167fd15c44)

## Prerequisites  ![to-do-list](https://user-images.githubusercontent.com/3996105/95450050-4fda3b80-0983-11eb-8e43-4d98a4f77101.png)

* `python3`  - You can use `python2.x` also you need to modify `print` function calls
* `pip` - installation of other dependant `python`library 
* `boto3` - `pip3 install boto3`  or `pip install boto3`
* [pygit2](https://pypi.org/project/pygit2/0.16.2/) - Fetch repository update and merge inside project.
* `mimetypes`
* `aws-cli` - to configure `aws creditional` basesd on environment specific 

## Installation  ![installation-symbol (1)](https://user-images.githubusercontent.com/3996105/95449955-21f4f700-0983-11eb-9564-39465aee2f49.png)

* You can download or clone repository for installation purpose. 
* Make sure install prerequisites
* Can run unitest file by changing values or can create separate python file and follow "How to use" section.

## How to use  ![guide](https://user-images.githubusercontent.com/3996105/95450176-8748e800-0983-11eb-9b98-402512a35228.png)

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
