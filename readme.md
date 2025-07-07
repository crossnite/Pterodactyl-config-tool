# Config Tool V2

A modern YAML configuration tool for Pterodactyl with a clean, translucent design. Built with Electron and featuring smooth animations, a beautiful UI, and intuitive YAML configuration generation.

## 🎯 Purpose

This is a simple and modern tool to help you easily generate or extend a `config.yml` file for Pterodactyl. It was built to work with tutorials and designed to simplify the process of preparing your server config — especially when setting up the daemon or reconfiguring it manually.

## ✨ Features

- 🎨 **Modern UI**: Clean, translucent design with smooth animations
- 📋 **Paste from Clipboard**: Use YAML config copied from your browser
- 📁 **Load from File**: Select existing YAML files from your system
- 🛠️ **Auto Configuration**: Automatically injects required system and Docker settings
- 🎲 **Custom IP Ranges**: Choose Docker network ranges (172.20.0.0/16 to 172.29.0.0/16)
- 💾 **Smart Output**: Saves as `final_config.yaml` with proper formatting
- ⚙️ **Customizable**: Adjust transparency and blur settings
- 🖥️ **Cross-platform**: Works on Windows, macOS, and Linux

## 📦 Installation

### Option 1: Download Pre-built Executable (Recommended)

1. Download the latest release from the [Releases page](https://github.com/crossnite/Pterodactyl-config-tool/releases)
2. Run the installer and follow the setup wizard
3. Launch the application from your desktop or start menu

### Option 2: Build from Source

#### Prerequisites
- **Node.js** (v16 or higher) - [Download here](https://nodejs.org/)
- **npm** (comes with Node.js)
- **Git** (optional, for cloning)

#### Setup Instructions

1. **Clone or download the repository**
   ```bash
   git clone https://github.com/crossnite/Pterodactyl-config-tool.git
   cd config-tool-v2
   ```
   
   Or download and extract the ZIP file, then navigate to the folder.

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Run the application**
   ```bash
   npm start
   ```

#### Building the Executable

To create a distributable executable:

```bash
# Install electron-builder globally (one-time setup)
npm install -g electron-builder

# Build for Windows
npm run dist
```

The executable will be created in the `dist` folder.

## 🖱️ How to Use

### Basic Usage

1. **Launch Config Tool V2**
2. **Choose Input Method**:
   - 📋 Click "Paste from Clipboard" to use YAML copied from your browser
   - 📁 Click "Browse YAML File" to load an existing config file
3. **Configure Network**:
   - Enter your preferred Docker IP range (20-29, e.g., 27 = `172.27.0.1`)
   - Leave blank for random selection
4. **Select Output** (Optional):
   - Choose where to save the generated config
   - Defaults to the same folder as input file or current directory
5. **Generate**: Click "Generate YAML Config"
6. **Result**: The final config is saved as `final_config.yml`

### Advanced Features

#### Settings Tab
- **Theme**: Choose between Dark, Light, or Auto themes
- **Transparency Level**: 
  - Grey (Non Transparent)
  - Low (Subtle)
  - Dark - Transparent (Default)
  - Darker (More Transparent)
- **Blur Intensity**: Adjust backdrop blur (8px, 12px, 20px)

#### Discord Tab
- Connect with the community for support and updates

## 🛠️ Technical Details

### What the Tool Does

1. **Loads YAML Configuration**: From file or clipboard
2. **Validates YAML**: Ensures proper syntax
3. **Injects System Paths**: Adds required Pterodactyl directories
4. **Configures Docker Network**: Sets up networking with custom IP ranges
5. **Generates Output**: Creates a complete, ready-to-use config file

### Generated Configuration

The tool automatically adds:

```yaml
system:
  root_directory: /mnt/user/appdata/pterodactyldeamons/lib
  log_directory: /var/log/pterodactyl
  archive_directory: /mnt/user/appdata/pterodactyldeamons/lib/archives
  backup_directory: /mnt/user/appdata/pterodactyldeamons/lib/backups
  tmp_directory: /tmp/pterodactyl

docker:
  network:
    interface: 172.{number}.0.1
    dns: [1.1.1.1, 1.0.0.1]
    name: pterodactyl_nw
    # ... complete network configuration
```

## 🚀 Development

### Project Structure
```
config-tool-v2/
├── main.js              # Main Electron process
├── index.html           # Main application window
├── startup.html         # Startup screen
├── package.json         # Project configuration
├── app_icon.ico         # Application icon
└── README.md           # This file
```

### Available Scripts
- `npm start` - Run in development mode
- `npm run dev` - Run with development flags
- `npm run build` - Build for development
- `npm run dist` - Create distributable package

### Technologies Used
- **Electron**: Cross-platform desktop framework
- **HTML5/CSS3**: Modern web technologies
- **JavaScript**: Application logic
- **js-yaml**: YAML parsing and generation
- **Node.js**: Runtime environment

## 📋 Requirements

### For End Users
- **Windows 10/11** (64-bit)
- **4GB RAM** minimum
- **100MB** disk space

### For Developers
- **Node.js** v16+
- **npm** v8+
- **Git** (optional)

## 🐛 Troubleshooting

### Common Issues

**Application won't start**
- Ensure you have the latest version
- Check Windows Defender isn't blocking the app
- Try running as administrator

**YAML parsing errors**
- Verify your YAML syntax is correct
- Check for special characters in the config
- Try pasting the config into a YAML validator first

**Build errors**
- Ensure Node.js version is 16 or higher
- Clear npm cache: `npm cache clean --force`
- Delete `node_modules` and run `npm install` again

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/crossnite/Pterodactyl-config-tool/tree/main?tab=License-1-ov-file) file for details.

## 🙏 Acknowledgments

- Built for the Pterodactyl community
- Inspired by modern UI design principles
- Uses Electron for cross-platform compatibility

---
This software is provided "as is", without warranty of any kind...
**Config Tool V2** - Simplifying Pterodactyl configuration management ✨
