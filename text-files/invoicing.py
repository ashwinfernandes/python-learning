import datetime
from os import SEEK_SET
from typing import TextIO


def get_year() -> int:
    """Return the current year as an integer."""
    return datetime.datetime.now().year


def parse_invoice_number(invoice_number: str) -> tuple[int, int]:
    """Split a well-formed invoice "number" into its component parts.

    :param invoice_number: A string of the form YYYY-NNNN
        YYYY is the 4 digit year.
        NNNN is a 4 digit invoice number, left padded with zeros.
        The 2 parts are separated with a "-" character.
    :return: The returned tuple will contain:
        the 4 digit year as an integer,
        the invoice number as an integer.
    """
    year, number = invoice_number.split("-")
    return int(year), int(number)


def next_invoice_number(invoice_number: str) -> str:
    """ Produce the next invoice "number" in sequence.

    The format of `invoice_number` is described in `parse_invoice_number`.

    :param invoice_number: A string representing an invoice number.
    :return: A string representing the next invoice number.
        The numerical part will be incremented, unless the current year
        isn't the same as the year in `invoice_number`. In that case,
        the new invoice number will contain the current year, and the
        numerical part will be set to "0001".
    """
    year, number = parse_invoice_number(invoice_number)
    curr_year = get_year()

    if curr_year != year:
        return f"{curr_year}-{1:04d}"
    else:
        return f"{year}-{number + 1:04d}"


def record_invoice(invoice_file: TextIO,
                   company: str,
                   amount: float,
                   last_line_ptr:int = 0) -> int:
    """Create a new invoice number, and write it to a file on disk.

    :param invoice_file: An open text file, opened using r+.
    :param company: The name of the company being invoiced.
    :param amount: The amount of the invoice.
    :param last_line_ptr: The position of the start of the last line in
        the file. This will be obtained by the previous call to
        `record_invoice`.
    :return: The position of the start of the last line in the file.
        This can be used in subsequent calls to `record_invoice`.
    """
    invoice_file.seek(last_line_ptr, SEEK_SET)
    last_row = ''
    for line in invoice_file:
        print('*', end='') # TODO delete after testing
        last_row = line
    if last_row:
        # invoice_number, _, _ = last_row.split('\t')
        invoice_number = last_row.split('\t')[0]
        new_invoice_number = next_invoice_number(invoice_number)
    else:
        # if the file is empty, we'll start numbering from 1.
        year = get_year()
        new_invoice_number = f'{year}-{1:04d}'

    last_line_ptr = invoice_file.tell()
    print(f'{new_invoice_number}\t{company}\t{amount}', file=invoice_file)
    return last_line_ptr

data_file = 'invoices.csv'

with open(data_file, 'r+') as invoices:
    last_line = record_invoice(invoices, 'ACME Roadrunner', 18.40)
    last_line = record_invoice(invoices, 'Squirrel Storage', 320.55, last_line)
