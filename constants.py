
BUILD_COMMAND = "ng build --aot"

PROD_EXPECTED_LIST = ['inline','main','polyfills','scripts','styles','vendor','index','favicon']

EXCLUDE_LIST = []

BRANCH_CONFIG = {
    'PROD': 'production',
    'STAGE': 'staging',
    'DEV': 'master'
}
AWS_CONFIG = {
    'PROD': 'prod',
    'STAGE': 'stage',
    'DEV': 'dev'
}
REQUEST_PARAMS = {
    'PROD':
        {
            'bucketName': 'S3_BUCKET_NAME',
            'repositoryPath': 'CODE_PATH_YOUR_PROJECT',
            'distributionId': 'CLOUDFRONT_DISTRIBUTION_ID',
            'buildCommand' : 'ng build --prod --aot',
            'buildPath' : 'CODE_BUILD_PATH'
        }
}
