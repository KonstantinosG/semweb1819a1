import csv

with open('Sch_IRI.csv', newline='') as ifp, open('Sch_RDF.nt', 'w') as ofp:
    reader = csv.reader(ifp)

    for s, p, o in reader:
        editted_s = f'_:b{s[2:]}'
        editted_p = f'<{p}>'
        if o[:2] == 'l:':
            editted_o = o[2:]
            if 'Ώρα' in p:
                editted_o += ':00'
            editted_o = f'"{editted_o}"'
        else:
            editted_o = f'<{o}>'
        ofp.write(' '.join([editted_s, editted_p, editted_o]) + ' .\n')
