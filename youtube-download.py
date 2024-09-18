from pytubefix import YouTube

yt_url = input('Link do youtube (com HTTPS): ')
audio_only = input('É apenas audio? S/n: ')
yt = YouTube(yt_url)

if audio_only == 'n':
    stream = yt.streams.filter(
        progressive=True, file_extension='mp4').get_highest_resolution()
    stream.download(output_path='./videos', filename=yt.title+'.mp4')
else:
    stream = yt.streams.filter(
        only_audio=True, file_extension='mp4').get_audio_only()
    stream.download(output_path='./audios', filename=yt.title+'.mp4')
