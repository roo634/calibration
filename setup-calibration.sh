#! /bin/bash

echo "Calibration Configuration"
echo
if (( $EUID != 0 )); then 
    echo "Please run as root or use sudo." 
    exit 1 
fi
echo

# Move the service files first....
cp services/*.service /lib/systemd/system


# Setup the pi config.txt file (controls drivers)
cp config.txt /boot/firmware/config.txt

echo "Installing dependcies..."

sudo apt update

sudo apt install -y \
    python3-opencv \
    python3-gi \
    python3-gi-cairo \
    python3-numpy \
    python3-dev \
    python3-matplotlib \
    python3-pygame \
    gir1.2-gstreamer-1.0 \
    gir1.2-gst-plugins-base-1.0 \
    gir1.2-gst-plugins-bad-1.0 \
    gstreamer1.0-tools \
    gstreamer1.0-plugins-base \
    gstreamer1.0-plugins-good \
    gstreamer1.0-plugins-bad \
    gstreamer1.0-plugins-ugly \
    gstreamer1.0-libcamera \
    ffmpeg

if [ ! -d ".venv" ]; then
    python3 -m venv --system-site-packages .venv
fi

source .venv/bin/activate

python3 -m pip install --upgrade pip

python3 -m pip install pymavlink

python3 -m pip install PyYAML mavproxy

python3 -m pip install future

echo
echo "Done."

systemctl enable calibration

# Remove this file and history
rm /home/pi/calibration*/setup-calibration.sh 
rm /home/pi/.bash_history
history -c



echo
echo "Rebooting in 10 seconds"
sleep 10
sudo reboot


