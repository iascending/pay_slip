#!/usr/bin/env python3
import pdb, random
import unittest
from faker import Faker

from PaySlip import PaySlip

fakegen = Faker()

class PaySlipTest(unittest.TestCase):

    def setUp(self):
        self.first_name     = fakegen.first_name()
        self.last_name      = fakegen.last_name()
        self.annual_salary  = fakegen.random_number(6)
        self.super_rate     = random.uniform(0, 0.5)
        self.pay_start_date = str(fakegen.date_this_year())
        self.employee = PaySlip(self.first_name, self.last_name, self.annual_salary, self.super_rate, self.pay_start_date)
        # pdb.set_trace()

    def test_payslip_create_first_name(self):
        with self.assertRaises(TypeError):
            PaySlip(42134, self.last_name, self.annual_salary, self.super_rate, self.pay_start_date)

    def test_payslip_create_last_name(self):
        with self.assertRaises(TypeError):
            PaySlip(self.first_name, False, self.annual_salary, self.super_rate, self.pay_start_date)

    def test_payslip_create_annual_salary(self):
        with self.assertRaises(TypeError):
            PaySlip(self.first_name, self.last_name, "annual_salary", self.super_rate, self.pay_start_date)
        with self.assertRaises(ValueError):
            PaySlip(self.first_name, self.last_name, -500000, self.super_rate, self.pay_start_date)

    def test_payslip_create_super_rate(self):
        with self.assertRaises(TypeError):
            PaySlip(self.first_name, self.last_name, self.annual_salary, "abc", self.pay_start_date)
        with self.assertRaises(ValueError):
            PaySlip(self.first_name, self.last_name, self.annual_salary, 0.5+self.super_rate, self.pay_start_date)
        with self.assertRaises(ValueError):
            PaySlip(self.first_name, self.last_name, self.annual_salary, -self.super_rate, self.pay_start_date)

    def test_payslip_create_pay_start_date(self):
        with self.assertRaises(TypeError):
            PaySlip(self.first_name, self.last_name, self.annual_salary, self.super_rate, 4123421)
        with self.assertRaises(ValueError):
            PaySlip(self.first_name, self.last_name, self.annual_salary, self.super_rate, "pay_start_date")

    def test_get_pay_period(self):
        employee = PaySlip(self.first_name, self.last_name, self.annual_salary, self.super_rate, "2019-04-05")
        self.assertEqual("05 Apr - 30 Apr", employee.get_pay_period())

    def test_get_gross_income(self):
        employee = PaySlip(self.first_name, self.last_name, 50001, self.super_rate, "2019-04-10")
        self.assertEqual(2917, employee.get_gross_income())

    def test_get_income_tax_range1(self):
        employee = PaySlip(self.first_name, self.last_name, 18200, self.super_rate, self.pay_start_date)
        self.assertEqual(0, employee.get_income_tax())

    def test_get_income_tax_range2(self):
        employee = PaySlip(self.first_name, self.last_name, 37000, self.super_rate, "2019-04-10")
        self.assertEqual(208, employee.get_income_tax())

    def test_get_income_tax_range3(self):
        employee = PaySlip(self.first_name, self.last_name, 87000, self.super_rate, "2019-04-01")
        self.assertEqual(1652, employee.get_income_tax())

    def test_get_income_tax_range4(self):
        employee = PaySlip(self.first_name, self.last_name, 180000, self.super_rate, "2019-04-01")
        self.assertEqual(4519, employee.get_income_tax())

    def test_get_income_tax_range5(self):
        employee = PaySlip(self.first_name, self.last_name, 200000, self.super_rate, "2019-04-01")
        self.assertEqual(5269, employee.get_income_tax())

    def test_get_net_income(self):
        employee = PaySlip(self.first_name, self.last_name, 50001, self.super_rate, "2019-04-10")
        self.assertEqual(2462, employee.get_net_income())

    def test_get_monthly_super(self):
        employee = PaySlip(self.first_name, self.last_name, 50001, 0.3, "2019-04-10")
        self.assertEqual(875, employee.get_monthly_super())

if __name__ == '__main__':
    unittest.main()
