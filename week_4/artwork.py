import csv

with open('Artworks.csv', 'r') as artwork_file:

    csv_reader = csv.DictReader(artwork_file)
    csv_writer = {}

    for row in csv_reader:
        nationality = row['Nationality']
        if nationality not in csv_writer:
            NewCsv = f"res{nationality}.csv"
            csv_writer[nationality] = open(NewCsv, 'w')
            output = csv.writer(csv_writer[nationality])
            output.writerow(['Title','Artist','Nationality'])

            output.writerow(row.values())

            for file in csv_writer.values():
                file.close()
   
