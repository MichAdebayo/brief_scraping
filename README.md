# Castorama Web Scraping Project

![Image](https://github.com/user-attachments/assets/20140b4a-4c59-487e-9e5a-92ca9f9a7d16)

## Overview

This repository contains a web scraping solution designed to help BricoSimplon, an e-commerce platform specializing in DIY and home improvement, monitor competitors' pricing strategies. By collecting and analyzing real-time product and category data from competitor websites (in this case, Castorama), this project supports BricoSimplon in optimizing its pricing policies and maintaining competitiveness in the market.

The scraping system was developed using Scrapy, focusing on clean and efficient data extraction, processing, and export. It ensures compliance with ethical scraping practices, avoiding server overload and respecting website policies.

## Features

### Implemented Functionalities

1. **Category Scraping:**

- Extracts all categories and subcategories from target websites.
- Differentiates between categories leading to subcategories and those linking directly to product lists.


2. **Product Scraping:**

- Collect product data (name, price, URL, availability, etc.) from category-specific pages.
- Handle pagination to scrape all products listed.

3. **Data Processing Pipeline:**

- Cleans and validates scraped data to ensure quality.
- Removes duplicates using unique identifiers for categories and products.

4. **Data Export:**

- **Categories** exported to categories.csv.
- **Products** exported to products.csv.

5. **Error Handling:**

- Includes error-catching mechanisms to manage missing or inconsistent data.
- Logs errors for debugging.


## Bonus Feature

**Database Integration:**
- Stores data in an SQLite relational database.
- Maintains tables for categories and products, linked by foreign keys.


## Getting Started

### Prerequisites

- Python 3.8 or higher
- Scrapy
- SQLite (optional, for database functionality)
- ipython (to enhance the interactive debugging and development process)

Install dependencies with:

```
pip install -r requirements.txt
````

## Running the Scrapers

1. **Categories Spider:** Extracts all categories and subcategories.
```
scrapy crawl castospider
```
2. **Product List Spider:** Scrapes product data from category-specific pages.

```
scrapy crawl productspider
````

## Data Outputs

### Category Data:

- Exported to `categories.csv`.
- Contains fields: `category`, `url`, `is_page_list` (which indicate whether a category is the final product page list).

### Product Data:

- Exported to `products.csv`.
- Contains fields: `unique_id`, `category`, `subcategory`, `subsubcategory`,`subsubsubcategory`, `title`, `price`, and `url`.

## Design Considerations

1. **Compliance:**

- Implements `DOWNLOAD_DELAY` and `USER_AGENT` to avoid overloading servers.
- Respects the `robots.txt` of the target websites.

2. **Deduplication:**

- Uses unique identifiers to ensure no duplicate categories or products.
- Handles cases where a product belongs to multiple categories.

3. **Modularity:**

Code is modular, making it easy to extend and maintain.


## Future Enhancements

- Add support for additional competitors.
- Implement a more advanced scheduler for real-time data scraping.
- Integrate machine learning to detect pricing trends and insights.

## Contributors

This project was collaboratively developed and managed by **Michael Adebayo** ([@MichAdebayo](https://github.com/MichAdebayo))  and **David Scott**([@Daviddavid-sudo](https://github.com/Daviddavid-sudo)).
