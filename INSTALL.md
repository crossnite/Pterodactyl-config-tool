# Installation Guide

## Quick Start (For Users)

### Download Pre-built Executable
1. Go to the [Releases page](https://github.com/yourusername/config-tool-v2/releases)
2. Download the latest `.exe` file
3. Run the installer
4. Launch from desktop or start menu

## Building from Source

### Prerequisites
- **Windows 10/11** (64-bit)
- **Node.js** v16 or higher
- **npm** (comes with Node.js)

### Step 1: Install Node.js
1. Download Node.js from [https://nodejs.org/](https://nodejs.org/)
2. Choose the LTS version (recommended)
3. Run the installer and follow the setup wizard
4. Verify installation by opening Command Prompt and typing:
   ```bash
   node --version
   npm --version
   ```

### Step 2: Download Source Code
**Option A: Using Git (Recommended)**
```bash
git clone https://github.com/yourusername/config-tool-v2.git
cd config-tool-v2
```

**Option B: Download ZIP**
1. Click the green "Code" button on GitHub
2. Select "Download ZIP"
3. Extract the ZIP file
4. Open Command Prompt in the extracted folder

### Step 3: Install Dependencies
```bash
npm install
```

### Step 4: Run the Application
```bash
npm start
```

## Building Executable

### Manual Build
```bash
# Install electron-builder globally
npm install -g electron-builder

# Build the executable
npm run dist
```

The executable will be created in the `dist` folder.

## Troubleshooting

### Common Issues

**"node is not recognized"**
- Node.js is not installed or not in PATH
- Restart Command Prompt after installing Node.js
- Reinstall Node.js if the issue persists

**"npm is not recognized"**
- npm comes with Node.js
- Ensure Node.js is properly installed
- Try running as administrator

**Build fails**
- Ensure you're in the correct directory
- Clear npm cache: `npm cache clean --force`
- Delete `node_modules` folder and run `npm install` again

**Permission errors**
- Run Command Prompt as administrator
- Check Windows Defender settings
- Ensure antivirus isn't blocking the build process

### Getting Help
- Check the [main README](README.md) for detailed information
- Join our [Discord server](https://discord.gg/aqfm8T5U2t) for support
- Open an issue on GitHub if you encounter bugs

## System Requirements

### Minimum Requirements
- **OS**: Windows 10 (64-bit)
- **RAM**: 4GB
- **Storage**: 100MB free space
- **Network**: Internet connection for initial setup

### Recommended Requirements
- **OS**: Windows 11 (64-bit)
- **RAM**: 8GB
- **Storage**: 500MB free space
- **Network**: Stable internet connection 