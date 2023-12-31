# PandasSpeedTests

## Introduction
This repository is designed to test and benchmark Python Pandas acceleration tools, focusing on identifying the most efficient methods for data processing and analysis.

## Key Comparisons
In this project, we are specifically comparing the following technologies:
- **Pandas**: The original Python data analysis library.
- **Modin**: An innovative library that accelerates Pandas using parallel and distributed computing.
- **cuDF**: A RAPIDS AI library that provides a Pandas-like API accelerated by NVIDIA GPUs.
- **Dask**: A flexible parallel computing library for analytic computing.
- **Datatable**: A Python package for manipulating large datasets, inspired by R's data.table.
- **Polars**: A fast DataFrame library implemented in Rust, designed to be used in Python.

Each of these technologies offers unique approaches to accelerate Pandas operations, and our aim is to provide comprehensive benchmarks and insights into their performance.

## Features
- **Benchmarking Reports**: Conducting comprehensive performance tests across different data sizes and operations.
- **Optimization Techniques**: Exploring and documenting best practices for each technology to optimize performance.
- **Comparative Analysis**: Providing detailed comparisons to help users choose the right tool for their specific needs.

## Testing Data
Use the following code to create your test data. --output and --size are optional.  
For example, you want to create a file named large_dataset.csv that takes up 5 GB of memory.
```
python CreateSample.py --output large_dataset.csv --size 5
```

## read_csv
1G            |  5G
:-------------------------:|:-------------------------:
![](https://github.com/wsxqaza12/PandasSpeedTests/blob/master/result_png/read_csv_1G_wins.png)  |  ![](https://github.com/wsxqaza12/PandasSpeedTests/blob/master/result_png/read_csv_5G_wins.png)

## group by | agg 1 columns
1G            |  5G
:-------------------------:|:-------------------------:
![](https://github.com/wsxqaza12/PandasSpeedTests/blob/master/result_png/groupby_agg1_1G_wins.png)  |  ![](https://github.com/wsxqaza12/PandasSpeedTests/blob/master/result_png/groupby_agg1_5G_wins.png)

## group by | agg 2 columns
1G            |  5G
:-------------------------:|:-------------------------:
![](https://github.com/wsxqaza12/PandasSpeedTests/blob/master/result_png/groupby_agg2_1G_wins.png)  |  ![](https://github.com/wsxqaza12/PandasSpeedTests/blob/master/result_png/groupby_agg2_5G_wins.png)

