import json
with open(r'd:\codingLerning\NLP\NLP_LAB_1\NLP_LAB_1\Introduction to Natural Language Processing (NLP).ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)
for i, cell in enumerate(nb['cells']):
    print(f"--- Cell {i} ({cell['cell_type']}) ---")
    source = cell.get('source', [])
    if isinstance(source, list):
        print("".join(source))
    else:
        print(source)
    print()
