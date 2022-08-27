from pytube import Playlist
from pytube import YouTube

# #download single vedio

input_massage = """
Choose, What do you wnat to download ?
"s" => Single vedio
"a" => Audio
"l" => playlist
"""

user_input = input(input_massage).strip().lower()

commands_list = ["s", "a", "l"]


def finish():

    print("download done")


def download_single_vedio():

    link = input("Please enter the vedio URL: ")

    vedio = YouTube(link)
    print(
        f"The Vedio duration is :\n {vedio.length/60} minutes \n -------------------")
    vedio.streams.get_highest_resolution().download(
        output_path="C:/Users/DELL/Downloads/Video")
    vedio.register_on_complete_callback(finish())


def download_audio():

    link = input("Please enter the vedio URL: ")

    audio = YouTube(link)
    print(
        f"The audio duration is :\n {audio.length/60} minutes \n -------------------")
    audio.streams.get_audio_only().download(
        output_path="C:/Users/DELL/Downloads/Video")
    audio.register_on_complete_callback(finish())


def download_playlist():

    play_list_link = input("Please Enter the playlist URL: ")
    playlist = Playlist(play_list_link)

    for vedio in playlist.videos:
        vedio.streams.get_highest_resolution().download(
            output_path=r"C:\Users\DELL\Downloads\Video")

    vedio.register_on_complete_callback(finish())


if user_input in commands_list:

    print(f"Command Found \"{user_input}\"")

    if user_input == "s":

        download_single_vedio()

    elif user_input == "a":

        download_audio()

    elif user_input == "l":

        download_playlist()


else:

    print(f"sorry this Command \"{user_input}\" Is Not Found")
