import torch
import pyro.distributions as dist

program = rf"""
data String = Nil | Cons Bool String;
define observe: Bool -> Bool -> () = \cur. \obs.
    if cur then
        if obs then
            factor {torch.exp(dist.Normal(60, 1).log_prob(torch.tensor(60, dtype=torch.float))).item():.30f} in
            ()
        else
            factor {torch.exp(dist.Normal(60, 1).log_prob(torch.tensor(120, dtype=torch.float))).item():.30f} in
            ()
    else
        if obs then
            factor {torch.exp(dist.Normal(120, 1).log_prob(torch.tensor(60, dtype=torch.float))).item():.30f} in
            ()
        else
            factor {torch.exp(dist.Normal(120, 1).log_prob(torch.tensor(120, dtype=torch.float))).item():.30f} in
            ()
;

define transite: Bool -> Bool = \cur.
    if cur then
        amb (factor 0.8 in True) (factor 0.2 in False)
    else
        amb (factor 0.1 in True) (factor 0.9 in False)
;

define hmma: Bool -> String -> () = \cur. \obs.
    case obs of 
    | Nil -> ()
    | Cons x xs -> 
        let _ = (observe cur x) in
        let nxt = (transite cur) in
        hmma nxt xs
;
"""

def build():
    global program

    for observationLength in range(1, 65):
        print(f"[Create] Perpl program with observation sequence of {observationLength}")
        with open(f'programs\\hmm.{observationLength}.perpl', 'w') as file:
            file.write(program)
            file.write("define obs =" + "(Cons True" * observationLength + " Nil" + ")" * observationLength + ";\n")
            file.write("hmma True obs")

if __name__ == '__main__':
    build()