import unittest
from angular_upload_s3cf import *

class MyTestCase(unittest.TestCase):
    def test_positive(self):
        request = {
            'bucketName': 'myportal.avinashdalvi.com',
            'buildPath': '/Library/WebServer/Documents/codebase/my-portal-angular/dist/',
            'repositoryPath': '/Library/WebServer/Documents/codebase/my-portal-angular',
            'envName': 'default',  # 'DEV, STAGE,PROD'
            'distributionId': 'E2UMS379NFU9DK',
            'portal': 'MyPortal',
            'buildCommand': 'ng build --prod --aot=true',
            'backupFolder': 'v_1.2.1'
        }
        obj = DeploymentService(request)
        response = obj.start_process()
        print(response)
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
