# Segregation Tracking Project

Comprehensive tracking of segregation across U.S. neighborhoods and schools — a collaboration between USC and Stanford.

## Overview

The [Segregation Tracking Project](https://edopportunity.org/segregation/) provides data on racial, ethnic, and economic segregation across every U.S. neighborhood and school. Maintained by Sean Reardon (Stanford) and Ann Owens (UCLA).

This dataset includes the publicly available **exposure-segregation** data from the companion research paper ([Nilforoshan et al., Nature 2023](https://www.nature.com/articles/s41586-023-06757-3)), which measures socioeconomic segregation through anonymized mobility patterns.

## Data

| File | Description | Rows |
|------|-------------|------|
| `data/exposure-segregation-county.csv` | Exposure segregation by county | 2,828 |
| `data/exposure-segregation-msa.csv` | Exposure segregation by metro area | 382 |

### County-level data

| Field | Description |
|-------|-------------|
| `exposure_segregation` | Raw exposure segregation index |
| `fips_code` | County FIPS code |
| `county_name` | County name |
| `exposure_segregation_smoothed` | Smoothed index (0–1 scale) |

### MSA-level data

| Field | Description |
|-------|-------------|
| `exposure_segregation` | Exposure segregation index |
| `msa` | Metropolitan Statistical Area name |
| `bridging_index` | Cross-group connectivity index (0–1) |

## Key Finding

Socioeconomic exposure segregation is **67% higher in the ten largest metropolitan areas** than in small MSAs with fewer than 100,000 residents — contradicting the assumption that large, diverse cities promote economic mixing.

## Methodology

- Based on 1.6 billion person-to-person encounters among 9.6 million individuals
- Data source: Anonymized cell phone location records (SafeGraph, 2017, 3-month window)
- Socioeconomic status inferred from nighttime home location and local rental prices
- **Exposure Segregation**: measures how much lower-income and higher-income residents encounter each other in daily movements
- **Bridging Index**: normalized measure (0–1) of cross-income encounters relative to a random baseline

## Full Dataset Access

The complete Segregation Tracking Project dataset — covering racial/ethnic and economic segregation across neighborhoods and schools from 1970 to the present — is available at:

**https://edopportunity.org/segregation/data/**

Registration (email + data use agreement) required. Free for research use; commercial use prohibited.

## Source Paper

Nilforoshan, H., Looi, W., Pierson, E., Villanueva, B., Fishman, N., Chen, Y., Sholar, J., Redbird, B., Grusky, D., & Leskovec, J. (2023). **Human mobility networks reveal increased segregation in large cities.** *Nature*, 623, 71–77. https://doi.org/10.1038/s41586-023-06757-3

## Project Credits

**Segregation Tracking Project**: Sean Reardon (Stanford), Ann Owens (UCLA), Demetra Kalogrides (Stanford). Funded by Russell Sage Foundation, Robert Wood Johnson Foundation, and Bill & Melinda Gates Foundation.

**Exposure-Segregation Research**: Hamed Nilforoshan, Wenli Looi, Emma Pierson, Blanca Villanueva, Nic Fishman, Yiling Chen, John Sholar, Beth Redbird, David Grusky, Jure Leskovec — Stanford SNAP Lab.
