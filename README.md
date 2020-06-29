# rvdm's Home Assistant Configuration Files
![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg) ![GitHub Activity](https://img.shields.io/github/last-commit/rvdm/home-assistant.svg)


# Physical Setup

I'm running my Home Assistant install using [Home Assistant Core](https://github.com/home-assistant/core) on a small Intel NUC machine in my utility closet.
The NUC is connected and integrated in my home network and a mix of home automation hardware and software.

## Hardware

- [Intel NUC NUC7i3BNK](https://www.intel.com/content/www/us/en/products/boards-kits/nuc/kits/nuc7i3bnk.html)
I stuffed this with 16GB of RAM and a 512GB Western Digital NVME drive.
- [Conbee II](https://phoscon.de/en/conbee2) USB stick for Zigbee connectivity
- [Eneco Toon](https://www.home-assistant.io/integrations/toon/) thermostat
- An old Vera Lite Z-wave controller. It's end of life, but I still use it as a cheap z-wave integration for home-assistant. Should eventually be replaced by a Z-wave stick :)

The above devices connect to a number of 'smart' devices in our home:
- Quite a few [GreenWave Reality Smart PowerNodes](https://products.z-wavealliance.org/products/54). These are smart z-wave power blocks with 6 EU power plug connectors that each are switchable and measure power consumption. They're not great quality, but they work for now.
- Some single [Fibaro Wall Plugs](https://www.fibaro.com/en/products/wall-plug/). They switch nice and fast, are stable, small and report power as well. 
- Lots of [TRÅDFRI](https://www.ikea.com/us/en/cat/smart-lighting-36812/) Zigbee bulbs. Cheap, work well with the Conbee II stick.
- A few TRÅDFRI switches (on/off and the round multi-button switch) for physically triggering scenes or switching power.
- A [Xiaomi 'smart humidifier'](https://xiaomi-mi.com/appliances/smartmi-zhimi-air-humidifier-2-white/) (WiFi)
- [Bosch fridge/freezer](https://www.bosch-home.nl/productoverzicht/KGN36HI32) with wifi and door-triggered cameras
- [Siemens dishwasher](https://www.siemens-home.bsh-group.com/nl/productoverzicht/SN278I26TE) with wifi
- [Roku Ultra](https://www.roku.com/products/roku-ultra) for media playing
- [Ikea Symfonisk](https://www.ikea.com/nl/nl/p/symfonisk-wifi-boekenplankspeaker-zwart-50357554/) Sonos 'clone'
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

