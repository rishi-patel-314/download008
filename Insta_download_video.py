from datetime import datetime
from tqdm import tqdm
import requests
import re
import sys
import json
​
​
header={
    "User-Agent":"Mozilla/5.0(Window NT 6.3;Win64 ; x64) AppleWebkit/537."
​
}
​
Insta_url=input("enter the url")
​
Tail= "?__a=1"
​
url=Insta_url+Tail

​
reponse= requests.get(url,headers=header).json()

video_location =reponse["graphql"]["shortcode_media"]['video_url']

file_size_request = requests.get(video_location, stream=True)
file_size = int(file_size_request.headers['Content-Length'])
block_size = 1024
filename = datetime.strftime (datetime.now (), '%Y-%m-%d-%H-%M-%S')
t = tqdm (total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)
with open (filename + '.mp4', 'wb') as f:
    for data in file_size_request.iter_content (block_size):
        t.update (len (data))
        f.write (data)
t.close ()
print ("Video downloaded successfully")
