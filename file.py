nakupovalni_seznam = []

print("Naredi nakupovalni seznam: ")

prvi_artikel = raw_input("Kaj zelis kupiti? ")

odgovor = "da"

while odgovor == "da":
    odgovor = raw_input("Ali zelis kaj dodati? da/ne ")

    if odgovor == "ne":
        print("Tvoj seznam: ")
        print("- " + prvi_artikel)
        for artikel in nakupovalni_seznam:
            print("- ") +  artikel
        break
    elif odgovor == "da":



        dodatek = raw_input("Povej kaj zelis dodati? ")

    nakupovalni_seznam.append(dodatek)




