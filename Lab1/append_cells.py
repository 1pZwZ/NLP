import json
file_path = r'd:\codingLerning\NLP\NLP_LAB_1\NLP_LAB_1\Introduction to Natural Language Processing (NLP).ipynb'
with open(file_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)
new_cells = [
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## Lab Tasks\n",
            "### Task 1 & 2: Download and open a dataset"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "import urllib.request\n",
            "import pandas as pd\n",
            "\n",
            "# Download a sample CSV dataset\n",
            "url = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv'\n",
            "dataset_path = 'airline-safety.csv'\n",
            "urllib.request.urlretrieve(url, dataset_path)\n",
            "print('Dataset downloaded successfully!')"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "# Open and display the dataset\n",
            "df = pd.read_csv(dataset_path)\n",
            "df.head()"
        ]
    }
]
nb['cells'].extend(new_cells)
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)
print("Notebook updated successfully.")
