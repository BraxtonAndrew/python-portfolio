# Oil Price Analyzer

Reads tick-level oil price data and prints the low, high, and range for each day.

Input format (one trade per line): `YYYYMMDD HHMMSS;price;volume`

```bash
python oil_data.py oildata_sample.txt
```

Example output:

```
Date             Low    High   Range
2017-02-12     54.26   54.42    0.16
2017-02-13     54.26   54.35    0.09
```

- `oildata_sample.txt` is a 750-line excerpt so the script runs out of the box.
- The full dataset (about 134 MB, 5.4M lines) is too large for GitHub. Pass its path as the argument to run on it; it takes about 3 seconds.
- The file is read line by line, so memory use stays small regardless of file size.
