import os
import threading
from tkinter import Tk, Button, Label, PhotoImage
import pygame

class MusicPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")

        self.label = Label(root, text="MUSIK PLAYER")
        self.label.pack(pady=20, padx=5)

        self.label = Label(root, text="musik.mp3")
        self.label.pack(pady=10, padx=5)

        self.button_play = Button(root, text="Putar Musik", command=self.play_music)
        self.button_play.pack(pady=10, padx=5)

        self.photo_pause = PhotoImage(file="playmp3\pause.png").subsample(16)
        self.photo_resume = PhotoImage(file="playmp3\play.png").subsample(16)

        self.button_pause = Button(root, image=self.photo_pause, command=self.pause_resume_music, state="disabled")
        self.button_pause.pack(pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.close_app)

        self.music_paused = False

    def play_music(self):
        file_path = os.path.join(os.getcwd(), "media", "musik.mp3")

        self.music_thread = threading.Thread(target=self._play_music_thread, args=(file_path,))
        self.music_thread.start()

        self.button_pause.config(state="normal", image=self.photo_pause)

    def _play_music_thread(self, file_path):
        pygame.init()
        pygame.mixer.init()

        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy() or self.music_paused:
            pygame.time.Clock().tick(10)

        duration = pygame.mixer.Sound(file_path).get_length()
        self.label.config(text=f"Durasi Musik: {duration:.2f} detik")

        self.button_play.config(state="normal")
     
        self.button_pause.config(state="disabled")

    def pause_resume_music(self):
        if not self.music_paused:
            pygame.mixer.music.pause()
            self.music_paused = True
            self.button_pause.config(image=self.photo_resume)
        else:
            pygame.mixer.music.unpause()
            self.music_paused = False
            self.button_pause.config(image=self.photo_pause)



    def close_app(self):
        pygame.mixer.quit()
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    app = MusicPlayerApp(root)
    root.mainloop()