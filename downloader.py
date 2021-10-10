import bs4 as bs
import requests
import argparse
from pathlib import Path
from tqdm import tqdm
import os


class AccioPodcast:
    def __init__(self):
        self.main_url = ""
        self.folder_name = "Downloads/"
        self.pages = 1
        self.names = []
        self.links = []
        self.initiator()
        self.get_names_and_link()
        self.download_files()

    def initiator(self):
        try:
            parser = argparse.ArgumentParser(
                description="This will download podcasts from podbean to the current working directory"
            )
            parser.add_argument("-p", "--pages", required=False, default=1, type=int)
            parser.add_argument("-u", "--url", required=True, type=str)
            parser.add_argument("-l", "--location", required=False, type=str)
            args = parser.parse_args()
            self.main_url = args.url
            self.pages = args.pages
            if args.location:
                self.folder_name = args.location + "/"

        except KeyboardInterrupt:
            exit(0)

    def get_names_and_link(self):
        print("collecting your podcasts....")
        for no_of_pages in range(1, self.pages + 1):
            url = ""
            if self.main_url[-1] == "/":
                url = self.main_url + "page/" + str(no_of_pages)
            else:
                url = self.main_url + "/page/" + str(no_of_pages)
            source = requests.get(url)
            soup = bs.BeautifulSoup(source.text, "lxml")

            # finding all links on the page
            all_audio_tag = soup.find_all(class_="pbplayerBox theme7")
            for findings in all_audio_tag:
                self.links.append(findings["data-uri"])
            print(
                "\n Number of podcast collected =",
                len(all_audio_tag),
                "on page",
                str(no_of_pages),
            )

            # finding all titles
            all_titles = soup.find_all(class_="main-title")
            for titles in all_titles:
                temp = titles.h2
                self.names.append(temp.text)
        print("All podcast collected.")

    def download_helper(self, filename, url):
        filename = filename + ".mp3"
        tmp_file_name = filename + ".tmp"

        cwd = Path.cwd()

        file_path = cwd.joinpath(filename)
        tmp_path = cwd.joinpath(tmp_file_name)

        if file_path.exists():
            return False

        # remove an existing temp file
        if tmp_path.exists():
            tmp_path.unlink()

        with requests.get(url, stream=True) as response:
            response.raise_for_status()

            total = int(response.headers.get("content-length", 0))

            with open(tmp_path, "wb") as f, tqdm(
                desc=filename,
                total=total,
                unit="iB",
                unit_scale=True,
                unit_divisor=1024,
            ) as bar:
                for chunk in response.iter_content(chunk_size=8192):
                    size = f.write(chunk)
                    bar.update(size)

        tmp_path.replace(filename)

        pwd = os.getcwd() + "/"
        if not os.path.exists(self.folder_name):
            os.system("mkdir " + self.folder_name)
        os.system("mv " + filename.replace(" ", "\ ") + " " + pwd + self.folder_name)

        return True

    def download_files(self):
        print("\n Starting your download...")
        for i in range(len(self.names)):
            print("\n Downloading", self.names[i])
            self.download_helper(self.names[i], self.links[i])
        print("\nDownloaded your podcast :) Bye.")


if __name__ == "__main__":
    AccioPodcast()
