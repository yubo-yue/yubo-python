import pickle

def main():
    outfile = open("numbers.dat", "wb")

    data = eval(input("Enter an integer"))
    while data != 0:
        pickle.dump(data, outfile)
        data = eval(input("Enter an integer"))
    outfile.close()

    infile = open("numbers.dat", "rb")

    end_of_file = False
    while not end_of_file:
        try:
            print(pickle.load(infile), end = " ")
        except EOFError:
            end_of_file = True
    infile.close()

    print("\nAll objects are read")

main()
