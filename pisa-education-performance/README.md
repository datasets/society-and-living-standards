# PISA Education Performance

OECD PISA (Programme for International Student Assessment) mean performance scores for 15-year-olds in **mathematics**, **reading**, and **science** — 85 countries and economies across 7 cycles from 2000 to 2018.

PISA is one of the few cross-country standardised assessments of student skills. It has been conducted every three years since 2000 and remains the primary source for international comparisons of education outcomes.

## Data

### `pisa-scores.csv`

Mean PISA scores in long format: one row per country × subject × year.

| Field | Description |
|---|---|
| `country_name` | Country or economy name |
| `country_code` | ISO 3166-1 alpha-3 code |
| `year` | PISA cycle year (2000, 2003, 2006, 2009, 2012, 2015, 2018) |
| `subject` | `mathematics`, `reading`, or `science` |
| `mean_score` | Mean PISA score (OECD mean ≈ 500, SD ≈ 100) |

**Coverage:** 85 countries/economies, 7 cycles, 3 subjects = 1,261 observations.

**Note:** PISA 2022 data (published December 2023) is not yet available in the World Bank EdStats source used here.

## Sources

- **OECD PISA** — [oecd.org/pisa](https://www.oecd.org/pisa/data/) — the authoritative source
- **World Bank EdStats** — [datatopics.worldbank.org/education](https://datatopics.worldbank.org/education/) — indicators `LO.PISA.MAT`, `LO.PISA.REA`, `LO.PISA.SCI` (mirrors OECD PISA data, CC-BY 4.0)

## Processing

Run `python3 process.py` to regenerate `data/pisa-scores.csv` by downloading the latest data from the World Bank EdStats API.
