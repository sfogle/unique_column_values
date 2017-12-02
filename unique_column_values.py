import csv
import argparse


def print_unique_column_values(csv_file_name, column_number):
    values = []
    with open(csv_file_name, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            values.append(row[column_number])
    for value in sorted(set(values)):
        print(value)


def main():
    parser = argparse.ArgumentParser(
        description=('Get the unique values '
                     'of a particular column from a csv file.'))
    parser.add_argument('csv_file_name')
    parser.add_argument('column_number', type=int)
    args = parser.parse_args()
    print_unique_column_values(args.csv_file_name, args.column_number)


if __name__ == '__main__':
    main()
