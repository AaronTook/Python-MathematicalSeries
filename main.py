"""
	Author: AaronTook (https://github.com/AaronTook/)
	Last modified : 3/6/2023
	Project name: Python MathematicalSeries
	File name: main.py
	File description: This file contains classes and functions for operations on and with Arithmetic and Aeometric series.
"""
import math

class GeometricSeries:
	""" A class used for operations on geometric series. """
	def __init__(self):
		self.type == "Geometric Series"
	def __str__(self):
		return self.type + " Object"
	def __repr__(self):
		return self.type + " Object"
	def getSum(n, A_1, r):
		""" Solve a geometric series using the first term as well as the number of terms and the common ratio. """
		S_n = A_1 * ((1-math.pow(r,n))/(1-r))
		return S_n
	def getN(A_1, A_n, r):
		""" Using the common ratio as well as the first and last terms, solve for the number of terms in the requested series. Use formula  A_n = A_1 * r^(n-1) to get n. """
		n = math.log(A_n/A_1, r) + 1
		return n

class ArithmeticSeries:
	""" A class used for operations on arithmetic series. """
	def __init__(self):
		self.type == "Arithmetic Series"
	def __str__(self):
		return self.type + " Object"
	def __repr__(self):
		return self.type + " Object"
	def getSumWithLastTerm(n, A_1, A_n):
		""" Solve an arithmetic series using the first and last term as well as the number of terms. This method uses Gauss' method for finding sums of arithmetic series. '"""
		S_n = (n/2) * (A_1 + A_n)
		return S_n
	def getSumWithD(n, A_1, d):
		""" Solve an arithmetic series using the first term as well as the number of terms and the common difference. """
		S_n = (n/2) * (2 * A_1 + (n-1) * d)
		return S_n
	def getN(A_1, A_n, d):
		""" Using the common difference as well as the first and last terms, solve for the number of terms in the requested series. """
		n = (A_n - A_1)/d
		return n
