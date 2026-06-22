import os
import json

def build_manifest():
    manifest = {'Setlists': {'_root_': []}, 'Resources': {}}

    # Scan 'Setlists' folder
    if os.path.exists('Setlists'):
        for item in os.listdir('Setlists'):
            item_path = os.path.join('Setlists', item)
            if os.path.isdir(item_path):
                # It's a band folder
                files = [f for f in os.listdir(item_path) if f.endswith('.txt')]
                manifest['Setlists'][item] = sorted(files)
            elif item.endswith('.txt'):
                # It's a root file
                manifest['Setlists']['_root_'].append(item)
        manifest['Setlists']['_root_'].sort()

    # Scan 'Resources' folder
    if os.path.exists('resources'):
        for band in os.listdir('resources'):
            band_path = os.path.join('resources', band)
            if os.path.isdir(band_path):
                files = [f for f in os.listdir(band_path) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]
                manifest['Resources'][band] = sorted(files)
    
    return manifest

if __name__ == '__main__':
    with open('manifest.json', 'w') as f:
        json.dump(build_manifest(), f, indent=4)
