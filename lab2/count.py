# Python Script to count countries in Avro
# Assuming it is safest to run this with "python count.py"

import pandas as pd
import avro.schema
from avro.datafile import DataFileReader
from avro.io import DatumReader

countries = []

reader = DataFileReader(open("countries.avro", "r"), DatumReader())
for country in reader:
    countries.append(country)
reader.close()

countries = pd.DataFrame.from_dict(countries)
count_pop = countries['population']
print 'Count of countries with over 10000000:',count_pop[count_pop > 10000000].size

