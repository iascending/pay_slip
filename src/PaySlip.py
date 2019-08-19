import calendar
from math import inf
from datetime import datetime

class PaySlip:
    """
    This is a class for employee's payslip operations.
    Class attributes:
        tax_rate: an array of tuples represent current tax table.
    Instance attributes:
        first_name:     a string for employee's first name.
        last_name:      a string for employee's last name.
        annual_salary:  an interger for employee's annual salary.
        super_rate:     a deciaml for employee's super rate [0 -0.5] inclusive.
        pay_start_date: a string represent of employee's payment start date.
        pay_end_date:   calculated employee's monthly payment end date.
        work_days_frac: calculated percentage of days employee worked in the month.
    """

    tax_rate_2017 = [
        (0,     18200,  0,      0),
        (18201, 37000,  0,      0.19),
        (37001, 87000,  3572,   0.325),
        (87001, 180000, 19822,  0.37),
        (180001,inf,    54232,  0.45)
    ]
    tax_rate_2019 = [
        (0,     18200,  0,      0),
        (18201, 37000,  0,      0.19),
        (37001, 90000,  3572,   0.325),
        (87001, 180000, 20797,  0.37),
        (180001,inf,    54232,  0.45)
    ]
    tax_rate = {2017: tax_rate_2017, 2019: tax_rate_2019}

    def __init__(self, first_name, last_name, annual_salary, super_rate, pay_start_date):
        """ The constructor of PaySlip Class. """
        if not isinstance(first_name, str):
            raise TypeError("first_name must be a string")
        self.first_name = first_name

        if not isinstance(last_name, str):
            raise TypeError("last_name must be a string")
        self.last_name  = last_name

        if not isinstance(annual_salary, int):
            raise TypeError("annual_salary must be an integer")
        if annual_salary <= 0:
            raise ValueError("annual_salary must be positive")
        self.annual_salary = annual_salary

        if not isinstance(super_rate, float):
            raise TypeError("super_rate must be a decimal")
        if super_rate < 0 or super_rate > 0.5:
            raise ValueError("super_rate: {}. It must be between (0, 0.5) inclusive".format(super_rate))
        self.super_rate = super_rate

        if not isinstance(pay_start_date, str):
            raise TypeError("pay_start_date must be a date represented by the string of ""%Y-%m-%d")
        try:
            self.pay_start_date = datetime.strptime(pay_start_date, "%Y-%m-%d").date()
            year  = self.pay_start_date.year
            self.tax_rate_year = year
            month = self.pay_start_date.month
            _, num_days = calendar.monthrange(year, month)
            self.pay_end_date  = datetime(year, month, num_days).date()
            work_days   = (self.pay_end_date - self.pay_start_date).days + 1
            self.work_days_frac = work_days/float(num_days)
        except ValueError:
            raise ValueError("Please use the date format %Y-%m-%d")

    def __str__(self):
        return "<PaySlip> object: {} {}".format(self.first_name, self.last_name)

    def get_pay_period(self):
        """Return a string of payment period based on pay_start_date."""
        start = self.pay_start_date.strftime("%d %b")
        end   = self.pay_end_date.strftime("%d %b")
        return "{} - {}".format(start, end)

    def get_gross_income(self):
        """Return gross income of the month."""
        return round(self.annual_salary/12.0*self.work_days_frac)

    def get_income_tax(self):
        """Return income tax of the month."""
        tax_rgn = [r for r in self.tax_rate[self.tax_rate_year] if r[0] <= self.annual_salary <= r[1]][0]
        return round((tax_rgn[2] + tax_rgn[3] * (self.annual_salary - tax_rgn[0]))/12.0*self.work_days_frac)

    def get_net_income(self):
        """Return net income of the month."""
        return self.get_gross_income() - self.get_income_tax()

    def get_monthly_super(self):
        """Return super paid for the month."""
        return round(self.get_gross_income()*self.super_rate)
