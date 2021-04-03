https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/python-setup

Setup
```
python3 -m venv env
. env/bin/activate

pip3 install adafruit-circuitpython-dht
sudo apt-get install libgpiod2
```

Run
```
. env/bin/activate
python3 dht-web.py
```