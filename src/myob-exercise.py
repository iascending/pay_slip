#!/usr/bin/env python3
import pdb, csv, os
from datetime import datetime

from PaySlip import PaySlip
from CsvFile import CsvFile

if __name__ == "__main__":

    src_field_names = ['First Name', 'Last Name', 'Annual Salary', 'Super Rate', 'Payment Start Date']
    out_field_names = ['Name', 'Pay Period', 'Gross Income', 'Income Tax', 'Net Income', 'Super']

    print("\nStarting to read input CSV file ..........")
    staff_info_list = CsvFile(os.path.join(os.path.dirname(__file__), 'input.csv'), src_field_names).read()

    pay_slip_list   = [PaySlip(*item) for item in staff_info_list]

    for item in pay_slip_list: print("    {}".format(item))
    print("Completed input CSV file reading..........")

    # pdb.set_trace()
    print("\nWriting following PaySlips into output CSV file ..........")
    CsvFile(os.path.join(os.path.dirname(__file__), 'output.csv'), out_field_names).write(pay_slip_list)
    print("Completed output CSV file writing..........................\n")
