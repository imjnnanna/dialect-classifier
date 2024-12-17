from readtxt import load_metadata, process_text

movies = "movies_text.txt"
tv = "tv_text.txt"
movies_sources = "movies_sources.txt"
tv_sources = "tv_sources.txt"

now = "now_text.txt"
now_sources = "now_sources.txt"

covid = "covid_text.txt"
covid_sources = "covid_sources.txt"

# output_csv = "media.csv"
# output_csv = "now.csv"
output_csv = "covid.csv"

metadata = load_metadata(covid_sources)
written_ids = set()
process_text(covid, metadata, output_csv, written_ids)

# NOW
# metadata = load_metadata(now_sources)
# written_ids = set()
# process_text(now, metadata, output_csv, written_ids)

# movies
# metadata = load_metadata(movies_sources)
# written_ids = set()
# process_text(movies, metadata, output_csv, written_ids)

# tvs
# metadata = load_metadata(tv_sources)
# process_text(tv, metadata, output_csv, written_ids)

print(f"Filtered texts saved to {output_csv}")