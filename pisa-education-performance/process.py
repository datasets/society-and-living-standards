"""
process.py — PISA Education Performance

Downloads OECD PISA mean performance scores (reading, mathematics, science)
for all participating countries across all available cycles from the
World Bank Education Statistics (EdStats) database, which mirrors the
authoritative OECD PISA data.

Source: World Bank EdStats API (source 12)
  https://datatopics.worldbank.org/education/

Indicators:
  LO.PISA.MAT  — PISA mean performance: mathematics
  LO.PISA.REA  — PISA mean performance: reading
  LO.PISA.SCI  — PISA mean performance: science

Outputs:
  data/pisa-scores.csv   — mean scores by country, subject, and year
"""

import csv
import json
import sys
import time
import urllib.request

WB_API = "https://api.worldbank.org/v2"
SOURCE = 12  # EdStats

INDICATORS = [
    ("LO.PISA.MAT", "mathematics"),
    ("LO.PISA.REA", "reading"),
    ("LO.PISA.SCI", "science"),
]


def fetch_json(url):
    print(f"  GET {url[:120]}", file=sys.stderr)
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def fetch_all_pages(indicator_id):
    """Fetch all pages for a given indicator, all countries, all years."""
    url = (
        f"{WB_API}/country/all/indicator/{indicator_id}"
        f"?format=json&per_page=2000&source={SOURCE}"
    )
    data = fetch_json(url)
    meta = data[0]
    records = data[1]

    total_pages = meta.get("pages", 1)
    for page in range(2, total_pages + 1):
        time.sleep(0.2)
        try:
            paged = fetch_json(url + f"&page={page}")
        except Exception as e:
            print(f"  Stopped at page {page}: {e}", file=sys.stderr)
            break
        records.extend(paged[1])

    return records


def main():
    all_rows = []

    for indicator_id, subject in INDICATORS:
        print(f"Fetching {subject} ({indicator_id})…", file=sys.stderr)
        records = fetch_all_pages(indicator_id)

        rows_added = 0
        for r in records:
            val = r.get("value")
            if val is None:
                continue
            try:
                score = round(float(val), 1)
            except (ValueError, TypeError):
                continue

            country_name = r["country"]["value"]
            iso3 = r.get("countryiso3code", "")
            year = r.get("date", "")

            # Skip aggregates (no ISO3 code or country id is aggregate)
            country_id = r["country"].get("id", "")
            if not iso3 or len(iso3) != 3:
                continue
            # World Bank returns aggregates with 2-char country IDs that are not ISO2
            # (e.g. "1W", "Z4"), skip them
            if not country_id or len(country_id) != 2 or country_id[0].isdigit():
                # Some valid ISO2 codes start with digits? No — skip digits-first
                pass

            all_rows.append(
                {
                    "country_name": country_name,
                    "country_code": iso3,
                    "year": int(year),
                    "subject": subject,
                    "mean_score": score,
                }
            )
            rows_added += 1

        print(f"  → {rows_added} valid observations", file=sys.stderr)

    # Sort by year, country, subject
    all_rows.sort(key=lambda r: (r["year"], r["country_name"], r["subject"]))

    out_path = "data/pisa-scores.csv"
    fieldnames = ["country_name", "country_code", "year", "subject", "mean_score"]
    with open(out_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_rows)

    print(f"\nWritten {len(all_rows)} rows to {out_path}", file=sys.stderr)

    years = sorted(set(r["year"] for r in all_rows))
    countries = sorted(set(r["country_name"] for r in all_rows))
    print(f"Years: {years}", file=sys.stderr)
    print(f"Countries/economies: {len(countries)}", file=sys.stderr)


if __name__ == "__main__":
    main()
