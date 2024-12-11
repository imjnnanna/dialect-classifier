import csv
import re

movies = "movies_text.txt"
tv = "tv_text.txt"
movies_sources = "movies_sources.txt"
tv_sources = "tv_sources.txt"

output_csv = "media.csv"

def load_metadata(file_path):
    metadata = {}
    with open(file_path, 'r', encoding='windows-1252') as f:
        reader = csv.DictReader(f, delimiter='\t')
        for row in reader:
            fileID = row['fileID']
            country = row['country']
            language = row['language(s)']
            if 'English' in language and ',' not in language:
                metadata[fileID] = country
    return metadata

def map_country_to_acronym(country):
    country_map = {
        "Australia": "AU",
        "Bangladesh": "BD",
        "Canada": "CA",
        "Great Britain": "GB",
        "Ghana": "GH",
        "Hong Kong": "HK",
        "Ireland": "IE",
        "India": "IN",
        "Jamaica": "JM",
        "Kenya": "KE",
        "Sri Lanka": "LK",
        "Malaysia": "MY",
        "Nigeria": "NG",
        "New Zealand": "NZ",
        "Philippines": "PH",
        "Pakistan": "PK",
        "Singapore": "SG",
        "Tanzania": "TZ",
        "United States": "US",
        "South Africa": "ZA",
        "USA": "US",
        "UK": "GB",
    }
    if country in country_map:
        return country_map[country]
    if ',' in country:
        return [map_country_to_acronym(c.strip()) for c in country.split(',')]
    return None

def process_text(text, metadata, output_csv, written_ids):
    with open(text, 'r', encoding='utf-8') as infile, open(output_csv, 'a', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        if outfile.tell() == 0:
            writer.writerow(["fileID", "text", "country"])

        for line in infile:
            match = re.match(r"@@(\d+)\s+(.*)", line)
            if match:
                fileID = match.group(1)
                text = match.group(2)
                if fileID in metadata and fileID not in written_ids:
                    country = map_country_to_acronym(metadata[fileID])
                    if country:
                        writer.writerow([fileID, text, country])
                        written_ids.add(fileID)

# movies
metadata = load_metadata(movies_sources)
written_ids = set()
process_text(movies, metadata, output_csv, written_ids)

# tvs
metadata = load_metadata(tv_sources)
process_text(tv, metadata, output_csv, written_ids)

print(f"Filtered texts saved to {output_csv}")