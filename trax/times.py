import time
import csv
import matplotlib.pyplot as plt
import pandas as pd
import concurrent.futures as cf


def get_column_pandas(path, column):
    """
    Uses pandas library to
    extract a single column from
    a .csv file
    :param path: path to .csv file
    :param column: column to extract
    :rtype: list
    """
    start_time = time.time()
    col_df = pd.read_csv(path, sep=';', usecols=[column])
    col_l = col_df[column].to_list()
    stop_time = time.time()
    execution_time = stop_time - start_time
    return execution_time, len(col_l), col_l


def col_list(file, column):
    """
    Extracts a single column from
    text file
    :param file: file to read
    :param column: column to extract
    :return: list
    """
    for i in csv.DictReader(file, delimiter=';'):
        col_l = i[column]
    return col_l


def get_column_future(path, column):
    """
    Extracts a single column from
    .csv file using csv read method
    while engaging multiple processors
    :param path:
    :param column:
    :return:
    """
    start_time = time.time()
    with open(path, 'r'):
        with cf.ProcessPoolExecutor(max_workers=4) as executor:
            list_c = [executor.submit(col_list, column=column)]
    stop_time = time.time()
    execution_time = stop_time - start_time
    return execution_time, len(list_c), list_c


def plot_times(list_pandas, list_csv):
    """
    Plots a comparison of
    time efficiency between two different
    functions
    :param list_pandas: list of values
    from pandas method
    :param list_csv: list of values from
    csv multiple processor method
    :return: execution times and plot
    """
    xs = []
    ys_pandas, ys_csv = [], []
    for i in list_pandas:
        for x in i:
            xs.append(x[1])
            ys_pandas.append(x[0])
    for i in list_csv:
        for y in i:
            ys_csv.append(y[0])
    print(xs)
    print(ys_pandas)
    print(ys_csv)

    plt.figure()
    plt.plot(xs, ys_pandas, xs, ys_csv, marker='o')
    plt.legend(["pandas", "csv multiple processes"])
    plt.xlabel('cases')
    plt.ylabel('time')
    plt.title('Execution time')
    plt.show()
