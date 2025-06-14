# Power Sensor Lamp Automation with Adaptive Lighting & Alert

Automatically control a lamp based on the power usage of any device with a smart power sensor.

This Home Assistant **Blueprint** fades your lamp in and out based on device use, adapts the lighting to the time of day, and can send a voice alert (plus a colored lamp warning) if the device is left running too long. Works great for turntables, coffee makers, fans, irons, or any device you want to monitor!

---

## Features

* **Lamp on/off** based on device power usage (customizable thresholds)
* **Adaptive fade-in/fade-out** for the lamp
* **Adaptive color temperature and brightness** based on the time of day
* **"Running too long" alert**: lamp changes color and sends a voice notification via Home Assistant speaker
* **All options configurable via UI** (no YAML editing required after import)
* **Reusable for any powered device** with a measurable power sensor

---

## Installation

### 1. Import the Blueprint from GitHub

Copy and paste this raw URL in Home Assistant's blueprint import:

```
https://raw.githubusercontent.com/johnstetter/home-assistant-blueprints/main/blueprints/automations/johnstetter/power_sensor_lamp_automation/power_sensor_lamp_automation.yaml
```

* Go to **Settings > Automations & Scenes > Blueprints**
* Click **Import Blueprint** (top right)
* Paste the raw URL above, hit **Preview** and then **Import**

---

### 2. Create a Timer Helper

* Go to **Settings > Devices & Services > Helpers**
* Add a **Timer** (e.g., `timer.device_running_too_long`)

---

### 3. Create an Automation from the Blueprint

* Go to **Settings > Automations & Scenes > + Create Automation**
* Choose **“Use Blueprint”**
* Pick **Power Sensor Lamp Automation with Adaptive Lighting & Alert**
* Fill in:

  * **Power Sensor:** E.g., `sensor.coffee_maker_power` or `sensor.record_player_electric_consumption_w`
  * **Lamp:** The lamp to control (must support color\_temp and/or RGB for full features)
  * **Media Player:** Where you want the voice alert (e.g., a Home Assistant voice speaker)
  * **Timer Helper:** The timer you created above
  * Set power thresholds, fade times, alert color, duration, and custom voice message as desired

---

## Customization & Tips

* **Thresholds**: Adjust for your device's "on" and "off" wattages
* **Adaptive lighting**: Defaults work for most, but can be customized in the YAML if needed
* **Alert color/message**: Pick your own color and announcement text
* **Works for any device**: Not just lamps—use it for any alert scenario where power is the trigger!

---

## Troubleshooting & Notes

* Your lamp should support `color_temp` or `rgb_color` for adaptive/alert features to work fully
* Voice message is fully customizable and supports the `{{ minutes }}` template variable for the timer duration
* Works with any Home Assistant-compatible TTS service (e.g., `tts.cloud_say`)
* If the lamp doesn't turn on or off as expected, adjust the power thresholds or fade timings

---

## Directory Structure

This blueprint is located here:

```
blueprints/automations/johnstetter/power_sensor_lamp_automation/
```

* `power_sensor_lamp_automation.yaml` — the blueprint YAML
* `README.md` — this file

---

## License

MIT License. Use, share, and enjoy!

---

## Credits

Created by John Stetter, designed for practical, real-world automation. If you find this useful, give a shout or a PR!

