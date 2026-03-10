# 🌐 URL Metadata Extractor

An **elite and comprehensive URL Metadata Extractor** for developers, researchers, and digital marketers. Input any URL and instantly retrieve essential metadata like title, description, keywords, Open Graph, and Twitter card details.

---

## Features

- Fetch metadata from **any website**.
- Extract **title**, **description**, **keywords**.
- Capture **Open Graph** & **Twitter Card** metadata if available.
- Display results in a **rich terminal table**.
- Optionally save output to a **JSON file**.
- Handles errors gracefully: invalid URLs, network issues, or missing metadata.
- Shows **progress while fetching** metadata for better UX.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/MrV3nomous/url-metadata-extractor.git
cd url-metadata-extractor
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

#### Dependencies:
- requests
- beautifulsoup4
- rich


---


### Usage

Run the program:

```bash
python metadata_extractor.py
```


### Optional JSON export:
In program prompt
Save metadata to JSON? (y/n): y


### Error Handling

Invalid URL → program requests a valid URL.

Network or connection issues → displays a friendly error message.

Missing metadata fields → shows N/A instead of crashing.


---


## Contributing

Contributions are welcome!

You can:
- Add support for more metadata fields.
- Improve parsing for edge-case websites.
- Enhance terminal UI with more styling.


---

## License
MIT License © 2026 Soumik Halder


