import json

with open('src/lib/data/services.json', 'r', encoding='utf-8') as f:
    services = json.load(f)

categories = {}
for s in services:
    cat = s['category']
    categories[cat] = categories.get(cat, 0) + 1

print(f"Total services: {len(services)}")
print("Categories:")
for cat, count in sorted(categories.items()):
    print(f" - {cat}: {count} services")
