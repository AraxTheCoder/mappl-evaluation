import torch
import pyro.distributions as dist
import argparse
import pyro
import pyro.contrib as contrib

max_tries=2**256

def float_tensor(d):
    return torch.tensor(d, dtype=torch.float)

def emit(z):
    if z:
        return 60
    
    return 120

def step(z):
    if z:
        return 0.8
    
    return 0.1

def model(cur, data):
        b = None
        if len(data) == 0:
            b = ()
        else:
            x = data[0]
            xs = data[1:]
            pyro.factor(f"obsve_{len(data)}", dist.Normal(emit(cur), 1).log_prob(float_tensor(x)))
            nxt = pyro.sample(f"state_{len(data)}", dist.Bernoulli(step(cur))).long()
            model(nxt.item(), xs)
            b = ()
        return ()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--horizon", type=int, required=True)
    args = parser.parse_args()

    data = (60, ) * args.horizon

    enum = contrib.oed.search.Search(model, max_tries=max_tries)
    enum.run(1, data)
    log_prob = torch.logsumexp(torch.tensor(enum.log_weights), dim=-1)

    print(torch.exp(log_prob).item())

if __name__ == '__main__':
    main()