# 💡 Motion-Based Lighting v2.5 – Adaptive & Configurable

A smart Home Assistant blueprint that controls lights and switches based on motion, time of day, and customized room settings.

Designed to be practical, flexible, and elegant — just like your setup, John.

## 🔥 Features

- 🕶️ Adaptive color temperature by time of day
- 💡 Configurable initial brightness
- ⏳ Per-room motion timeout & dimming overrides
- 🌥️ Daytime override mode for gloomy days
- 🧠 Intelligent state handling (won't turn off manually activated lights)
- 🎛️ Optional switch support (e.g., lava lamps, accent lights)
- 🌙 Bedtime shutoff window

## 📦 Inputs

| Name                          | Description                                                         |
|-------------------------------|---------------------------------------------------------------------|
| `motion_sensor`               | Binary motion sensor to trigger the automation                      |
| `lights`                      | Light entities to control                                           |
| `switches`                    | Optional switches to control (e.g., plugs)                          |
| `initial_brightness`          | Default brightness when lights turn on                             |
| `override_initial_brightness` | Per-instance override of initial brightness                        |
| `off_delay`                   | Default delay before starting dimming after no motion (in seconds) |
| `override_off_delay`          | Per-instance override of off delay                                 |
| `dimming_time`                | Delay before turning off after dimming                             |
| `dimming_brightness`          | Minimum brightness before turning off (percent)                    |
| `override_dimming_brightness` | Per-instance override of dimming threshold                         |
| `bedtime`                     | Time after which motion no longer triggers the lights              |
| `daytime_mode`                | Optional override to allow lights during daytime                   |

## 🚀 Usage

To use this blueprint:

1. In Home Assistant, go to *Settings > Automations & Scenes > Blueprints > Import Blueprint*
2. Paste the raw GitHub URL for the YAML file:
https://raw.githubusercontent.com/johnstetter/home-assistant-blueprints/main/blueprints/automation/johnstetter/motion_lighting_adaptive/motion_lighting_adaptive.yaml
3. Fill in your room-specific inputs and hit save.

## 🧠 How It Works

- Only triggers when motion is detected **after sunset** (unless daytime mode is enabled) and **before bedtime**
- If the light was already on before motion, it won’t shut it off after dimming
- Smoothly dims lights over time before shutting them off
- Color temperature adapts based on time of day:
- 5000K during the day
- 4000K early evening
- 3000K later evening
- 2700K at night

## 🛠 Version History

| Version | Notes                                                                 |
|---------|-----------------------------------------------------------------------|
| v2.5    | Per-room overrides, daytime mode, better logic guards                |
| v2.4    | Smart skip dimming if lights were already on, smoother transitions   |
| v2.3    | First public release, adaptive color, configurable brightness & delay|

## 🧑‍💻 Maintainer

**John Stetter**
[GitHub @johnstetter](https://github.com/johnstetter)

Made in Madison, WI with tea, code, and a healthy respect for accessible design. ☕🧠
