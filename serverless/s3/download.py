from core import *
import argparse
from pathlib import Path
import os
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument("profile", help="The profile from .aws/credentials")
parser.add_argument(
    "-bucket", default="",
    help="The name of the bucket (default: a single bucket is selected)"
)
parser.add_argument(
    "-dir", default=".",
    help="The parent directory for files (default: current directory)"
)
parser.add_argument(
    "keys", nargs="+",
    help="The keys of the objects to download"
)
args = parser.parse_args()
args.dir = os.path.abspath(args.dir)

# Calculate unique directories.
dirs = []
for key in args.keys:
    path = Path(key)
    if args.dir != "":
        path = Path(args.dir).joinpath(path)
    for part in path.parents[::-1][1:]:
        if part not in dirs:
            dirs.append(part)
# Create necessary directories.
for i_dir in dirs:
    if not os.path.exists(i_dir):
        os.mkdir(i_dir)

s3 = get_s3(args.profile)
args.bucket = get_bucket(s3, args.bucket)

# Download.
keys = tqdm(args.keys, desc="Download")
for key in keys:
    keys.set_description(f"Download ({os.path.basename(key)})")
    s3.download_file(args.bucket, key, os.path.join(args.dir, key))
