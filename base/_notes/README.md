# Nanny Pi
- NSD server
- VLC runner
- Button Controller?

    docker-compose up -d
    docker build -t player .
    docker run -it --device=/dev/snd --env="DISPLAY" --net=host player 

-v /dev/snd:/dev/snd --privileged
## VLC



apt-get install dbus*
apt-get install alsa-utils
apt-get install pulseaudio
vlc-plugin*

RUN useradd -m vlc \
&& usermod -a -G audio vlc


Gtk-WARNING **: cannot open display: unix:0.0
 ->
xhost +local:docker