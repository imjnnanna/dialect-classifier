import csv
import re

def load_metadata(file_path):
    metadata = {}
    with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
        reader = csv.DictReader(f, delimiter='\t')
        for row in reader:
            if 'fileID' in row:
                fileID = row['fileID']
            else:
                fileID = row['textID']
            country = row['country']
            if 'language' in row:
                language = row['language(s)']
                if 'English' in language and ',' not in language:
                    metadata[fileID] = country
            else:
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

        "AU": "AU",
        "BD": "BD",
        "CA": "CA",
        "GB": "GB",
        "GH": "GH",
        "HK": "HK",
        "IE": "IE",
        "IN": "IN",
        "JM": "JM",
        "KE": "KE",
        "LK": "LK",
        "MY": "MY",
        "NG": "NG",
        "NZ": "NZ",
        "PH": "PH",
        "PK": "PK",
        "SG": "SG",
        "TZ": "TZ",
        "US": "US",
        "ZA": "ZA",

        "USA": "US",
        "UK": "GB",
    }
    if country in country_map:
        return country_map[country]
    if ',' in country:
        return [map_country_to_acronym(c.strip()) for c in country.split(',')]
    print(country)
    return None

def process_text(text, metadata, output_csv, written_ids):
    with open(text, 'r', encoding='utf-8', errors='replace') as infile, open(output_csv, 'a', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        if outfile.tell() == 0:
            writer.writerow(["fileID", "text", "country"])

        for line in infile:
            match = re.match(r"@@(\d+)(.*)", line)
            if match:
                fileID = match.group(1)
                text = match.group(2).strip()
                if fileID in metadata:
                    country = map_country_to_acronym(metadata[fileID])
                    writer.writerow([fileID, text, country])
