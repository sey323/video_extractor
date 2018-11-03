import os
from glob import glob
import cv2
from pytube import YouTube

class MovieIter(object): #動画のフレームを返すイテレータ
    def __init__(self, moviefile, size=None, inter_method=cv2.INTER_AREA , interval = 1 ):
        #TODO: check if moviefile exists
        if os.path.isfile(moviefile):#mp4ファイルが存在するとき
            print('[Loading]\tLoading Movie')
            self.org = cv2.VideoCapture(moviefile)
        else:#MP4がないときはYoutubeからダウンロード
            print('[Download]\tDownloadMovie')
            self.youtube_downloader(moviefile,'./src')
            dnld_movie_path = self.get_latest_modified_file_path('./src/')
            self.org = cv2.VideoCapture(dnld_movie_path)

        self.framecnt = 0
        self.size = size #frame size
        self.inter_method = inter_method
        self.interval = interval
    def __iter__(self):
        return self
    def __next__(self):
        self.end_flg, self.frame = self.org.read()
        if not self.end_flg: # end of the movie
            raise StopIteration()
        self.framecnt+=1
        if self.size: # resize when size is specified
            self.frame = cv2.resize(self.frame, self.size, interpolation=self.inter_method)
        return self.frame
    def __del__(self): # anyway it works without destructor
        self.org.release()

    def youtube_downloader(self,url,save_path):
        '''
        YouTubeからダウンロードする
        ------
        Parameters
            url:動画のURL
        '''
        yt = YouTube(url)
        yt.streams.get_by_itag(22).download(save_path)
        return yt.title

    def get_latest_modified_file_path(self,dirname):
        target = os.path.join(dirname, '*')
        files = [(f, os.path.getmtime(f)) for f in glob(target)]
        latest_modified_file_path = sorted(files, key=lambda files: files[1])[-1]
        return latest_modified_file_path[0]
