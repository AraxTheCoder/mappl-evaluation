def main():
    performance_enumeration = "./enumeration/performance-enumeration.csv"
    performance_mappl = "./mappl/performance-mappl.csv"
    performance_perpl = "./perpl/performance-perpl.csv"
 
    for performance_file in [performance_enumeration, performance_mappl, performance_perpl]:
        with open(performance_file, 'r') as file:
            print(performance_file)
            for line in file.readlines()[1:]:
                values = line.strip().split(",")
                mean_timing = values[3]
                observation_length = values[-1]
                print(observation_length, mean_timing)

if __name__ == "__main__":
    main()