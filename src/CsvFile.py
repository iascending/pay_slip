import pdb, csv, sys
from functools import reduce
from datetime import datetime

class CsvFile:
    """
    This is an class for reading and writing .csv file operations.
    attributes:
        file_name:      file_name to be opened for csv file read or write.
        fieldnames:     column names to be writen into output csv file.
        pay_slip_list:  a list of PaySlip objects created from input csv file.
        pay_slip_info:  a list of PaySlip details writen to output csv file.
    """
    def __init__(self, file_name, fieldnames=None):
        """The constructor of class. """
        self.file_name       = file_name
        self.fieldnames      = fieldnames
        self.staff_info_list = []

    def read(self):
        """
        Read employee basic payment info from a csv file,
        save into PaySlip object, and
        store as the element of pay_slip_list
        """
        with open(self.file_name, newline='') as fh:
            reader = csv.reader(fh)
            try:
                for row in reader:
                    if reader.line_num == 1:
                        if self.fieldnames != row:
                            raise ValueError('Field names should be {}'.format(self.fieldnames))
                    else:
                        self.staff_info_list.append([row[0], row[1], int(row[2]), float(row[3].strip('%'))/100,
                                                    datetime.strptime(row[4], "%d-%b-%y").date().strftime("%Y-%m-%d")])
                return self.staff_info_list
            except csv.Error as e:
                sys.exit('file {}, line {}: {}'.format(self.file_name, reader.line_num, e))

    def write(self, pay_slip_list):
        """Write calculated employee detailed payment info into a csv file. """
        with open(self.file_name, 'w', newline='') as fh:
            writer = csv.DictWriter(fh, fieldnames=self.fieldnames)
            writer.writeheader()

            pay_slip_info = [(el.first_name + " " + el.last_name,
                              el.get_pay_period(),
                              el.get_gross_income(),
                              el.get_income_tax(),
                              el.get_net_income(),
                              el.get_monthly_super()
                             ) for el in pay_slip_list ]
            for el in pay_slip_info: print("    {}".format(el))
            writer.writerows([dict(zip(self.fieldnames, x)) for x in pay_slip_info])