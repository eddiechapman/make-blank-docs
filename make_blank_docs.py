"""
Create blank .docx files using a list of records in CSV format.

A blank document will be created for each 'FALSE' value in each row.
The documents will be named "[degree_id]-[category].docx". So if 
degree # 204 has a false "skills" value, the document will be named
"204-skills.docx".  

usage:
    $ python3 make_blank_docs.py -i [INPUT] -o [OUTPUT]

    INPUT
        Path to a .csv file containing columns:
            Degree_id   - (int) ID of a single degree program
            Skills      - (str) one of 'T', 'F'
            Mission     - (str) one of 'T', 'F'
            Courses     - (str) one of 'T', 'F'

    OUTPUT
        Path to a directory where the documents will be stored.

"""
import argparse
import csv
import logging
import pathlib
import docx


def main(args):
    logging.basicConfig(
        level=args.log_level or logging.INFO,
        filename='make_blank_docs.log',
        format='%(levelname)s:%(asctime)s:%(message)s'
    )

    INPUT = pathlib.Path(args.input)
    OUTPUT = pathlib.Path(args.output)

    if not INPUT.exists():
        logging.error(f'File not found: {args.input}')
        raise SystemExit
    elif not INPUT.is_file():
        logging.error(f'Not a file: {args.input}')
        raise SystemExit
    if not OUTPUT.exists():
        logging.error(f'Output path not found: {args.output}')
        raise SystemExit
    elif not OUTPUT.is_dir():
        logging.error(f'Output path is not a directory: {args.output}')
        raise SystemExit

    logging.info('Beginning program.')

    with open(INPUT, 'r') as f:
        logging.debug(f'File opened: {INPUT}')
        reader = csv.DictReader(f)
        for row in reader:
            logging.debug(row)
            degree_id = row['Degree_id'].zfill(3)
            for col in ['Skills', 'Courses', 'Mission']:
                if row[col] != 'T':
                    path = OUTPUT / f'{degree_id}-{col}.docx'
                    doc = docx.Document()
                    doc.save(path)
                    logging.debug(f'Document saved: {path}')
    
    logging.info(f'Program complete. Documents are located: {OUTPUT}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        '-v', '--verbose', 
        help='Verbose (debug) logging level.',
        const=logging.DEBUG, 
        dest='log_level',
        nargs='?',
    )
    group.add_argument(
        '-q', '--quiet',
        help='Silent mode, only log warnings and errors.',
        const=logging.WARN,
        dest='log_level',
        nargs='?',
    )
    parser.add_argument(
        '-i', '--input',
        required=True,
        metavar='input',
        type=str,
        help='the path to the csv file',
    )
    parser.add_argument(
        '-o', '--output',
        required=True,
        metavar='output',
        type=str,
        help='the path to the directory where documents will be stored.'
    )
    args = parser.parse_args()
    main(args)
