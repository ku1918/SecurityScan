import boto3
session = boto3.Session(
    aws_access_key_id='***REMOVED***',
   aws_secret_access_key='***REMOVED***'
)


#Then use the session to get the resource
s3 = session.resource('s3')

s3.Bucket('stackvidhya').upload_file('E:/temp/testfile.txt','file2_uploaded_by_boto3.txt')