#!/bin/bash

hyperfine_runs=1 

range="${1:-13}" # default: 64

here=$(dirname "$0")

executer="python"

file_name="performance-enumeration"
file="./programs/hmm.py"

{
hyperfine --export-csv  "$here/${file_name}.csv"  \
          --runs "$hyperfine_runs" \
          --parameter-scan length 1 "$range" \
          --style none --output inherit \
          --ignore-failure \
        "$executer ${file} --horizon {length}" 
        # --export-json "$here/${file_name}.json" \
 } 2>&1 | tee "$here/hmm.enumeration.log"
