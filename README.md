# dialect-classifier
English dialect classifier, for LING 380 final project.
Description of files:
Datasets:
--Jewon can you describe these------(basically just say which file name corresponds to which dataset(s).

Data Cleaning/Manipulation Code:
For each individual dataset(Corpus, media test, covid test, now test), we have a cleaning <insert name(s) of datsets here>.ipynb. To extract the data we used for our tests and training, run these notebooks to get "cleaned_<insert dataset name>.csv", which is what will be used in the training and testing code.

Cleaning Media.ipynb: creates test.csv
Cleaning Now and Covid.ipynb: creates testcovid.csv and testnow.csv
cleaning slayer.ipynb: creates cleaned_slayer.csv

Model Fine-Tuning Code:
For DistilBERT code and TinyBERT code, the files "Ling 380 Project Model-Fine Tuning <insert model name here> here.ipynb can be run with the created csvs noted above.



