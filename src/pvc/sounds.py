from pvc.audio_file import AudioFile


def play_sound(file_path: str) -> None:

    audio = AudioFile(file_path)
    audio.play()
    audio.close()
