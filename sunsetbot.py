import twitter, sys, os, twitter_secrets

lat = "51.4847637N"
long = "0.0510414W"
offset = 5 # minutes before sunset

youtube_link = "https://www.youtube.com/channel/UCV0mm5ClLgAA0mxFRcb27pA/live"
temp_capture_file = "capture.jpg"

# Set to False for production, otherwise it won't wait for the right amount of time
debug = True 

sunwait_command = "sunwait wait sunset {debug} {lat} {long} offset {offset}".format(debug = "debug" if debug else "", lat = lat, long = long, offset = offset)

sunwait_status = os.system(sunwait_command)
if sunwait_status != 0:
    print("sunwait returned error status, quitting")
    sys.exit()

if os.path.exists(temp_capture_file):
  os.remove(temp_capture_file)

youtube_command = "youtube-dl --prefer-ffmpeg \"{youtube_link}\" -o - | dd count=32 bs=4096 | ffmpeg -i - -f image2 -frames:v 1 {output_file}"

os.system(youtube_command.format(youtube_link = youtube_link, output_file = temp_capture_file))

if not os.path.exists(temp_capture_file):
    print("youtube-dl did not manage to download frame, quitting")
    sys.exit()

api = twitter.Api(consumer_key=twitter_secrets.consumer_key,
                  consumer_secret=twitter_secrets.consumer_secret,
                  access_token_key=twitter_secrets.access_token_key,
                  access_token_secret=twitter_secrets.access_token_secret)

status = api.PostUpdate('', media=temp_capture_file)
