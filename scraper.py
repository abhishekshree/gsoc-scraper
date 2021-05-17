import csv
import requests

out = "gsoc2021.csv"
url = "https://summerofcode.withgoogle.com/api/program/current/project/?page=1&page_size=20"
fields = ['Name', 'Organization', 'Project']

page = requests.get(url)
total_pages = int((page.json())['count'] / 20) + 1

print("Starting to write in the " + out + " file...")

with open(out, 'w', newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=fields)
    writer.writeheader()

    # We fetch each page from the API, with 20 elements. There are a total of 1291 projects so, 65 pages!
    for j in range(1, total_pages + 1):
        url = "https://summerofcode.withgoogle.com/api/program/current/project/?page={}&page_size=20".format(j)
        page = requests.get(url)
        d = page.json()
        li = d['results']  # list containing the selected projects

        for x in li:
            # Fetched the fields from each object
            proj = x['title']
            org = x['organization']['name']
            name = x['student']['display_name']

            # this dictionary will be written in the csv
            write_dict = {
                'Name': name,
                'Organization': org,
                'Project': proj
            }
            writer.writerow(write_dict)

print("Written!")
