import requests
from bs4 import BeautifulSoup
from rich.console import Console
from rich.table import Table
from rich.progress import Progress
from urllib.parse import urlparse
import json

console = Console()

def fetch_html(url):
    try:
        # Validate URL
        parsed = urlparse(url)
        if not parsed.scheme:
            url = "http://" + url  # add default scheme
        headers = {"User-Agent": "Mozilla/5.0"}
        with Progress() as progress:
            task = progress.add_task(f"[cyan]Fetching {url} ...", total=1)
            response = requests.get(url, headers=headers, timeout=10)
            progress.update(task, advance=1)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        console.print(f"[red]Error fetching URL:[/red] {e}")
        return None

def parse_metadata(html):
    soup = BeautifulSoup(html, "html.parser")
    metadata = {}

    # Standard HTML metadata
    metadata['title'] = soup.title.string.strip() if soup.title else 'N/A'
    desc = soup.find("meta", attrs={"name": "description"})
    metadata['description'] = desc["content"].strip() if desc and "content" in desc.attrs else 'N/A'
    keywords = soup.find("meta", attrs={"name": "keywords"})
    metadata['keywords'] = keywords["content"].strip() if keywords and "content" in keywords.attrs else 'N/A'

    # Open Graph
    og_title = soup.find("meta", attrs={"property": "og:title"})
    metadata['og:title'] = og_title["content"].strip() if og_title and "content" in og_title.attrs else 'N/A'
    og_desc = soup.find("meta", attrs={"property": "og:description"})
    metadata['og:description'] = og_desc["content"].strip() if og_desc and "content" in og_desc.attrs else 'N/A'
    og_image = soup.find("meta", attrs={"property": "og:image"})
    metadata['og:image'] = og_image["content"].strip() if og_image and "content" in og_image.attrs else 'N/A'

    # Twitter Cards
    tw_title = soup.find("meta", attrs={"name": "twitter:title"})
    metadata['twitter:title'] = tw_title["content"].strip() if tw_title and "content" in tw_title.attrs else 'N/A'
    tw_desc = soup.find("meta", attrs={"name": "twitter:description"})
    metadata['twitter:description'] = tw_desc["content"].strip() if tw_desc and "content" in tw_desc.attrs else 'N/A'
    tw_image = soup.find("meta", attrs={"name": "twitter:image"})
    metadata['twitter:image'] = tw_image["content"].strip() if tw_image and "content" in tw_image.attrs else 'N/A'

    return metadata

def display_metadata(metadata):
    table = Table(title="URL Metadata Extractor", show_lines=True)
    table.add_column("Property", style="bold cyan")
    table.add_column("Value", style="white")
    for key, value in metadata.items():
        table.add_row(key, value)
    console.print(table)

def save_to_json(metadata, filename="metadata.json"):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(metadata, f, ensure_ascii=False, indent=4)
        console.print(f"[green]Metadata saved to {filename}[/green]")
    except Exception as e:
        console.print(f"[red]Failed to save JSON:[/red] {e}")

def main():
    console.print("[bold green]Elite URL Metadata Extractor[/bold green]\n")
    while True:
        url = console.input("Enter URL (or type 'exit' to quit): ").strip()
        if url.lower() == "exit":
            break
        html = fetch_html(url)
        if html:
            metadata = parse_metadata(html)
            display_metadata(metadata)

            save_option = console.input("Save metadata to JSON? (y/n): ").strip().lower()
            if save_option == "y":
                save_to_json(metadata)

        console.print("\n")

if __name__ == "__main__":
    main()
