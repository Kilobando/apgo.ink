import os
import pytest
from bs4 import BeautifulSoup
from urllib.parse import urlparse

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Collect all html files in repository
html_files = []
for root, _, files in os.walk(REPO_ROOT):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

@pytest.mark.parametrize('html_path', html_files)
def test_internal_links_exist(html_path):
    with open(html_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
    for a in soup.find_all('a', href=True):
        href = a['href']
        if href.startswith('https://apgo.ink/'):
            path = urlparse(href).path.lstrip('/')
            if not path:
                target_file = os.path.join(REPO_ROOT, 'index.html')
            else:
                # Skip dictionary cross references and journal articles not present
                if path.startswith('dictionary/') or path.startswith('journal/'):
                    continue
                target_dir = os.path.join(REPO_ROOT, path)
                target_file = os.path.join(target_dir, 'index.html')
                if not os.path.exists(target_dir) and os.path.exists(target_dir + '.html'):
                    target_file = target_dir + '.html'
            assert os.path.exists(target_file), f"Broken link: {href} referenced from {html_path}"

