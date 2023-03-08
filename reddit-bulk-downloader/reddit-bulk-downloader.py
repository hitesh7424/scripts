import yt_dlp
import requests
import time
import re


def image_download():
    counter = 0
    name = int(time.time())
    for link in image_links:
        # Send an HTTP request to the URL and get the response
        response = requests.get(link)

        # Check if the response was successful (HTTP status code 200)
        if response.status_code == 200:
            # Open a file for writing and write the content of the response to it
            with open(f"images/image_{subreddit}_{name}.jpg", "wb") as f:
                f.write(response.content)
                counter += 1
                name += 1
        else:
            print("\rError while downloading image.", end='')

    print(f"{counter} images downloaded")


def video_download():
    name = int(time.time())
    counter = 0
    for link in video_links:
        output_dir = 'videos'

        ydl_opts = {
            'outtmpl': output_dir + f'/video_{subreddit}_{name}.%(ext)s',
            'user_agent': my_user_agent
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
                name += 1
                counter += 1
        except:
            print('not downloaded')

    print(f"{counter} videos downloaded")


'''

["memes",
"dankmemes",
"AdviceAnimals",
"terriblefacebookmemes",
"youtubehaiku",
"funny",
"gifs",
"whitepeopletwitter",
"blackpeopletwitter",
"wholesomememes",
"PrequelMemes",
"SequelMemes",
"TrebuchetMemes",
"HistoryMemes",
"CursedComments",
"showerthoughts"]

'''

sub_list = ["memes",
            "dankmemes",
            "AdviceAnimals",
            "terriblefacebookmemes",
            "youtubehaiku",
            "funny",
            "gifs",
            "whitepeopletwitter",
            "blackpeopletwitter",
            "wholesomememes",
            "PrequelMemes",
            "SequelMemes",
            "TrebuchetMemes",
            "HistoryMemes",
            "CursedComments",
            "showerthoughts"]

# Define your custom user agent string
my_user_agent = "your bot 0.1"
headers = {"User-Agent": my_user_agent}

for i in range(len(sub_list)):
    if(i < 10):
        print(f'0{i}. r/{sub_list[i]}')
    else:
        print(f'{i}. r/{sub_list[i]}')

sub_number = int(input('subreddit: '))

subreddit = sub_list[sub_number]
limit = 200

url = f"https://www.reddit.com/r/{subreddit}/new.json?limit={limit}"
print('url: ',url)
response = requests.get(url=url, headers=headers)

json_text = response.text

# Define the regex pattern
image_pattern = r"https://i\.redd\.it/\w+\.jpg"
video_pattern = r"https:\/\/v\.redd\.it\/\w{13}"

image_links = re.findall(image_pattern, json_text)
video_links = re.findall(video_pattern, json_text)
image_links = list(set(image_links))
video_links = list(set(video_links))
# print(image_links)
# print(video_links)


number_of_videos = len(video_links)
number_of_images = len(image_links)
print(f"subreddit: r/{subreddit}")
print(f"number of videos found: {number_of_videos}")
print(f"number of images found: {number_of_images}")

inputyn = str(input("[Y/n]"))

if (inputyn == 'y' or inputyn == 'Y'):
    video_download()
    # image_download()
