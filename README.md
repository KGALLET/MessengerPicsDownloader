Simple script to download all pictures from a facebook conversation
This script is using [fbchat > 1.8.0](https://github.com/carpedm20/fbchat)

# Usage

Don't forget to change DESTINATION_FOLDER variable.

```
usage: download_messenger_pictures.py [-h] [--output OUTPUT] 
                                      email password thread_id

positional arguments:
  email                 Email of your facebook account
  password              Password of your facebook account
  thread_id             ID of your conversation

optional arguments:
  -h, --help            show this help message and exit
  --output OUTPUT, -o OUTPUT
                        Output folder where pictures will be stored
```

To use it in a crontab, for example : 
```
0 20 * * * sudo /usr/bin/python3.7 download_messenger_pictures.py <email> <password> <thread_id> --output <destination_folder> > <destination_folder>/logs.info 2>&1 & 
```

TODO : 
Do it for the vids
