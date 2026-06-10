import json

with open('src/lib/data/services.json', 'r', encoding='utf-8') as f:
    services = json.load(f)

subcats = {}
for s in services:
    sub = s.get('architecturalCategory', 'None')
    subcats[sub] = subcats.get(sub, 0) + 1

print(f"Total services: {len(services)}")
print("Architectural Categories:")
for sub, count in sorted(subcats.items()):
    print(f" - {sub}: {count} services")
