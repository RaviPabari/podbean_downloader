import bs4 as bs
import requests
import argparse
from pathlib import Path
from tqdm import tqdm


class AccioPodcast:
    def __init__(self):
        self.main_url = ""
        self.folder_name = ""
        self.pages = ""
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
            args = parser.parse_args()
            self.main_url = args.url
            self.pages = args.pages
        except KeyboardInterrupt:
            exit(0)

    def get_names_and_link(self):
        print("collecting your podcasts....")
        for no_of_pages in range(1, self.pages + 1):
            url = ''
            if self.main_url[-1] == '/':
                url = self.main_url + str(no_of_pages)
            else:
                url = self.main_url + '/' + str(no_of_pages)
            source = requests.get(url)
            soup = bs.BeautifulSoup(source.text, "lxml")

            # finding all links on the page
            all_audio_tag = soup.find_all(class_="pbplayerBox theme7")
            for findings in all_audio_tag:
                self.links.append(findings["data-uri"])
            print(
                "\n Collected podcast.\n\n Number of podcast collected =",
                len(all_audio_tag),
            )

            # finding all titles
            all_titles = soup.find_all(class_="main-title")
            for titles in all_titles:
                temp = titles.h2

    def download_helper(self, filename, url):
        pass

    def download_files(self):
        pass


if __name__ == "__main__":
    AccioPodcast()
