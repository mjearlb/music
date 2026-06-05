import os
import json

def build_manifest():
    manifest = {}

    # Scan root for folders starting with "Backup"
    for item in os.listdir('.'):
        if os.path.isdir(item) and item.startswith('Backup'):
            manifest[item] = {}
            for band in os.listdir(item):
                band_path = os.path.join(item, band)
                if os.path.isdir(band_path):
                    # Gather and sort all text files
                    files = [f for f in os.listdir(band_path) if f.endswith('.txt')]
                    files.sort()
                    manifest[item][band] = files
    return manifest

if __name__ == '__main__':
    data = build_manifest()
    with open('manifest.json', 'w') as f:
        json.dump(data, f, indent=4)
    print("✨ manifest.json generated successfully!")
