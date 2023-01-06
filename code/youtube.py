from pytube import YouTube
import logging

# TODO - Documentation...

logging.basicConfig(level=logging.DEBUG, format=(
    '%(asctime)s - %(levelname)s - %(message)s'), filename='config/youtube-logfile.log')


def youtube_download(link: str) -> str:
    """
    Method to download videos from YouTube. Will require only the video url.

    :param link: (Required) The YouTube url that should be downloaded.
    
    :return: str
    """
    youtube_object = YouTube(link)
    youtube_object = youtube_object.streams.get_highest_resolution()

    try:
        youtube_object.download('data/YouTube/')

    except Exception as e:
        logging.error(f'An error occurred: {e}')

    logging.info(f'Downloaded: {link}')
