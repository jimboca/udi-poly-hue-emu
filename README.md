![Build Status](https://travis-ci.org/jimboca/udi-poly-hue-emu.svg?branch=master)](https://travis-ci.org/jimboca/udi-poly-hue-emu)

# harmony-polyglot

This is the Hue Emulator Poly for the [Universal Devices ISY994i](https://www.universal-devices.com/residential/ISY) [Polyglot interface](http://www.universal-devices.com/developers/polyglot/docs/) with  [Polyglot V2](https://github.com/Einstein42/udi-polyglotv2)
(c) JimBoCA aka Jim Searle
MIT license.

This node server is intended to allow controlling ISY994 devices from other devices that support a Hue Hub.  So devices like a Harmony Hub can control ISY devices or scenes.  The Harmony Elite remote has dedicated home control buttons which work very well with this setup.  It also should work to control devices with Amazon Alexa, but I no longer use Alexa so I can not support it.  The Google home no longer works with local Hue hubs, so that isn't supported either.

Previously this functionality was available in [ISYHelper](https://github.com/jimboca/ISYHelper) but all ISYHelper functions have been moved to nodeservers.

It uses the [PyISY Library](https://pypi.python.org/pypi/PyISY) to connect to the ISY and control devices, and the [Python Hue Hub Emulator](https://github.com/falk0069/hue-upnp) to emulate a Hue Hub.

## Setup

By default all devices that have a 'Spoken' property set in the ISY notes will be added to the list.  To set this right click on the device in the ISY admin console and select 'Notes'.  If you have a recent version of the ISY firmware and admin console you should see the option to add 'Spoken'.  If you want the spoken name to always match the device name, just make the value of the Spoken property be the number one '1', without the quotes. Make sure there are no accents in the Spoken property, only plain ASCII characters, or the discovery will fail.

To control a scene you can set the Spoken on the scene controller, in which case the PyHue will turn on the scene, or set the Spoken on the scene itself. (Need to test how brighten/dim work with scenes)

IMPORTANT: Currently if you 'group device' it will not find your Spoken property on your device.  This is an issue with the PyISY library that I will try to fix soon because almost all my devices were grouped. (Is this still true?)

## Installation

1. Backup Your ISY in case of problems!
   * Really, do the backup, please
2. Go to the Polyglot Store in the UI and install HueEmulator
3. Open the ISY Admin Console, close and re-open if it was already open.
3. Once it installs you should see a new node 'Hue Emulator Controller'
   * If you don't see that node, then restart the Harmony node server from the Polyglot UI.
4. Set the Configuration as described in the next section.
5. Restart the nodeserver after all params are saved.

## Configuration

In to 'Configuration' tab contains the default values for all Custom Configuration Parameters.

* hue_port : The port used for Hue Emulator Can keep default of 8080
* isy_host : The IP address of your ISY on the local network
* isy_port : The http port of your ISY
* isy_user : The user for your ISY
* isy_password: The password for your ISY

### Hue Emulator Controller node

This is the one and only node for this nodeserver.  It has the following options:

* Debug Mode:  The Logger mode, debug will spew a lot of information, info is he default.
* Listen:  Enabling this is the same as pushing the button on a hue hub.  You should only turn on when adding the hub to another device.

## Debug

The log for the nodeserver will show that it is parsing all the notes from each device.  When it finds a spoken property it will print information about that device.

You should see it checking the ‘notes’ of each device on the ISY when it starts up:
```2018-06-17 21:05:50,246 INFO     ISY Request: http://your.isy.ip:80/rest/nodes/2E%20AD%2073%201/notes
```

And if it finds a Spoken set you should see:
```2018-06-17 21:05:50,339 INFO     ISYHueEmu:refresh: add_spoken_device: name=The Device Nmae, spoken=The Spoken Property
```
followed by a few other lines about the device.

Also, in the nodeserver directory there will be a config.json that contains the devices it found

## TODO

- Move device info Custom Configuration Paramaters instead of config.json
- New polyglot UI can display Help, test it to should show device info
- Test bright/dim scenes
- Shut down listener on startup

## Requirements

1. Polyglot V2 itself should be run on Raspian Stretch.
  To check your version, ```cat /etc/os-release``` and the first line should look like
  ```
  PRETTY_NAME=Raspbian GNU/Linux 9 (stretch)
  ```
  It is possible to upgrade from Jessie Stretch, but I would recommend just reimaging the SD card.  Some helpful links:
   * https://www.raspberrypi.org/blog/raspbian-stretch/
   * https://linuxconfig.org/raspbian-gnu-linux-upgrade-from-jessie-to-raspbian-stretch-9
1. This has only been tested with ISY 5.0.12 so it is not guaranteed to work with any other version.

# Upgrading

Open the Polyglot web page, go to nodeserver store and click "Update" for "HueEmulator". You can answer No to the install profile question.

Then restart the  nodeserver by selecting it in the Polyglot dashboard and select Control -> Restart, and watch the log to make sure everything goes well.

# Release Notes

- 2.0.1 06/19/2018
  - Move to released PyISY 1.1.0 to fix finding scenes.
- 2.0.0
  - Never officially released.