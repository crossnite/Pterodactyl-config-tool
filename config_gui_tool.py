import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import filedialog, messagebox
import yaml
import random
import os
import pyperclip  # You'll need to install this package: pip install pyperclip

class ConfigToolApp:
    def __init__(self, root):
        self.root = root
        self.root.title("YAML Config Tool")
        self.root.geometry("500x450")
        self.file_path = None
        self.pasted_config = None  # to store pasted YAML text

        self.frame = ttk.Frame(root, padding=20)
        self.frame.pack(fill=BOTH, expand=True)

        self.label = ttk.Label(self.frame, text="Select your YAML config", bootstyle="info")
        self.label.pack(pady=10)

        # File browse button
        self.file_button = ttk.Button(self.frame, text="Browse File", command=self.browse_file, bootstyle="secondary-outline")
        self.file_button.pack(pady=5)

        # Paste from clipboard button
        self.paste_button = ttk.Button(self.frame, text="Paste Config from Clipboard", command=self.paste_from_clipboard, bootstyle="secondary-outline")
        self.paste_button.pack(pady=5)

        self.num_label = ttk.Label(self.frame, text="Preferred number (20–29, leave blank for random):", bootstyle="info")
        self.num_label.pack(pady=(20, 5))

        self.number_entry = ttk.Entry(self.frame, width=20)
        self.number_entry.pack()

        self.generate_button = ttk.Button(self.frame, text="Generate Config", command=self.generate_config, bootstyle="success")
        self.generate_button.pack(pady=25)

        self.status = ttk.Label(self.frame, text="", bootstyle="warning")
        self.status.pack()

    def browse_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("YAML files", "*.yaml *.yml")])
        self.pasted_config = None  # reset pasted config if browsing file
        if self.file_path:
            self.status.config(text=f"Selected file: {os.path.basename(self.file_path)}")

    def paste_from_clipboard(self):
        clipboard_text = pyperclip.paste()
        try:
            # Try loading the clipboard text as YAML to validate
            yaml.safe_load(clipboard_text)
            self.pasted_config = clipboard_text
            self.file_path = None  # reset file path if pasting
            self.status.config(text="✅ YAML config pasted from clipboard successfully.", bootstyle="success")
        except Exception:
            self.pasted_config = None
            messagebox.showerror("Error", "Clipboard content is not valid YAML.")
            self.status.config(text="❌ Failed to paste YAML from clipboard.", bootstyle="danger")

    def generate_config(self):
        # Load config from file or from pasted clipboard data
        if self.file_path:
            try:
                with open(self.file_path, 'r') as f:
                    config = yaml.safe_load(f)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load file:\n{str(e)}")
                self.status.config(text="❌ Failed to load YAML file.", bootstyle="danger")
                return
        elif self.pasted_config:
            try:
                config = yaml.safe_load(self.pasted_config)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load pasted YAML:\n{str(e)}")
                self.status.config(text="❌ Failed to load pasted YAML.", bootstyle="danger")
                return
        else:
            messagebox.showerror("Error", "Please select a YAML file or paste YAML from clipboard.")
            return

        try:
            number = self.number_entry.get().strip()
            if not number.isdigit() or not (20 <= int(number) <= 29):
                number = random.randint(20, 29)
                messagebox.showinfo("Info", f"Using random number: {number}")
            else:
                number = int(number)

            if 'system' not in config or not isinstance(config['system'], dict):
                config['system'] = {}

            config['system'].update({
                'root_directory': '/mnt/user/appdata/pterodactyldeamons/lib',
                'log_directory': '/var/log/pterodactyl',
                'archive_directory': '/mnt/user/appdata/pterodactyldeamons/lib/archives',
                'backup_directory': '/mnt/user/appdata/pterodactyldeamons/lib/backups',
                'tmp_directory': '/tmp/pterodactyl',
            })

            config['docker'] = {
                'network': {
                    'interface': f'172.{number}.0.1',
                    'dns': ['1.1.1.1', '1.0.0.1'],
                    'name': 'pterodactyl_nw',
                    'ispn': False,
                    'driver': 'bridge',
                    'network_mode': 'pterodactyl_nw',
                    'is_internal': False,
                    'enable_icc': True,
                    'interfaces': {
                        'v4': {
                            'subnet': f'172.{number}.0.0/16',
                            'gateway': f'172.{number}.0.1'
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
            }

            # Determine output folder and file name
            if self.file_path:
                output_dir = os.path.dirname(self.file_path)
            else:
                output_dir = os.getcwd()  # current working directory if pasted

            output_path = os.path.join(output_dir, "final_config.yaml")
            with open(output_path, 'w') as f:
                yaml.dump(config, f, sort_keys=False)

            messagebox.showinfo("Success", f"Config written to:\n{output_path}")
            self.status.config(text="✅ Config generated successfully.", bootstyle="success")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred:\n{str(e)}")
            self.status.config(text="❌ Failed to generate config.", bootstyle="danger")

if __name__ == "__main__":
    import sys
    try:
        import pyperclip
    except ImportError:
        messagebox.showerror("Dependency Error", "The 'pyperclip' module is required. Please install it via:\npip install pyperclip")
        sys.exit(1)

    app = ttk.Window(themename="darkly")
    ConfigToolApp(app)
    app.mainloop()
