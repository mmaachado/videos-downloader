from vimeo_downloader import Vimeo
import pandas as pd
import os

"""
In the urls.txt you get two columns: 
URL -> The website that is hosting the video.
VIMEO_ID -> The vimeo unique identifier for the video, you can get it by clicking in 'Share' or get it in the HTML of the website.

Paste as many links you want.
"""
df = pd.read_csv('../urls.txt', delimiter=',')

# If you want to create folders for more than one module

module = 1
path = os.makedirs(f'../data/Module {module}', exist_ok=True)

# For more than one video, use this counter
video_num = 1

# Here is the loop that will download each link you pasted
for row in df.to_dict():
    # Identify the website url
    extracted_url = row['URL']
    # Identify the vimeo unique id
    extracted_id = row['VIMEO_ID']
    """
    Strip the url to get only the video title
    e.g. https://vimeo/123456-my-first-class
    Will be: 123456 my first class
    """
    raw_title = extracted_url[69:].replace('-', ' ')
    # Remove the digits so we got only my first class
    title = ''.join([i for i in raw_title if not i.isdigit()])
    # Some cases the string comes with withespace in the first character, so I just strip the string and capitalize it
    title = title.strip().capitalize()

    # Here we parse the vimeo id and tells the program that it comes from and embed url, for more details check the vimeo-downloader lib documentation
    vimeo = Vimeo(f'{extracted_id}', embedded_on=f'{extracted_url}')
    # [-1] Downloads the best quality video, check lib documentation for more info
    vimeo.streams[-1].download(download_directory=path, filename=title)

    # Each time it saves a file, it will increase this title number
    video_num += 1