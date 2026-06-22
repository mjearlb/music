import os
import json

def build_manifest():
    manifest = {}

    # 1. Scan the new 'Setlists' folder
    if os.path.exists('Setlists'):
        # We treat 'Setlists' as the top-level key in the manifest
        manifest['Setlists'] = {}
        for band in os.listdir('Setlists'):
            band_path = os.path.join('Setlists', band)
            if os.path.isdir(band_path):
                files = [f for f in os.listdir(band_path) if f.endswith('.txt')]
                manifest['Setlists'][band] = sorted(files)

    # 2. Scan Resources (remains the same)
    if os.path.exists('resources'):
        manifest['Resources'] = {}
        for band in os.listdir('resources'):
            band_path = os.path.join('resources', band)
            if os.path.isdir(band_path):
                files = [f for f in os.listdir(band_path) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]
                manifest['Resources'][band] = sorted(files)
    
    return manifest

if __name__ == '__main__':
    with open('manifest.json', 'w') as f:
        json.dump(build_manifest(), f, indent=4)
    print("✨ manifest.json updated with Setlists and Resources!")
