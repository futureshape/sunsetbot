# sunsetbot
Twitter bot that posts a daily photo of the sunset from my camera live stream on YouTube

## Dependencies

* [Sunwait](https://github.com/risacher/sunwait) - install from source or use the [Ubuntu snap](https://snapcraft.io/install/sunwait/ubuntu) or [MacPorts](https://ports.macports.org/port/sunwait/summary)
* [Python Twitter API](https://python-twitter.readthedocs.io/en/latest/)
* [youtube-dl](https://github.com/ytdl-org/youtube-dl)
* [ffmpeg](https://ffmpeg.org/)

## Setup

1. Set up a camera pointing out of your window towards the sunset, and livestream it on YouTube
2. Set up Twitter: Sign up for Twitter account for your bot, [apply for Twitter Developer account](https://developer.twitter.com/en/apply-for-access) using your new Twitter account, create an application and get the keys  
3. Clone repository to your server
4. Rename `twitter_secrets_template.py` to `twitter_secrets.py` and add the keys you got from Twitter
5. Edit `sunsetbot.py` to update your location (`lat`, `long` - must be in a format recognisable by `sunwait`), and the URL to your YouTube livestream (`youtube_link`)
6. Keep `Debug` set to `True` (to avoid a long wait) and run the script (`python3 sunsetbot.py`) to check that the image has been captured an posted on Twitter
7. Set `Debug` to `False` and get `cron` to run your script once a day, around mid-day. `sunsetwait` will cause the script to pause until sunset, at which point the image will be captured and posted on Twitter. The script will then quit and will get to run again next day using `cron`  
