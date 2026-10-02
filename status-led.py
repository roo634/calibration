import time
import socket
import struct
import fcntl
from gpiozero import LED

# Configuration
LED_PIN = 17
INTERFACE = 'zt0'  # Change to 'eth0' if waiting for starlink
CHECK_INTERVAL = 2    # Seconds between network checks
BLINK_INTERVAL = 1  # Seconds for blink speed

led = LED(LED_PIN)

def get_ip_address(ifname):
    """Returns the IP address of an interface, or None if not configured."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Request the IP address from the interface name
        return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack('256s', ifname[:15].encode('utf-8'))
        )[20:24])
    except IOError:
        return None

def check_network():
    try:
        with socket.create_connection(("8.8.8.8", 53), timeout=CHECK_INTERVAL):
            return True
    except OSError:
        return False


def main():
    print(f"Starting network LED monitor for {INTERFACE}...")
    while True:
        # Phase 1: Turn LED solid ON until IP is assigned and has network
        led.on()
        while True:
            ip = get_ip_address(INTERFACE)
            if ip and check_network():
                print(f"Interface {INTERFACE} configured with IP: {ip}")
                break
            time.sleep(CHECK_INTERVAL)

        # Phase 2: Blink continuously once IP is found and has network
        while check_network():
            led.toggle()
            time.sleep(BLINK_INTERVAL)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        led.off()

