# CHANGELOG
All notable changes to this project are documented here.

## [2026-07-23] Fix website extraction fallback
Files changed:
- main.py
Reason:
Fixed an issue where the website fallback logic would naively grab the first external link on the page, resulting in tracking domains like 'bing.com' being extracted. Added specific tracking exclusions and enhanced element search for the website URL.

## [2026-07-23] Refactor scraper to use requests and BeautifulSoup
Files changed:
- requirements.txt
- nixpacks.toml (Deleted)
- railway.json (Deleted)
- Dockerfile (New)
- main.py
- test_scraper.py
Reason:
The camoufox headless browser caused heavy OS dependency issues and crashes on Railway. Replaced it with a lightweight HTTP requests-based scraper. Replaced legacy Nixpacks configuration with a standard Dockerfile for Railway deployment.
Related tests:
test_scraper.py