# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation')
session
s3 = session.resource('s3')
bucket = s3.create_bucket(Bucket='cheinig-video-recognition', CreateBucketConfiguration={'LocationConstraint': session.region_name})
bucket
from pathlib import Path
get_ipython().run_line_magic('ls', '/Users/christoph/Downloads/*.mp4')
pathname = '/Users/christoph/Downloads/video.mp4'
path = Path(pathname).expanduser().resolve()
print(path)
bucket.upload_file(str(path), str(path.name))
rekognition_client = session.client('rekognition')
response = rekognition_client.start_label_detection(Video={'S3Object': { 'Bucket' : bucket.name, 'Name': path.name}})
response
job_id = response['JobId']
result = rekognition_client.get_label_detection(JobId=job_id)
result
result.keys()
result['JobStatus']
result['ResponseMetadata']
result['VideoMetadata']
result['Labels']
len(result['Labels'])
