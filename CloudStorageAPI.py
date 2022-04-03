import os
from pprint import pprint
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\Oleg\GCP\MyAccount_Keys\pandasproject01-79e0dccd2add.json'

storage_client = storage.Client()

bucket_name = 'example_bucket_0101'

## Create a new bucket
bucket = storage_client.bucket(bucket_name)

bucket.storage_class = 'COLDLINE' # Archive | Nearline | Standard
#bucket.location = 'US' # Taiwan
bucket = storage_client.create_bucket(bucket, location='US') # returns Bucket object

## Bucket detail
#pprint(vars(bucket))
print('Bucket detail')
print(bucket.name) #example_bucket_0101
print(bucket._properties['selfLink']) #US
print(bucket._properties['id']) #2022-03-12T23:21:36.508Z
print(bucket._properties['location']) #COLDLINE
print(bucket._properties['timeCreated']) #2022-03-12T23:21:36.508Z
print(bucket._properties['storageClass']) #2022-03-12T23:21:36.508Z
print(bucket._properties['timeCreated']) #
print(bucket._properties['updated']) #

#second option
def create_bucket(bucket_name):
    storage_client = storage.Client()
    bucket = storage_client.create_bucket(bucket_name, location='EUROPE-WEST1')
    print("Bucket {} created".format(bucket.name))

## Accessing specific bucket. Get Bucket

my_bucket = storage_client.get_bucket(bucket_name)
pprint(vars(my_bucket))

"""
Upload File instead of ##
"""
print('Upload File')
def upload_to_bucket(blob_name, file_path, bucket_name):
    '''
    Upload file to a bucket
    : blob_name  (str) - object name
    : file_path (str)
    : bucket_name (str)
    '''
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.upload_from_filename(file_path)
        return True
    except Exception as e:
        print(e)
        return False

file_path = r'C:\Users\ruchinskyo\OneDrive - Dun and Bradstreet\Desktop\Json Test'

# upload to blob named 'Json List 01'
upload_to_bucket('Json List 01', os.path.join(file_path,'1.json'),'example_bucket_0101')
# upload to subfolder 'document/2.json'
upload_to_bucket('document/2.json', os.path.join(file_path,'2.json'),'example_bucket_0101')


"""
List All Blobs 
"""
print('List All Blobs')
def list_blobs(bucket_name):
    """Lists all the blobs in the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)

    blobs = bucket.list_blobs()

    for blob in blobs:
        print(blob.name)

"""
Download File By Blob Name
"""
print('Download File By Blob Name')
def download_file_from_bucket(blob_name, file_path, bucket_name):
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        with open(file_path, 'wb') as f:
            storage_client.download_blob_to_file(blob, f)
        return True
    except Exception as e:
        print(e)
        return False

bucket_name='example_bucket_0101'
download_file_from_bucket('Json List 01', os.path.join(os.getcwd(), 'file1.json'), bucket_name)
download_file_from_bucket('document/2.json', os.path.join(file_path, 'file2.json'), bucket_name)


# download_file_from_bucket('Voice List', r'H:\PythonVenv\GoogleAI\Cloud Storage\Voice List.csv', bucket_name)


"""
Download File By Passing URI Path
"""
def download_file_uri(uri, file_path):
    with open(file_path, 'wb') as f:
        storage_client.download_blob_to_file(uri, f)
    print('Saved')

uri = 'gs://<uri>'
# download_file_uri(uri, r'H:\PythonVenv\GoogleAI\Cloud Storage\Voice List2.csv')



"""
List Buckets
list_buckets(max_results=None, page_token=None, prefix=None, projection='noAcl', fields=None, project=None, timeout=60, retry=<google.api_core.retry.Retry object>)
"""
for bucket in storage_client.list_buckets(max_results=100):
    print(bucket)

