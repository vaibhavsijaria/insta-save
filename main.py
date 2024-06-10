from utils.metadata import add_description, read_description, search_description
from utils.insta_dl import download_reel

import os
def main():
    reel_url = ""
    dl_path = download_reel(reel_url,"downloads/")
    with open("downloads/download.txt") as f:
        # print(dl_path)
        output_file = add_description(dl_path,f.read())
    os.remove("downloads/download.txt")
    print(read_description(output_file))
    print(search_description("processed/","doctor"))
main()