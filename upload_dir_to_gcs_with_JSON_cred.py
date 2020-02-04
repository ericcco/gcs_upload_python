import os
from google.cloud import storage

#change "rootdir" and "bucket_name" for your specific values
rootdir = '[YOUR_DIRECTORY]/'
bucket_name = '[BUCKET_NAME]'
 
def upload_blob(source_file_name, destination_blob_name):
 
    storage_client = storage.Client.from_service_account_json('[SERVICE_ACCOUNT_KEY.JSON')
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
 
    blob.upload_from_filename(source_file_name)
 
    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )
 
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        upload_blob(os.path.join(subdir, file), os.path.join(subdir, file))
        print(os.path.join(subdir, file))
