import re
import os

def extract_rgb(color_str):
    # Extract RGB values from string like "rgb(145 213 172)"
    match = re.search(r'rgb\((\d+)\s+(\d+)\s+(\d+)\)', color_str)
    if match:
        r, g, b = map(int, match.groups())
        return f"{r:02x}{g:02x}{b:02x}"
    return None

def clean_var_name(var_name):
    # Remove leading -- and all dashes
    return var_name.lstrip('-').replace('-', '')

def convert_md_to_ini(md_file):
    with open(md_file, 'r') as f:
        content = f.read()
    
    # Extract all color variables
    colors = {}
    for line in content.split('\n'):
        if line.strip().startswith('--'):
            parts = line.strip().split(':')
            if len(parts) == 2:
                name = clean_var_name(parts[0].strip())
                value = parts[1].strip().rstrip(';')
                hex_value = extract_rgb(value)
                if hex_value:
                    colors[name] = hex_value
                else:
                    colors[name] = value
    
    # Generate ini content
    ini_content = "[material-colors]\n; All Material CSS variables, names cleaned\n\n"
    for name, value in colors.items():
        ini_content += f"{name} = {value}\n"
    return ini_content

def main():
    # Get the directory of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    material_color_dir = os.path.join(script_dir, 'material-color')
    
    # Process both dark and light themes
    for theme in ['dark', 'light']:
        md_file = os.path.join(material_color_dir, f'{theme}.css')
        if os.path.exists(md_file):
            ini_content = convert_md_to_ini(md_file)
            output_file = os.path.join(script_dir, f'all_colors_{theme}.ini')
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(ini_content)
            print(f"Generated {output_file}")

if __name__ == "__main__":
    main() 