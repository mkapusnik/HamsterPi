from guizero import App, PushButton, Text
import vlc

app = App(title="Krecek")
#app.set_full_screen()
headline = Text(app, text = "Krecek")

media = vlc.MediaPlayer("rtsp://krecek.local:8555/unicast")
media.set_fullscreen(True)
media.audio_set_volume(100)
media.play()

#app.set_full_screen()
app.display()
