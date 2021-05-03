# rvdm's Home Assistant Configuration Files
![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg) ![GitHub Activity](https://img.shields.io/github/last-commit/rvdm/home-assistant.svg)


# Physical Setup

I'm running my Home Assistant install using [Home Assistant Core](https://github.com/home-assistant/core) on a small Intel NUC machine in my utility closet.
The NUC is connected and integrated in my home network and a mix of home automation hardware and software.

## Hardware

- [Intel NUC NUC7i3BNK](https://www.intel.com/content/www/us/en/products/boards-kits/nuc/kits/nuc7i3bnk.html)
I stuffed this with 16GB of RAM and a 512GB Western Digital NVME drive.
- [Conbee II](https://phoscon.de/en/conbee2) USB stick for Zigbee connectivity
- [Aeotec](https://aeotec.com/z-wave-usb-stick/) Z-wave stick
- [Eneco Toon](https://www.home-assistant.io/integrations/toon/) thermostat

The above devices connect to a number of 'smart' devices in our home:
- Quite a few [GreenWave Reality Smart PowerNodes](https://products.z-wavealliance.org/products/54). These are smart z-wave power blocks with 6 EU power plug connectors that each are switchable and measure power consumption. They're not great quality, but they work for now.
- Some single [Fibaro Wall Plugs](https://www.fibaro.com/en/products/wall-plug/). They switch nice and fast, are stable, small and report power as well. 
- Lots of [TRÅDFRI](https://www.ikea.com/us/en/cat/smart-lighting-36812/) Zigbee bulbs. Cheap, work well with the Conbee II stick.
- A few TRÅDFRI switches (on/off and the round multi-button switch) for physically triggering scenes or switching power.
- A [Xiaomi 'smart humidifier'](https://xiaomi-mi.com/appliances/smartmi-zhimi-air-humidifier-2-white/) (WiFi)
- [Bosch fridge/freezer](https://www.bosch-home.nl/productoverzicht/KGN36HI32) with wifi and door-triggered cameras
- [Siemens dishwasher](https://www.siemens-home.bsh-group.com/nl/productoverzicht/SN278I26TE) with wifi
- [Roku Ultra](https://www.roku.com/products/roku-ultra) for media playing
- [LG Oled 48CX TV](https://www.lg.com/us/tvs/lg-oled48cxpub-oled-4k-tv)
- [Ikea Symfonisk](https://www.ikea.com/nl/nl/p/symfonisk-wifi-boekenplankspeaker-zwart-50357554/) Sonos 'clone'
- [Samsung WW80T754ABT washing machine](https://www.samsung.com/nl/washers-and-dryers/washing-machines/front-load-8kg-white-ww80t754abt-s2/)
- [Withings Cardio](https://www.withings.com/nl/en/body-cardio) smart scale
- [Hue motion sensor](https://www.philips-hue.com/en-us/p/hue-motion-sensor/046677473389) as an experiment
- Not really home automation, but the car reports metrics, GPS and status back via [Connected Drive](https://www.bmw-connecteddrive.nl/app/index.html#/portal)

In the house devices are wired where possible, but lots of devices connect via wifi. The network is based all off Ubiquiti equipment:
- [Ubiquiti Edgerouter 12](https://www.ui.com/edgemax/edgerouter-12/) as a router
- [Ubiquiti EdgeSwitch 8-150w](https://www.ui.com/edgemax/edgeswitch-8-150w/) PoE switch for some additional equipment
- a few [Ubiquiti NanoHD](https://unifi-nanohd.ui.com/) access points for wireless connectiviy

I try to keep noisy equipment out of the house, so storage and backups is done off-site. 

## Software

For Home Assistant, I run Debian Buster, using a btrfs root. Docker was added using the standard docker-ce repositories. 
I run two container setups outside of home-assistant:
- [Portainer](https://www.portainer.io/) for container management
- ELK stack for monitoring and logging
This was installed using standard ELK docker-compose files that can be found [here](https://github.com/deviantony/docker-elk)

After getting the base infrastructure in place, home-assistant was installed using the standard [Docker install instructions](https://www.home-assistant.io/docs/installation/docker/).

In home-assistant I do a few things to automate - but there should be much more 'smartness' to it. Partially this is due to lack of sensors (and the inability of most sensors to ignore cats); the other bit that needs to be fixed is proper presence detection.

Things I do do:
- Switch off unneeded power at night. This saves more energy than I thought!


- 'Night mode' triggers when I enable my alarm. 
This works by using the 'sleep cycle' app which can connect to Hue devices. In home-assistant I have a 'fake hue' hub which pretends to be a light. 
The light connected to that is a virtual light, which triggers some automation in appdaemon. The appdaemon script takes care of the following:
- When I switch off the alarm in the morning, switch on the espresso machine, so it's warmed up when I exit the shower.
- If it's a weekday and not a holiday, *and* I woke up after a certain time, I'm working from home, so the espresso machine gets switched on at 12 so I have a heated machine after lunch.

On non-weekdays or holidays, the machine gets switched on at around 11 only.
The appdaemon scripts and configs are in the apps/ section of this repo.



- Some node-red automation around the lights upstairs. 
I control these using Ikea wireless switches. I have two lights next to the bed, and one bigger light. These are switched on and off depending on state:
- When the bed lights are off, and that side's button gets pushed, both bed lights and the big light switch on.
- When the bed lights and the big lights are on, and one of the 'off' buttons gets pushed, that side's light switches off, along with the big light.
- When only one light is on, and that side's 'off' button gets pushed, only that light switches off.

This convuluted automation takes care of our before-sleeping routines :)



- Some simple automation using light groups for switching off and on all of the 'media stuff' at the same time. 




Todo:
- Proper presence detection
- Proper sensor automation (occupancy / movement)
- More graphs and measurements around humidity and air quality
- Some switches for lights that are not switchable yet. Replacing of physical wall switches by Shelly or the like.
