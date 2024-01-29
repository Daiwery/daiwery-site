import boto3
import sys
import threading
import os


def get_s3(profile):
    session = boto3.session.Session(profile_name=profile)
    s3 = session.client(
        service_name="s3",
        endpoint_url="https://storage.yandexcloud.net",
        region_name="ru-central1",
    )
    return s3


def get_bucket(s3, bucket):
    if bucket == "":
        buckets = s3.list_buckets()["Buckets"]
        if len(buckets) != 1:
            raise ValueError("Count of buckets is not equal 1")
        bucket = buckets[0]["Name"]
    return bucket


class ProgressUploadPercentage(object):
    def __init__(self, filename):
        self._filename = filename
        self._size = float(os.path.getsize(filename))
        self._seen_so_far = 0
        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        # To simplify, assume this is hooked up to a single filename
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            s = "\r%s  %s / %s  (%.2f%%)" % (
                self._filename, self._seen_so_far, int(self._size), percentage
            )
            sys.stdout.write(s)
            sys.stdout.flush()
