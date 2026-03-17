# A History of Global Living Conditions

Two centuries of progress in human wellbeing — poverty, life expectancy, child mortality, literacy, political freedom, and education — from 1800 to today. Based on Our World in Data's article "A History of Global Living Conditions in 6 Charts".

## Background

The world of 1800 was one of almost universal poverty, short lives, rampant child death, near-total illiteracy, and autocratic rule. Over the past two centuries that picture has been transformed. This dataset tracks six dimensions of that transformation using long-run global estimates compiled by Our World in Data.

## Data

Six CSV files in `data/`:

| File | Description | Coverage |
|------|-------------|----------|
| `life-expectancy.csv` | Global average life expectancy at birth (years) | 1770–2023 |
| `child-mortality.csv` | Share of children dying before age 5, and survival rate (%) | 1800–2023 |
| `literacy.csv` | Share of adults who are literate vs. illiterate (%) | 1820–2023 |
| `democracy.csv` | Population living under democratic vs. autocratic regimes | 1800–2024 |
| `poverty.csv` | World population by income bracket (2011 international dollars per day) | 1820–2018 |
| `education.csv` | Global adult population (15+) by highest education level | 1950–2020 |

### Key columns

**`life-expectancy.csv`**

| Column | Description |
|--------|-------------|
| `year` | Year |
| `life_expectancy_years` | Life expectancy at birth (years) |

**`child-mortality.csv`**

| Column | Description |
|--------|-------------|
| `year` | Year |
| `child_mortality_rate` | Share of children dying before age 5 (%) |
| `child_survival_rate` | Share of children surviving to age 5 (%) |

**`poverty.csv`**

| Column | Description |
|--------|-------------|
| `year` | Year |
| `above_30_usd` | People living on more than 30 USD per day |
| `between_10_30_usd` | People living on 10–30 USD per day |
| `between_5_10_usd` | People living on 5–10 USD per day |
| `between_1_90_5_usd` | People living on 1.90–5 USD per day |
| `below_1_90_usd` | People in extreme poverty (under 1.90 USD per day) |

## Sources

- Our World in Data. [A History of Global Living Conditions in 6 Charts](https://ourworldindata.org/a-history-of-global-living-conditions).

## License

[Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)
