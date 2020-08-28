#!/usr/bin/env python
"""
    File            : deployement.py
    Package         :
    Description     :
    Created by Avinash on 18/09/2019
"""


from angular_upload_s3cf import *

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
