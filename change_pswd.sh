#! /bin/bash

username="pi"

read -s -p "Enter secret key: " secret
echo

serial=$(awk '/Serial/ {print $3}' /proc/cpuinfo)

echo 
echo "Serial number is"
echo "$serial"

sleep 10

new_password=$(
    printf '%s' "$serial" |
    openssl dgst -sha256 -hmac "$secret" |
    awk '{print $2}'
    cut -c1-16
)

echo 
echo "Password is"
echo "$new_password"

sleep 10

mkdir /mnt/sdcard
mount /dev/mmcblk0p2 /mnt/sdcard

printf '%s:%s\n' "$username" "$new_password" | sudo chroot /mnt/sdcard chpasswd

umount /mnt/sdcard
rm -r /mnt/sdcard

