# YAML Config Tool for Pterodactyl

This is a simple and modern tool to help you easily generate or extend a `config.yml` file for Pterodactyl.

It was built to work with [My Tutorial](https://youtu.be/AsGPjArpSsw?si=Y4ESXsvpV4ZOtEOg) and designed to simplify the process of preparing your server config — especially when setting up the daemon or reconfiguring it manually.

---

## ✨ Features

- 🧠 Paste a raw config directly from your clipboard (e.g. copied from the Pterodactyl panel)
- 📂 Load an existing `config.yml` file from disk
- 🛠️ Automatically injects required system and Docker configuration
- 🎲 Customize internal IP ranges (172.20.0.0/16 to 172.29.0.0/16)
- 💾 Saves the updated config back to a clean `.yml` file
- 🎨 Dark modern GUI theme for a user-friendly experience

---

## 🖱️ How to Use

1. **Launch the tool**
2. Choose:
   - 📋 "Paste from Clipboard" to use a config copied from your browser
   - 📁 "Select Existing Config File" to load one from your PC
3. Pick your **preferred Docker IP range** (e.g. 27 = `172.27.0.1`) - 27 Is what I Like
4. Click `Generate Config`
5. The final config will be saved as `generated_config.yml` in the same folder

---

## 📦 Requirements

No manual setup required — just run the `.exe`.  
(If you're running from source, you’ll need Python 3 and the following Python packages: `pyyaml`, `ttkthemes`, `tkinter`.)

---

## 📌 Notes

- The output is compatible with modern Pterodactyl Daemon installations.

---
