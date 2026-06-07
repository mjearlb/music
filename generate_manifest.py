import os
import json

def build_manifest():
    manifest = {}

    # 1. Scan Backups
    for item in os.listdir('.'):
        if os.path.isdir(item) and item.startswith('Backup'):
            manifest[item] = {}
            for band in os.listdir(item):
                band_path = os.path.join(item, band)
                if os.path.isdir(band_path):
                    files = [f for f in os.listdir(band_path) if f.endswith('.txt')]
                    manifest[item][band] = sorted(files)

    # 2. Scan Resources (Auto-detect folders inside)
    if os.path.exists('resources'):
        manifest['Resources'] = {}
        for band in os.listdir('resources'):
            band_path = os.path.join('resources', band)
            if os.path.isdir(band_path):
                # Include images
                files = [f for f in os.listdir(band_path) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]
                manifest['Resources'][band] = sorted(files)
    
    return manifest

if __name__ == '__main__':
    with open('manifest.json', 'w') as f:
        json.dump(build_manifest(), f, indent=4)
    print("✨ manifest.json updated with Resources!")
