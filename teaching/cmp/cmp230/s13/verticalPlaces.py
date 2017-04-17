#Strings hw: Printing lists vertically


def main():
    places = ["San Francisco",
              "Christchurch ",
              "Sydney       ",
              "Bangkok      ",
              "Copenhagen   "]

    print(places)
    l = len(places[0])
    for i in range(l):
        for j in range(len(places)):
            print(places[j][i], end="  ")
        print()

main()
