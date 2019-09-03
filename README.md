# image-creator-for-epaper10p3

# Setup

```
pip install pygame pytz python-connpass python-dateutil
```

```
sudo apt install fonts-noto
```

# Run

```
python main.py
```

# Set as crontab job to show image on epaper with using IT8951

## Setup package for root

```
sudo su
pip install pygame pytz python-connpass python-dateutil
```

## Set crontab job

```
sudo crontab -e
```

Every 30 minutes
```
*/30 * * * * cd /home/pi/gitprojects/image-creator-for-epaper10p3 && /usr/bin/python main.py && /home/pi/gitprojects/IT8951/IT8951 0 0 events.bmp
```

# License

MIT

# References

- [10.3inch e-Paper HAT (D)](https://www.waveshare.com/wiki/10.3inch_e-Paper_HAT_(D))
- [raspi_spi_epaper/main_show_halake_events.py](https://github.com/asukiaaa/raspi_spi_epaper/blob/master/main_show_halake_events.py)
