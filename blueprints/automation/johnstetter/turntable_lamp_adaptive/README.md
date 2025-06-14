# 🎶 Turntable Lamp Automation with Adaptive Lighting & Notification

Let your lamp vibe with your vinyl.  
This Home Assistant **Blueprint** will:

- **Fade in** your lamp with the right color and brightness for the time of day when you play a record
- **Turn off** the lamp when the record stops
- **Warn you** (voice + red lamp) if you leave the record spinning too long

---

## Features

- **Smooth fade-in/fade-out** transitions
- **Adaptive lighting** by time of day (morning = bright/cool, evening = warm)
- **Configurable “left running” reminder**—voice + red alert lamp
- **Everything is configurable from the UI** (no YAML edits needed!)

---

## How to Install

### 1. Import the Blueprint from GitHub

#### **Copy and paste this RAW URL in Home Assistant’s blueprint import:**

https://raw.githubusercontent.com/johnstetter/home-assistant-blueprints/main/blueprints/automations/johnstetter/turntable_lamp_adaptive/turntable_lamp_adaptive.yaml


- Go to **Settings > Automations & Scenes > Blueprints**
- Click **Import Blueprint** (top right)
- Paste the raw URL above, hit **Preview** and then **Import**

Or click this badge if your HA supports it:  
[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?external_url=https://raw.githubusercontent.com/johnstetter/home-assistant-blueprints/main/blueprints/automations/johnstetter/turntable_lamp_adaptive/turntable_lamp_adaptive.yaml)

---

### 2. Create a Timer Helper

- Go to **Settings > Devices & Services > Helpers**
- Add a **Timer** (e.g. `timer.record_player_running_too_long`)

---

### 3. Create an Automation from the Blueprint

- Go to **Settings > Automations & Scenes > + Create Automation**
- Choose **“Use Blueprint”**
- Pick **Turntable Lamp Automation with Adaptive Lighting & Notification**
- Fill in:
    - **Power Sensor:** e.g. `sensor.record_player_electric_consumption_w`
    - **Lamp:** e.g. `light.turntable_lamp`
    - **Media Player:** e.g. `media_player.living_room_home_assistant_voice_pe_media_player`
    - **Timer Helper:** your timer from above
    - Adjust thresholds, fade times, alert colors, and durations as you like

---

## Repo Structure

This blueprint lives here:  
`blueprints/automations/johnstetter/turntable_lamp_adaptive/`

- `turntable_lamp_adaptive.yaml` — the blueprint YAML file
- `README.md` — this file!

---

## Customization

- Tweak thresholds, fade, colors, alert duration all from the UI
- Voice announcement and alert lamp color are customizable
- Works for any powered device, not just turntables

---

## Troubleshooting & Notes

- Lamp should support `color_temp` and/or `rgb_color` for full effect (edit YAML for other lamp types)
- Want to tweak the sass? Edit the notification message in the blueprint YAML
- Fork it, PR it, use it for your espresso machine—no rules here

---

## Credits

Created by [John Stetter](https://github.com/johnstetter)  
Powered by vinyl, caffeine, and “wait, did I leave that spinning?”

MIT License. Share & enjoy.


