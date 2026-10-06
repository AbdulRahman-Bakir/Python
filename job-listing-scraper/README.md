# Job Listing Scraper

A Python web scraper that extracts job listings from the [Real Python Fake Jobs](https://realpython.github.io/fake-jobs/) website and stores the results in a CSV file.

## Features

* Fetches the job listing page using `requests`
* Parses HTML using Beautiful Soup
* Extracts:

  * Job title
  * Company name
  * Location
  * Job detail URL
* Handles missing HTML fields gracefully
* Handles HTTP and network errors
* Exports the scraped data to `jobs.csv`

## Technologies

* Python
* Requests
* Beautiful Soup
* CSV

## Project Structure

```text
job-listing-scraper/
├── src/
│   └── job_listing_scraper/
│       ├── __init__.py
│       └── main.py
├── pyproject.toml
├── uv.lock
└── README.md
```

## Installation

Install the project dependencies with [uv](https://docs.astral.sh/uv/):

```bash
uv sync
```

## Usage

Run the scraper with:

```bash
uv run job-listing-scraper
```

The scraper creates a `jobs.csv` file containing the extracted job listings.

## Example CSV

```csv
title,company,location,detail_url
Senior Python Developer,Payne Roberts and Davis,Stewartbury AA,https://realpython.github.io/fake-jobs/jobs/senior-python-developer-0.html
```

## Purpose

This project was built to practice web scraping with Python, particularly working with HTTP responses, HTML parsing, Beautiful Soup, and structured data extraction.
