# Material Theme for Spicetify

A clean, modern theme for [Spicetify](https://github.com/spicetify/spicetify-cli), inspired by Google's Material You design language.

## 📸 Screenshots

![image](https://github.com/user-attachments/assets/bb141fdd-8dbb-489a-ab7f-313f2c7009f7)
![{F3EB99F7-605E-49DC-A0CE-A4BE1F4953ED}](https://github.com/user-attachments/assets/8d50a964-5333-4ebb-938f-0d362c6aded3)



## 📦 Features
- Material You inspired look and feel
- Light and dark color schemes
- Easy color customization
- Responsive and clean interface

## ⚡ Requirements
- [Spotify Desktop](https://www.spotify.com/download/)
- [Spicetify CLI](https://github.com/spicetify/spicetify-cli)

## 🛠️ Installation

### 1. Install Spicetify CLI
If you haven't installed Spicetify yet, follow the [official guide](https://spicetify.app/docs/getting-started/installation) or run:

```sh
# Windows (PowerShell)
Invoke-WebRequest -UseBasicParsing "https://raw.githubusercontent.com/spicetify/spicetify-cli/master/install.ps1" | Invoke-Expression

# macOS/Linux
curl -fsSL https://raw.githubusercontent.com/spicetify/spicetify-cli/master/install.sh | sh
```

### 2. Backup your current Spicetify config (optional)
```sh
spicetify backup apply
```

### 3. Download this theme
Clone or download this repository into your Spicetify Themes folder:

```
%userprofile%\AppData\Local\spicetify\Themes\Material
```

Or clone via git:
```sh
git clone https://github.com/yourusername/material-spicetify.git "%userprofile%\AppData\Local\spicetify\Themes\Material"
```

## 🚀 Usage

Apply the theme with:
```sh
spicetify config current_theme Material
spicetify apply
```

## 🎨 Customization
- Edit `color.ini` to change the main color palette.
- Use `all_colors_dark.ini` or `all_colors_light.ini` for full color overrides.
- Advanced: Use `convert_colors.py` to generate color files from palettes.

## 🧩 Troubleshooting
- If Spotify updates and the theme breaks, run:
  ```sh
  spicetify backup restore
  spicetify apply
  ```
- Make sure Spicetify and Spotify are up to date.

## 🚧 Future Plans
- Add more diverse color schemes (palettes)
- Improve and expand theme settings
- Implement additional customization options
- Introduce other enhancements for user convenience

## 📚 Useful Links
- [Spicetify Docs](https://spicetify.app/docs/)
- [Spicetify Themes Gallery](https://github.com/spicetify/spicetify-themes)

---

**Enjoy your personalized Material You experience in Spotify!**
