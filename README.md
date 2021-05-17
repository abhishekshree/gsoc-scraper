# gsoc-scraper
For scraping the results.

### Usage:
- This scrapper uses, the ```requests``` library.
- There was an API endpoint which I found through the Developer console. This endpoint will always fetch the current projects so can be reused.

To run this locally, the steps are:
- Run the command ```pip install -r requirements.txt```
- Run ```python scraper.py```
- This will create a ```gsoc2021.csv``` file with the desired columns.

---
[Link to the endpoint](https://summerofcode.withgoogle.com/api/program/current/project/?page=1&page_size=20)

This took some time so let it run for about 5 minutes peacefully please.