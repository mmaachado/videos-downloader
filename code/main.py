from vimeo import vimeo_id_downloader
from youtube import youtube_download
from typho import typing


class VideoDownloader():
    """
    Class to get which platform user intent to download from.

    :method youtube_download(link=link):
        Get YouTube url that should be downloaded.
        :return: .mp4 file saved into YouTube folder.

    :method vimeo_id_dowloader(videos=videos, cookies=cookies, module=module):
        Get Vimeo id, browser cookies that should be downloaded and save file into module folder with number choosed by user.
        :return: .mp4 file saved into Vimeo/Module "number" folder.
    """
    typing('Which platform should be downloaded?\n1. YouTube\n2. Vimeo\n')
    user_choice = input()

    if user_choice == '1':
        link = input('Enter YouTube url: ')
        youtube_download(link=link)

    elif user_choice == '2':
        videos = input('Vimeo unique IDs: ')
        cookies = input('Browser Cookies: ')
        module = input('Module number: ')

        vimeo_id_downloader(videos=videos, cookies=cookies, module=module)

    else:
        typing('Wrong input!')
