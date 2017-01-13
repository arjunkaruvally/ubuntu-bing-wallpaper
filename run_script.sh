PATH=$PATH:/usr/local/bin

LD_LIBRARY_PATH=/lib:/usr/lib:/usr/local/lib

# export DBUS_SESSION_BUS_ADDRESS=$(ps -u phablet e | grep -Eo 'dbus-daemon.*address=unix:abstract=/tmp/dbus-[A-Za-z0-9]{10}' | tail -c35)

PID=$(pgrep gnome-session)
export DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$PID/environ|cut -d= -f2-)


python /home/arjun/open_source/bing-wallpaper-ubuntu/updater.py

DATE=$(date +%d)

echo dateis
echo $DATE

filename="/home/arjun/open_source/bing-wallpaper-ubuntu/pics/file$DATE.jpg"

echo $filename

gsettings set org.gnome.desktop.background picture-uri file://$filename