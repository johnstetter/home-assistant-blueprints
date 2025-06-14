# 🎶 Turntable Lamp Automation with Adaptive Lighting & Notification

**Let your lamp follow your vinyl.**  
This Home Assistant **Blueprint** automatically fades in your lamp when your record player is spinning, adapts lighting to the time of day, and warns you if you forget to stop the music.

---

## Features

- **Fade-in/fade-out:** Smooth transitions for lamp on/off.
- **Adaptive color & brightness:** Matches time of day—bright & cool in the morning, warm at night.
- **Forgetful-proof:** Sends a voice alert and turns the lamp red if the turntable runs too long.
- **All options UI-configurable:** No YAML wrangling needed after setup.

---

## How To Install This Blueprint

### 1. **Direct Import from GitHub**

Just click the link below, or paste the raw URL into Home Assistant’s **Blueprint import**:

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://github.com/johnstetter/home-assistant-blueprints/raw/main/turntable_lamp_adaptive.yaml)

Or use this raw link in the import dialog:
https://github.com/johnstetter/home-assistant-blueprints/raw/main/turntable_lamp_adaptive.yaml


**How to do it:**
1. Go to **Settings > Automations & Scenes > Blueprints**
2. Click **“Import Blueprint”** (top right)
3. Paste the raw GitHub URL above, then hit **Preview** and **Import**

---

### 2. **Create a Timer Helper**

- Go to **Settings > Devices & Services > Helpers**
- Click **Create Helper** > **Timer**
- Name it (e.g. `timer.record_player_running_too_long`)

---

### 3. **Create Your Automation from the Blueprint**

- Go to **Settings > Automations & Scenes > + Create Automation**
- Pick **“Use Blueprint”**
- Choose **Turntable Lamp Automation with Adaptive Lighting & Notification**
- Fill out:
    - **Power Sensor:** E.g. `sensor.record_player_electric_consumption_w`
    - **Lamp:** E.g. `light.turntable_lamp`
    - **Media Player:** E.g. `media_player.living_room_home_assistant_voice_pe_media_player`
    - **Timer Helper:** The one you just made
    - Adjust thresholds, fade times, alert color, duration, etc.

---

## Customization

- **Thresholds:** Tune for your turntable’s wattage (on/off)
- **Fade Duration:** How fast the mood shifts
- **Colors/Temperature:** Defaults are adaptive, tweak if you want
- **Timer/Notifications:** Set your own “left running” interval, red light style, and voice message

---

## Troubleshooting & Tips

- Lamp must support `color_temp` and/or `rgb_color` for best results (otherwise, edit YAML for your setup)
- This works for any powered device—not just record players!
- For more/less sass in the voice alert, edit the announcement message in the blueprint YAML

---

## Credits

Inspired by John Stetter’s love of vinyl and his refusal to let the music stop—or run all night.

MIT License. Use, fork, and enjoy.

---


