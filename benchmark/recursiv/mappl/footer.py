def head(data):
    return data[0]

def tail(data):
    return data[1:]

def halt_transformed(_b):
    return 0.0

def emit(z):
    if z:
        return 60
    
    return 120

def step(z):
    if z:
        return 0.8
    
    return 0.1

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--horizon", type=int, required=True)

    args = parser.parse_args()

    data = (60, ) * args.horizon

    log_prob = hmm(halt_transformed, 1, data)

    print(torch.exp(log_prob).item())

if __name__ == '__main__':
    main()