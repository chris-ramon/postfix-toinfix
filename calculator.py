# -*- coding: utf-8 -*-
import unittest
import re
import operator
class Calculator:
	def __init__(self, expr):
		expr = list(expr)
		self.expr = expr
		self.stack = []
		print 'la exp es' + str(self.expr)
		self.operations = {"+" : operator.add , \
		"-" : operator.sub, "*" : operator.mul, \
		"/" : operator.floordiv }

	def get_element(self):
		element = self.expr[0]
		self.expr.pop(0)
		return element

	def check_type(self, value):
		m = re.match(r'[\+\-\*\/]', value)
		if m:
			return 'operator'
		m = re.match(r'[\d+]', value)
		if m:
			return 'operand'

	def add_to_stack(self, val):
		self.stack.append( val )
		return self.stack

	def solve_expression(self):
		for element in self.expr:
			print 'element evaluating ' + element
			element_type = self.check_type(element)
			if element_type == 'operator':
				operator = element
				last_element = self.stack.pop()
				second_last_element = self.stack.pop()
				result = self.solve_operation(second_last_element, \
					last_element, operator)
				self.add_to_stack( result )
			if element_type != 'operator':
				print 'agregando '  + element
				self.add_to_stack( element )
		return self.stack

	def solve_operation(self, value1, value2, operator):
		print "expression " + str(value1) + operator + str(value2) 
		return self.operations[operator](int(value1), int(value2))


cee = Calculator("45+")
_cee = Calculator("45+")
_cee2 = Calculator("49-")
_cee3 = Calculator("456*+")
_cee4 = Calculator("456*+2-")
class CalculatorTest(unittest.TestCase):
	def test_init(self):
		self.assertEquals(True, isinstance(cee, Calculator) )

	def test_check_type(self):
		self.assertEquals('operand', cee.check_type("1"))
		self.assertEquals('operator', cee.check_type("*"))
		self.assertEquals('operator', cee.check_type("-"))
		self.assertEquals('operator', cee.check_type("/"))
		self.assertEquals('operator', cee.check_type("+"))
		self.assertEquals(None, cee.check_type("asd"))

	def test_add_to_stack(self):
		self.assertEquals([4], cee.add_to_stack(4))
		self.assertEquals([4,5], cee.add_to_stack(5))

	def test_solve_operation(self):
		#self.assertEquals(3, cee.solve_operation(1,2,"+"))
		#self.assertEquals(8, cee.solve_operation(4,2,"*"))
		#self.assertEquals(1, cee.solve_operation(2,2,"/"))
		#self.assertEquals(5, cee.solve_operation(7,2,"-"))
		pass

	def test_solve_expression(self):
		#self.assertEquals([9], _cee.solve_expression())
		self.assertEquals([-5], _cee2.solve_expression())
		self.assertEquals([34], _cee3.solve_expression())
		self.assertEquals([32], _cee4.solve_expression())

if __name__ == '__main__':
    unittest.main()