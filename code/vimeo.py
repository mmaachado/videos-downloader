from vimeo_downloader import Vimeo
import logging
import os

logging.basicConfig(level=logging.DEBUG, format=(
    '%(asctime)s - %(levelname)s - %(message)s'), filename='../config/vimeo-logfile.log')

# Actual module
module = 1
# Download path
path = os.makedirs(f'../data/Modulo {module}', exist_ok=True)

# Chrome cookies for login, how to extract: https://pypi.org/project/vimeo-downloader/
cookies = """ """.strip()

# List of vimeo id's for download
videos = []

# Attribute to adjust number of videos title
video_num = 1
# Here is the loop that will download each id pasted
for video in videos:
    vimeo = Vimeo(url=video, cookies=cookies)
    best_stream = vimeo.best_stream
    title = best_stream.title
    title = f'{video_num} {title}'

    logging.info(f'Downloading"{title}')
    best_stream.download(
        download_directory=f'../data/Modulo {module}/', filename=title)

    video_num += 1
