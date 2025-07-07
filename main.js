const { app, BrowserWindow, ipcMain, dialog } = require('electron');
const path = require('path');
const fs = require('fs');
const yaml = require('js-yaml');

let mainWindow;
let startupWindow;

function createStartupWindow() {
  startupWindow = new BrowserWindow({
    width: 400,
    height: 300,
    frame: false,
    transparent: true,
    resizable: false,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false
    },
    icon: path.join(__dirname, 'app_icon.ico')
  });

  startupWindow.loadFile('startup.html');
  
  // Center the window
  startupWindow.center();
  
  // Remove menu bar
  startupWindow.setMenu(null);
}

function createMainWindow() {
  mainWindow = new BrowserWindow({
    width: 1200,
    height: 800,
    frame: false,
    transparent: true,
    resizable: true,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false
    },
    icon: path.join(__dirname, 'app_icon.ico'),
    show: false
  });

  mainWindow.loadFile('index.html');
  
  // Center the window
  mainWindow.center();
  
  // Remove menu bar
  mainWindow.setMenu(null);
  
  // Show window when ready
  mainWindow.once('ready-to-show', () => {
    mainWindow.show();
  });
}

app.whenReady().then(() => {
  createStartupWindow();
  
  // After 3 seconds, close startup and open main window
  setTimeout(() => {
    if (startupWindow) {
      startupWindow.close();
    }
    createMainWindow();
  }, 3000);
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (BrowserWindow.getAllWindows().length === 0) {
    createMainWindow();
  }
});

// IPC handlers
ipcMain.handle('select-output-directory', async () => {
  const result = await dialog.showOpenDialog(mainWindow, {
    properties: ['openDirectory'],
    title: 'Select Output Directory'
  });
  
  if (!result.canceled) {
    return result.filePaths[0];
  }
  return null;
});

ipcMain.handle('browse-yaml-file', async () => {
  const result = await dialog.showOpenDialog(mainWindow, {
    properties: ['openFile'],
    filters: [
      { name: 'YAML files', extensions: ['yaml', 'yml'] }
    ],
    title: 'Select YAML File'
  });
  
  if (!result.canceled) {
    return result.filePaths[0];
  }
  return null;
});

ipcMain.handle('generate-yaml-config', async (event, data) => {
  try {
    let config;
    
    if (data.filePath) {
      // Load from file
      const fileContent = fs.readFileSync(data.filePath, 'utf8');
      config = yaml.load(fileContent);
    } else if (data.pastedConfig) {
      // Load from pasted content
      config = yaml.load(data.pastedConfig);
    } else {
      throw new Error('No YAML content provided');
    }

    // Generate random number if not provided or invalid
    let number = data.networkNumber;
    if (!number || number < 20 || number > 29) {
      number = Math.floor(Math.random() * 10) + 20;
    }

    // Update system configuration
    if (!config.system || typeof config.system !== 'object') {
      config.system = {};
    }

    Object.assign(config.system, {
      'root_directory': '/mnt/user/appdata/pterodactyldeamons/lib',
      'log_directory': '/var/log/pterodactyl',
      'archive_directory': '/mnt/user/appdata/pterodactyldeamons/lib/archives',
      'backup_directory': '/mnt/user/appdata/pterodactyldeamons/lib/backups',
      'tmp_directory': '/tmp/pterodactyl',
    });

    // Add Docker configuration
    config.docker = {
      'network': {
        'interface': `172.${number}.0.1`,
        'dns': ['1.1.1.1', '1.0.0.1'],
        'name': 'pterodactyl_nw',
        'ispn': false,
        'driver': 'bridge',
        'network_mode': 'pterodactyl_nw',
        'is_internal': false,
        'enable_icc': true,
        'interfaces': {
          'v4': {
            'subnet': `172.${number}.0.0/16`,
            'gateway': `172.${number}.0.1`
          },
          'v6': {
            'subnet': 'fdba:17c8:6c94::/64',
            'gateway': 'fdba:17c8:6c94::1011'
          }
        }
      },
      'domainname': '',
      'registries': {},
      'tmpfs_size': 100
    };

    // Determine output path
    let outputDir = data.outputDirectory;
    if (!outputDir) {
      if (data.filePath) {
        outputDir = path.dirname(data.filePath);
      } else {
        outputDir = process.cwd();
      }
    }

    const outputPath = path.join(outputDir, 'final_config.yaml');
    const yamlContent = yaml.dump(config, { sortKeys: false });
    fs.writeFileSync(outputPath, yamlContent);

    return {
      success: true,
      outputPath: outputPath,
      networkNumber: number
    };
  } catch (error) {
    return {
      success: false,
      error: error.message
    };
  }
});

ipcMain.handle('minimize-window', () => {
  mainWindow.minimize();
});

ipcMain.handle('maximize-window', () => {
  if (mainWindow.isMaximized()) {
    mainWindow.unmaximize();
  } else {
    mainWindow.maximize();
  }
});

ipcMain.handle('close-window', () => {
  mainWindow.close();
}); 