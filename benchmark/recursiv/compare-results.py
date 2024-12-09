def main():
    log_enumeration = "./enumeration/hmm.enumeration.log"
    log_mappl = "./mappl/hmm.mappl.log"
    log_perpl = "./perpl/hmm.perpl.log"

    values_enumeration = []
    values_mappl = []
    values_perpl = []

    with open(log_enumeration, 'r') as logFile:
        for line in logFile:
            values_enumeration.append(float(line.strip()))

    with open(log_mappl, 'r') as logFile:
        for line in logFile:
            values_mappl.append(float(line.strip()))

    with open(log_perpl, 'r') as logFile:
        for line in logFile:
            values_perpl.append(float(line.strip()[1 : -1]))

    for index in range(max(len(values_enumeration), len(values_mappl), len(values_perpl))):
        if index < len(values_enumeration) and index < len(values_mappl):
            print("diff enumeration-mappl", abs(values_enumeration[index] - values_mappl[index]))

        if index < len(values_enumeration) and index < len(values_perpl):
            print("diff enumeration-perpl", abs(values_enumeration[index] - values_perpl[index]))

        if index < len(values_mappl) and index < len(values_perpl):
            print("diff mappl-perpl", abs(values_mappl[index] - values_perpl[index]))

if __name__ == "__main__":
    main()