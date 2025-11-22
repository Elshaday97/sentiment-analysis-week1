# Scripts

This folder contains **standalone utility scripts** used during early development and exploratory phases.

They are intentionally lightweight and focused on specific text-processing tasks.  
All reusable logic is being progressively migrated into the `src/` package for better testing, reuse, and maintainability.

## Current Scripts

### `text_cleaning.py`

**Purpose:** Preprocess financial news headlines by removing noise and boilerplate common in analyst articles.

- clean_text(): Removes URLs, numbers, stop words + financial noise
- extract_domain(): Handles email-style publishers
