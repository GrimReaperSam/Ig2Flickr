# Ig2Flickr

This is a short script to upload your posted photos from Instagram to your Flickr account. Now that Instagram doesn't allow
non-commercial users to query more than the most recent 20 posts, it's easier to use the Flickr API, but you need to synchronize it
with what you have on Instagram.

## Setup

First clone the repo

`git clone https://github.com/GrimReaperSam/Ig2Flickr.git`

Then you can install the required libraries using `pip`

`pip install -r requirements.txt`

Finally, you need to setup a Flickr app account to get your API key and secret for the upload to work.
Please visit [Flickr](https://www.flickr.com/services/apps/create/apply/) to obtain them.

Download the Instagram data from your account. If you don't know how to do that, you can follow Instagram's 
help [here](https://help.instagram.com/181231772500920).

## Run

Once you downloaded the data from Instagram, all you need to do is extract the zip folder, then run this script as follows

`python ig2flickr.py API_KEY API_SECRET IG_FOLDER [--geocode]`

The `--geocode` option allows you to also upload location data to Flickr, but you need to first configure it from 
your Flickr settings.