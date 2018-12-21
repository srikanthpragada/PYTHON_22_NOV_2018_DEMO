import requests

resp = requests.get("https://restcountries.eu/rest/v2/all")
countries = resp.json()
file = open("countries.txt","wt")
for country in countries:
    brds = country['borders']
    # print(brds)
    if len(brds) > 0:
        borders = ":".join(brds)
    else:
        borders = "None"

    st  = "%s,%s,%s,%s,%s\n" % (country['alpha3Code'],country['name'],
                            country['capital'], country['population'],
                            borders)
    try:
        file.write(st)
    except Exception as ex:
        print(country['name'], ex)

file.close()



