import instaloader
from pathlib import Path
import os
import re

def get_next_filename(directory, extension):
    max_num = 0
    for filename in os.listdir(directory):
        base, ext = os.path.splitext(filename)
        if ext == extension:
            if numbers := re.findall(r'\d+', base):
                max_num = max(max_num, int(numbers[0]))
    return str(max_num + 1) + extension

def download_reel(reel_url, file_directory):
    L = instaloader.Instaloader(download_pictures=False, download_video_thumbnails=False,
                                download_videos=True, compress_json=False, save_metadata=False)
    L.filename_pattern = "download"
    reel_shortcode = reel_url.split('/')[-2]
    reel = instaloader.Post.from_shortcode(L.context, reel_shortcode)
    L.download_post(reel, target=Path(file_directory))
    dl_name =  Path(file_directory)/get_next_filename(file_directory,".mp4")
    os.rename(Path(file_directory)/"download.mp4",dl_name)
    return dl_name

