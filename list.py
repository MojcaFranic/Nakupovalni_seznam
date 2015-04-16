nakupovalni_seznam = []

print("Naredi nakupovalni seznam: ")

prvi_artikel = raw_input("Kaj zelis kupiti? ")

nakupovalni_seznam.append(prvi_artikel)

odgovor = "da"

while odgovor == "da":
    odgovor = raw_input("Ali zelis kaj dodati? da/ne ")

    if odgovor == "ne":
        print("Tvoj seznam: ")

        for artikel in nakupovalni_seznam:
            print("- ") +  artikel
        break
    elif odgovor == "da":



        dodatek = raw_input("Povej kaj zelis dodati? ")

    nakupovalni_seznam.append(dodatek)
