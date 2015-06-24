# HeroTwitter
Python API to take GoPro picture and upload to Twitter.

## Description

This program can be used to take GoPro pictures and automatically upload it to a Twitter account. The GoPro must be connected via WiFi. 

## How it works

There are three modules:

- **gopro.py**: Controls GoPro device remotely, setup and download taken photos to local device, all through the Wifi connection.
- **twitter.py**: Upload ficture files to Twitter.
- **herotwitter.py**: Joins the previews modules and provides the final funcionality: take photo and upload it to Twitter.

## Setup

First, download the code:

```bash
git clone https://github.com/rodolfosantos/HeroTwitter.git && cd HeroTwitter
```

Install the following dependencies: requests, wget, and tweepy.
Execute this to install them on your machine:

```bash
sudo pip install requests
sudo pip install wget
sudo pip install tweepy
```

Set your Twitter account consumer keys and access tokens, used for OAuth, into **twitter.py** module:

```bash
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
```

## Example

To use this library, your computer should be connected to Internet via Ethernet, and sould be connected to GoPro via Wifi interface.

Then execute python interpreter into HeroTwitter folder:

```bash
$ python
>>> import herotwitter

>>> herotwitter.takePhotoAndUpload("Photo uploaded with https://github.com/rodolfosantos/HeroTwitter")
```



## Change History

This project uses [semantic versioning](http://semver.org/).

### v0.1.0 - 2015/06/xx

* Initial release

