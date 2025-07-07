# Release Notes

## Version 2.0.0 - 

### ✨ New Features
- **Modern UI**: Clean, translucent design
- **YAML Configuration Tool**: Generate and extend Pterodactyl config files
- **Multiple Input Methods**: Paste from clipboard or load from file
- **Custom Network Configuration**: Choose Docker IP ranges (172.20.0.0/16 to 172.29.0.0/16)
- **Transparency Settings**: Adjust UI transparency and blur intensity
- **Cross-platform**: Built with Electron for Windows, macOS, and Linux

### 🛠️ Technical Features
- **YAML Processing**: Full YAML parsing and generation with js-yaml
- **System Integration**: Automatic injection of Pterodactyl system paths
- **Docker Network Setup**: Complete Docker network configuration
- **Error Handling**: Comprehensive error messages and validation
- **File Management**: Native file dialogs and clipboard integration

### 🎨 UI/UX Improvements
- **Startup Animation**: Beautiful animated startup screen
- **Smooth Transitions**: Page transitions and hover effects
- **Custom Titlebar**: Modern window controls
- **Responsive Design**: Adapts to different window sizes
- **Dark Theme**: Modern dark interface with customizable transparency

### 📁 File Structure
```
config-tool-v2/
├── main.js              # Main Electron process
├── index.html           # Main application window
├── startup.html         # Startup screen
├── package.json         # Project configuration
├── app_icon.ico         # Application icon
├── build.bat            # Windows build script
├── build.ps1            # PowerShell build script
├── README.md           # Documentation
├── INSTALL.md          # Installation guide
└── RELEASE_NOTES.md    # This file
```

### 🔧 Build System
- **Electron Builder**: Automated build process
- **NSIS Installer**: Professional Windows installer
- **Auto-updates**: Ready for future update system
- **Code Signing**: Prepared for code signing

### 📋 System Requirements
- **OS**: Windows 10/11 (64-bit)
- **RAM**: 4GB minimum (8GB recommended)
- **Storage**: 100MB free space
- **Network**: Internet connection for initial setup

### 🚀 Installation
1. Download the installer from the releases page
2. Run `ConfigToolV2-Setup`
3. Follow the installation wizard
4. Launch from desktop or start menu

### 🐛 Known Issues
- None reported

### 🔮 Future Plans
- Auto-update system


---

**Config Tool V2** - Simplifying Pterodactyl configuration management since 2025 ✨ 
