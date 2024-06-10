import subprocess
import json
import os

from fuzzywuzzy import fuzz
from pathlib import Path

def add_description(file_path, description,output_path = "processed"):
    output_dir = Path(output_path)
    output_dir.mkdir(parents=True, exist_ok=True)
    file_name = file_path.name
    output_file = output_dir / file_name
    command = f'ffmpeg -y -i {file_path} -metadata description="{description}" -codec copy {output_file}'
    subprocess.run(command, shell=True, check=True,stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    return output_file


def read_description(file_path):
    command = f'ffprobe -v quiet -print_format json -show_format -show_streams {file_path}'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    data = json.loads(result.stdout)
    return data['format']['tags'].get('description', None)


def search_description(directory, search_term):
    matching_videos = []
    for filename in os.listdir(directory):
        if filename.endswith(".mp4"):
            file_path = os.path.join(directory, filename)
            description = read_description(file_path)
            if description and fuzz.token_set_ratio(search_term, description) > 70:
                matching_videos.append(file_path)
    return matching_videos