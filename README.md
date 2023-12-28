# Pico WiFi Duck - Raspberry Pi Pico W

![Raspberry Pi Pico W](https://cdn.mos.cms.futurecdn.net/Xmn9ztSwKavDfzgX6x3g4g.jpg)

## Overview

Pico WiFi Duck is a project that enables the emulation of a USB Rubber Ducky over Wi-Fi using the Raspberry Pi Pico W. This functionality allows for remote control and automation of target systems, making it a versatile tool for penetration testing and security assessments. This project is inspired by the [WIFI DUCK](https://github.com/spacehuhntech/wifiduck) project by [spacehuhn](https://github.com/SpacehuhnTech).

## Features

- Emulates USB Rubber Ducky functionality over Wi-Fi.
- Remote scripting and automation capabilities.
- Requires only one Microcontroller.
- Based on the [pico-ducky](https://github.com/dbisu/pico-ducky) project.
- Cost-effective, approximately $6 (40dt).

## Getting Started

### Prerequisites

- Raspberry Pi Pico W.
- Micro-USB Cable.
- Basic Knowledge.

### Installation

1. **Install CircuitPython:**

   - Click [here](https://adafruit-circuit-python.s3.amazonaws.com/bin/raspberry_pi_pico_w/fr/adafruit-circuitpython-raspberry_pi_pico_w-fr-8.0.0.uf2) to download (Version 8.0.0).
   - Plug the device into a USB port while holding the boot button. It will show up as a removable media device named RPI-RP2.
   - Copy the downloaded (".uf2") file to the root of the Pico (RPI-RP2). The device will reboot and after a second or so, it will reconnect as CIRCUITPY.

2. **Install Pico Wifi Duck Files on the Pico:**
   - Download the release file from [here](https://github.com/majdsassi/Pico-WIFI-Duck/releases/download/Release/Relese.zip).
   - Unzip it.
   
    ![](https://gcdnb.pbrd.co/images/D8EojIfPHI9v.jpg?o=1)
   - While plugging in your Pico, copy and paste the files that you unzip onto the "CIRCUITPY" drive.
   
     ![](https://gcdnb.pbrd.co/images/WuZOVmyUAWF4.jpg?o=1)

### Usage

1. Connect your Raspberry Pi Pico W to the target system using a good-quality USB cable.

2. Connect to the WiFi network created by the Pico; it's called **"Pico Wifi Duck"**, and its password is **"pico123456"**.

   ![WIFI CONNECTION](https://gcdnb.pbrd.co/images/Nm86ZhwCuXth.jpg?o=1)

3. Open your browser and navigate to [192.168.4.1](http://192.168.4.1).

   ![Webpage](https://gcdnb.pbrd.co/images/Qrj5szwW56B3.jpg?o=1)

4. Write your script in the textarea, and please make sure to end your script with an empty line. If you know of any solutions for this issue, feel free to share.

### Note
This project is still under development, and it may contain some errors.
Dont Forget to end Your Script with an empty line .
