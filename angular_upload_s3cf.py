#!/usr/bin/env python
"""
    File 	        : angular_upload_s3cf.py
    Package         : angular_upload_s3cf
    Description     : A Python package to upload Angular build to S3 along with CloudFront
    Created by Avinash on 25/07/2020
"""

# git checkout production
# git fetch origin
# git merge origin/production
# ng build --prod --aot=false 
# ng build --configuration=production
# take bakup file of
# inline.*
# main.*
# polyfills.*
# scripts.*
# styles.*
# vendor.*
# create folder "backup_current date"  -- backup_18092019. - optional step for rollback deployment.
# cut this above files and paste into backup folder
# Copy files from "dist" folder all files and paste into root folder

import os
import random
import string
import subprocess
import datetime
import boto3
from constants import *
import traceback
#from pygit2 import Repository
import mimetypes
import traceback


class DeploymentService():

    def __init__(self,request):
        self.bucket_name = request.get('bucketName')
        self.env = request.get('envName')
        self.build_path = request.get('buildPath')
        self.repo_path = request.get('repositoryPath')
        self.connect_aws()
        self.distribution_id = request.get('distributionId')
        self.portal = request.get('portal')
        self.build_command = request.get('buildCommand')
        if request.get('expectedList'):
            self.expected_list = request.get('expectedList')
        else:
            self.expected_list = PROD_EXPECTED_LIST

        if request.get('excludeList'):
            self.exclude_list = request.get('excludeList')
        else:
            self.exclude_list = EXCLUDE_LIST

    def get_file_name(self,input):
        return input.split('/')[-1]

    def get_folder_name(self,input):
        return input.split('/')[-2]

    def connect_aws(self):
        self.aws_session = boto3.Session(profile_name=AWS_CONFIG.get(self.env))
        self.s3_client = self.aws_session.client('s3')
        self.s3_resource = self.aws_session.resource('s3')

    def start_process(self):

        try:
            folder_list, file_list = list_object = self.list_objects()
            backup_folder_name = "backup_"+ datetime.datetime.now().strftime("%d%m%Y")
            if backup_folder_name not in folder_list:
                self.s3_client.put_object(Bucket=self.bucket_name, Key=(backup_folder_name + '/'))

            for file in file_list:
                file_header_name = file.split(".")
                print(file_header_name)
                '''
                TODO Add exclusion of file
                can exclude those files which not required to push every time 
                using expected_list and exclude_list
                '''
                #if file_header_name[0] in self.expected_list and file_header_name[0]
                # not in self.exclude_list.get(self.portal):
                copy_source = {'Bucket': self.bucket_name, 'Key': file}
                self.s3_client.copy_object(CopySource=copy_source, Bucket=self.bucket_name, Key=backup_folder_name+"/"+file)
                self.s3_client.delete_object(Bucket=self.bucket_name, Key=file)

            self.create_build()
            self.upload_build()
            self.clear_cache_invalidation(self.distribution_id)
            return {
                "status": 200,
                "message": "Build Successfully Uploaded to S3 and CloudFront"
            }
        except Exception as e:
            print(e)
            traceback.print_exc()
            return {
                "status": 500,
                "message": "Build Failed for more details check console output"
            }

    def list_objects(self):
        list_object = self.s3_client.list_objects_v2(Bucket=self.bucket_name)

        file_array = []
        #print(list_object)
        folder_array = []

        if 'Contents' in list_object.keys():
            for list in list_object['Contents']:
                # print list
                if "/" in list.get('Key'):
                    folder_name = self.get_folder_name(list.get('Key'))
                    folder_array.append(folder_name)
                else:
                    file_name = self.get_file_name(list.get('Key'))
                    file_array.append(file_name)

        print(folder_array)
        print(file_array)
        return folder_array,file_array

    def create_build(self):
        pwd = self.repo_path
        os.chdir(pwd)
        print("Build starting...")
        build_pwd = self.build_path
        os.chdir(build_pwd)

        print("Running %s" % self.build_command)
        os.system(self.build_command)
        print("Build Completed...")

    def upload_build(self):
        try:
            print("Uploading code to S3 is in progress...")
            root_path = self.build_path
            print(root_path)
            image_dir = False
            for root, dirs, files in os.walk(root_path):
                #print(root)
                #print(files)
                for file in files:
                    folder_path = root.split("/dist/")[1]

                    s3_file = os.path.join(folder_path, file)
                    print("Uploading file : %s" % s3_file)
                    read_mime_types = mimetypes.guess_type(s3_file)

                    if read_mime_types[0]:
                        content_type = read_mime_types[0]
                    else:
                        content_type = 'binary/octet-stream'

                    self.s3_client.upload_file(os.path.join(root, file), self.bucket_name, s3_file,ExtraArgs={'ContentType':content_type})

            print("Code uploaded successfully!")

        except Exception as err:
            print(err)

    def clear_cache_invalidation(self,distribution_id):
        unique_time_stamp = datetime.datetime.timestamp(datetime.datetime.now())
        print(unique_time_stamp)
        client = self.aws_session.client('cloudfront')
        try:
            response = client.create_invalidation(
                DistributionId= distribution_id,
                InvalidationBatch={
                    'Paths': {
                        'Quantity': 2,
                        'Items': [
                            '/*','/index.html'
                        ]
                    },
                    'CallerReference': str(unique_time_stamp)
                }
            )
            if response.get('ResponseMetadata').get('HTTPStatusCode') == 201 or response.get('HTTPStatusCode') == 200:
                print("Invalidation Request Initiated...")
                print('To check status go to invalidation tab.')
            #print(response)
        except Exception as err:
            print(err)
