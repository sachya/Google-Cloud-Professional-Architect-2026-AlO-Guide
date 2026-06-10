import json
import re
import os

services = []
current_category = "General"
current_service = {}
capture_mode = 0

# Parse output.md
with open('output.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for line in lines:
    line = line.strip()
    if not line:
        continue
    
    # Check for category
    if line.startswith('## '):
        current_category = line.replace('## ', '').strip()
        continue
    
    # Check for service table entries
    if line == '__Service Name__':
        continue # Skip header
    if line in ('__Architectural Category__', '__Primary Operational Capabilities & Developer Utility__', '__Primary Source Citations__'):
        continue
    
    # Match __Service Name__
    match_service = re.match(r'^__(.*)__$', line)
    if match_service:
        # Save previous
        if current_service:
            services.append(current_service)
        
        name = match_service.group(1).replace('\\-', '-').replace('\\(', '(').replace('\\)', ')').replace('\\.', '.')
        current_service = {
            'id': re.sub(r'[^a-z0-9]', '-', name.lower()),
            'name': name,
            'category': current_category,
            'architecturalCategory': '',
            'description': '',
            'features': [],
            'cliExamples': [],
            'iamRoles': []
        }
        capture_mode = 1
        continue
    
    if capture_mode == 1:
        current_service['architecturalCategory'] = line.replace('\\-', '-').replace('\\(', '(').replace('\\)', ')').replace('\\.', '.')
        capture_mode = 2
        continue
    elif capture_mode == 2:
        current_service['description'] = line.replace('\\-', '-').replace('\\(', '(').replace('\\)', ')').replace('\\.', '.')
        capture_mode = 3
        continue
    elif capture_mode == 3:
        # Citation number, ignore and reset
        capture_mode = 0
        continue

if current_service:
    services.append(current_service)

# Create a json
os.makedirs('src/lib/data', exist_ok=True)
with open('src/lib/data/services.json', 'w', encoding='utf-8') as f:
    json.dump(services, f, indent=2)

print(f"Extracted {len(services)} services.")
