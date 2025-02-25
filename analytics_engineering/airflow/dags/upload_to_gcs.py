from google.cloud import storage


def upload_to_gcs(bucket, object_name, local_file):

    # Workaround for uploading large files to GCS
    storage.blob._MAX_MULTIPART_SIZE = 5 * 1024 * 1024  # 5MB
    storage.blob._DEFAULT_CHUNKSIZE = 5 * 1024 * 1024  # 5MB

    client = storage.Client()
    bucket = client.bucket(bucket)
    blob = bucket.blob(object_name)
    blob.upload_from_filename(local_file)
