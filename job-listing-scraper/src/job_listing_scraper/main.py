import requests
from bs4 import BeautifulSoup
import csv


def main() -> None:
    url = "https://realpython.github.io/fake-jobs/"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return
    
    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")
    cards = soup.find_all("div", class_="card")
    jobs = []
    for card in cards:
        title = card.find("h2", class_="title")
        if title:
            title = title.get_text(strip=True)
        else:
            title = None
        company = card.find("h3", class_="subtitle")
        if company:
            company = company.get_text(strip=True)
        else:
            company = None
        location = card.find("p", class_="location")
        if location:
            location = location.get_text(strip=True)
        else:
            location = None
        detail_url_element = card.find("a", string="Apply")
        if detail_url_element and detail_url_element.get("href"):
            detail_url = detail_url_element["href"]
        else:
            detail_url = None
        job= {
            "title": title,
            "company": company,
            "location": location,
            "detail_url": detail_url
        }
        jobs.append(job)

    with open("jobs.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["title","company","location","detail_url"])
        writer.writeheader()
        writer.writerows(jobs)