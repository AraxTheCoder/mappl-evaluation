#!/bin/bash

hyperfine_runs=1 

range="${1:-32}" # default: 64

here=$(dirname "$0")

compiler="mappl"
executer="python"

file_name="performance-mappl"
file="tmp.py"

{
hyperfine --export-csv  "$here/${file_name}.csv"  \
          --runs "$hyperfine_runs" \
          --parameter-scan length 1 "$range" \
          --setup "$compiler pyro ./programs/hmm.mappl | cat header.py - footer.py > ${file}" \
          --cleanup "rm ${file}" \
          --style none --output inherit \
          --ignore-failure \
        "$executer ${file} --horizon {length}" 
        # --export-json "$here/${file_name}.json" \
 } 2>&1 | tee "$here/hmm.mappl.log"
