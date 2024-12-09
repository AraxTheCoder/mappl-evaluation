#!/bin/bash

hyperfine_runs=1 

perpl_range="${1:-32}" # default: 64

here=$(dirname "$0")

perplc="perplc"
sum_product="sum_product.py"

file_name="performance-perpl"
fgg_file="tmp.fgg"

{
hyperfine --export-csv  "$here/${file_name}.csv"  \
          --runs "$hyperfine_runs" \
          --parameter-scan length 1 "$perpl_range" \
          --setup "$perplc ./programs/hmm.{length}.perpl> ${fgg_file}" \
          --cleanup "rm ${fgg_file}" \
          --style none --output inherit \
          --ignore-failure \
        "$sum_product -d -m fixed-point -l 1e-50 ${fgg_file}" 
        # --export-json "$here/${file_name}.json" \
 } 2>&1 | tee "$here/hmm.perpl.log"
