from vimeo_downloader import Vimeo
import logging
import os

logging.basicConfig(level=logging.DEBUG, format=(
    '%(asctime)s - %(levelname)s - %(message)s'), filename='config/vimeo-logfile.log')


def vimeo_id_downloader(videos: list, cookies: str, module: int) -> None:
    """
    This method will require only the viemo unique ID, you can get it by clicking in the option 'Share'.

    :param videos: (Required) Vimeo unique id's, comma separated if more than one.
    :param cookies: (Required) Users cookies that allow lib to login into host platform.
    :param module: (Optional) Number of module.

    :return: None
    """

    # Actual module
    module = module
    # Download path
    path = os.makedirs(f'data/Vimeo/Modulo {module}', exist_ok=True)

    # Chrome cookies for login, how to extract: https://pypi.org/project/vimeo-downloader/
    cookies = f"""{cookies}""".strip()

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
            download_directory=f'data/Vimeo/Modulo {module}/', filename=title)

        video_num += 1
