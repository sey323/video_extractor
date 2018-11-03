import sys
from pytube import YouTube

def youtube_downloader(url,save_path):
    '''
    YouTubeからダウンロードする
    '''
    yt = YouTube(url)
    yt.streams.get_by_itag(22).download(save_path)
    return yt.title

if __name__ == "__main__":
    if ( len( sys.argv ) != 2):   # 引数が足りない場合は、その旨を表示
        print('Usage: # python %s filename' % sys.argv[0])
        quit()
    url = sys.argv[1]
    youtube_downloader(url,'./src')
