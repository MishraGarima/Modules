#Python Code for Accessing AWS S3 storage

import boto3
import os
from dotenv import load_dotenv

load_dotenv()

s3 = boto3.resource(service_name="s3",
        region_name=os.getenv("region_name"),
        aws_access_key_id=os.getenv("aws_access_key_id"),
        aws_secret_access_key=os.getenv("aws_secret_access_key"), verify=False)

#print all bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

#view all object keys within the specified bucket
bucket = s3.Bucket('bucket_name')
for obj in bucket.objects.all():
    print(obj.key)

#get file from bucket
bucket.download_file("source_file", "destination_file")
#source_file example: x/y/z.extension similarly insert destination_file