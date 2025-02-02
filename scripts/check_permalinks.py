"""Open permalinks generated by `hugo list all > my_file.csv`"""

import csv
import logging
import urllib.error
import urllib.parse
import urllib.request
from multiprocessing import Pool
from pathlib import Path
from typing import Any, Dict

import fire
import frontmatter

CONTENT_DIR = Path(__file__).parents[1] / "content"


def main(path: Path, localhost: bool = False, port: int = 1313):
    # load csv
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        contents = list(reader)
    logging.info(f"Found {len(contents)} content files")

    # modify URLs if needed
    if localhost:
        logging.info("Converting links to localhost")
        contents = [convert_url_to_localhost(content=c, port=port) for c in contents]

    # check URLs
    logging.info("Checking URLs and adding aliases...")
    with Pool() as pool:
        pool.map(check_urls, contents)
    logging.info("Checking complete")


def add_aliases(content: Dict[str, Any]):
    dir_name = str(Path(content["path"]).parts[-2])
    dir_path = next(CONTENT_DIR.rglob(dir_name))
    md_path = dir_path / "index.md"

    with open(md_path) as f:
        post = frontmatter.load(f)

    if "aliases" not in post.metadata:
        post.metadata["aliases"] = []

    alias_path = urllib.parse.urlparse(content["permalink"]).path
    post.metadata["aliases"].append(alias_path)

    with open(md_path, "w") as f:
        f.write(frontmatter.dumps(post))


def convert_url_to_localhost(content: Dict[str, Any], port: int):
    netloc = f"localhost:{port}"
    url = content["permalink"]
    url = urllib.parse.urlparse(url)._replace(netloc=netloc, scheme="http").geturl()
    content["permalink"] = url
    return content


def check_urls(content: Dict[str, Any]):
    """Return the content object if the URL fails to connect"""
    try:
        urllib.request.urlopen(content["permalink"])
    except urllib.error.HTTPError:
        logging.error(f"Bad URL: {content}")
        add_aliases(content)
    except urllib.error.URLError:
        logging.error("Host not available")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    fire.Fire(main)
