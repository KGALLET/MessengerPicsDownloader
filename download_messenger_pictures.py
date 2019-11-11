#!python3
import os
from os import mkdir
from os.path import isdir, join
from datetime import datetime

from fbchat import Client
from fbchat.models import ImageAttachment
import urllib3

http = urllib3.PoolManager()

DESTINATION_FOLDER="XXX"

def isFileExist(filename):
    for dir, sub_dirs, files in os.walk(DESTINATION_FOLDER):
        if filename in files:
            return True
    return False

def download_pictures(user, password, thread_id, output_folder):
    downloaded = 0
    if not isdir(output_folder):
        mkdir(output_folder)

    client = Client(user, password)

    images = client.fetchThreadImages(thread_id)
    for im in images:
        if not type(im) == ImageAttachment:
            continue
        if (im.original_extension) == 'gif':
            continue
        img_filename = im.uid + ".jpg"
        output_filename = join(output_folder, img_filename)
        if (isFileExist(img_filename)):
            print("File %s already downloaded" % img_filename)
            continue
        url = client.fetchImageUrl(im.uid)
        data = http.request("GET", url=url, preload_content=False)
        data = data.read()
        downloaded += 1
        print("Downloading %s" % output_filename)

        with open(output_filename, "wb") as f:
            f.write(data)

    client.send(Message(text="Synchronisation du cloud fini, nb photos telecharges: " + downloaded), thread_id=client.uid, thread_type=ThreadType.USER)
    client.send(Message(text="Synchronisation du cloud fini, nb photos telecharges: " + downloaded), thread_id=thread_id, thread_type=ThreadType.USER)

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("email", help="Email of your facebook account")
    parser.add_argument("password", help="Password of your facebook account")
    parser.add_argument("thread_id", help="ID of your conversation")
    parser.add_argument("--output", '-o', help="Output folder where pictures will be stored", default=".")

    args = parser.parse_args()
    download_pictures(args.email, args.password, args.thread_id, args.output)
