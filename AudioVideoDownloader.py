from pytubefix import YouTube
import os
from pytubefix import Playlist


class AudioVideoDownloader:
    def get_mp3(self, url, dest_dir):
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        print("start to extract audio from youtube url:" + url)
        yt = YouTube(str(url))

        title = "default"
        if yt.title:
            title = yt.title

        audio = yt.streams.filter(only_audio=True).first()
        out_file = audio.download(output_path=dest_dir, filename=title + ".mp3")
        print("downloaded audio file to folder:" + out_file)
        return out_file

    def get_mp3s(self, urls, dest_dir):
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        for url in urls:
            print("start to extract audio from youtube url:" + url)
            yt = YouTube(str(url))
            title = yt.title
            audio = yt.streams.filter(only_audio=True).first()
            out_file = audio.download(output_path=dest_dir, filename=title + ".mp3")
            print("downloaded audio file to folder:" + out_file)

    def download_youtube_video(self, url, output_path="."):
        try:
            yt = YouTube(str(url))
            stream = yt.streams.get_highest_resolution()
            video_title = yt.title
            output_file = os.path.join(output_path, f"{video_title}.mp4")
            stream.download(output_path=output_path)
            print(f"Video '{video_title}' downloaded successfully to {output_file}")
        except Exception as e:
            print(f"Error downloading video: {e}")

    def download_youtube_video_playlist(self, url, output_path="."):
        try:
            pl = Playlist(url)

            for video in pl.videos:
                stream = video.streams.get_highest_resolution()
                video_title = video.title
                output_file = os.path.join(output_path, f"{video_title}.mp4")
                stream.download(output_path=output_path)
                print(f"Video '{video_title}' downloaded successfully to {output_file}")
        except Exception as e:
            print(f"Error downloading video: {e}")


def main():

    url = "https://www.youtube.com/watch?v=c2TJZb4FBlc"
    downloader = AudioVideoDownloader()
    downloader.get_mp3(url, 'output')



if __name__ == "__main__":
    main()
