import boto3


def get_s3(profile):
    session = boto3.session.Session(profile_name=profile)
    s3 = session.client(
        service_name="s3",
        endpoint_url="https://storage.yandexcloud.net",
        region_name="ru-central1",
    )
    return s3


def get_bucket(s3, bucket):
    buckets = s3.list_buckets()["Buckets"]
    if bucket == "":
        if len(buckets) != 1:
            raise ValueError("Count of buckets is not equal 1")
        bucket = buckets[0]["Name"]
    else:
        if bucket not in [i["Name"] for i in buckets]:
            raise ValueError(f"Bucket '{bucket}' does not exist")
    return bucket
