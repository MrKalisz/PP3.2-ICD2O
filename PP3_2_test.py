import os.path
import sys
import PP3_2

def test_q1_1(capsys):

	try:
		exists = os.path.exists("PP3_2.py")
		assert exists
	except:
		sys.exit()

	input_values = ['-1', '7']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP3_2.input = mock_input

	PP3_2.q1()
	captured = capsys.readouterr()
	assert captured.out == "Input a positive integer: Input a positive integer: 14\n"

def test_q2_1(capsys):

	try:
		exists = os.path.exists("PP3_2.py")
		assert exists
	except:
		sys.exit()

	input_values = ['Hello', 'Bye']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP3_2.input = mock_input

	PP3_2.q2()
	captured = capsys.readouterr()
	assert captured.out == "Input a password: Confirm the password: Input a password: Confirm the password: success.\n"

def test_q3_1(capsys):

	try:
		exists = os.path.exists("PP3_2.py")
		assert exists
	except:
		sys.exit()

	input_values = ['Yes', 'Yes', '5', '7']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP3_2.input = mock_input

	PP3_2.q3()
	captured = capsys.readouterr()
	assert captured.out == "Input an integer: Input an integer that is a multiple of the first integer: Input an integer: Input an integer that is a multiple of the first integer: success.\n"

def test_q1_2(capsys):

	try:
		exists = os.path.exists("PP3_2.py")
		assert exists
	except:
		sys.exit()

	input_values = ['7', '14', '-1']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP3_2.input = mock_input

	PP3_2.q1()
	captured = capsys.readouterr()
	assert captured.out == "Input a positive integer: Input a positive integer: Input a positive integer: 0\n"

def test_q2_2(capsys):

	try:
		exists = os.path.exists("PP3_2.py")
		assert exists
	except:
		sys.exit()

	input_values = ['-5', '0', 'Hello']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP3_2.input = mock_input

	PP3_2.q2()
	captured = capsys.readouterr()
	assert captured.out == "Input a password: Confirm the password: Input a password: Confirm the password: Input a password: Confirm the password: success.\n"

def test_q3_2(capsys):

	try:
		exists = os.path.exists("PP3_2.py")
		assert exists
	except:
		sys.exit()

	input_values = ['hello', 'Hello', 'Bye', 'Bye', 'Bye', '5']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP3_2.input = mock_input

	PP3_2.q3()
	captured = capsys.readouterr()
	assert captured.out == "Input an integer: Input an integer that is a multiple of the first integer: Input an integer: Input an integer that is a multiple of the first integer: Input an integer: Input an integer that is a multiple of the first integer: success.\n"

def test_q1_3(capsys):

	try:
		exists = os.path.exists("PP3_2.py")
		assert exists
	except:
		sys.exit()

	input_values = ['12']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP3_2.input = mock_input

	PP3_2.q1()
	captured = capsys.readouterr()
	assert captured.out == "Input a positive integer: 10\n"

def test_q2_3(capsys):

	try:
		exists = os.path.exists("PP3_2.py")
		assert exists
	except:
		sys.exit()

	input_values = ['2']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP3_2.input = mock_input

	PP3_2.q2()
	captured = capsys.readouterr()
	assert captured.out == "Input a password: Confirm the password: success.\n"

def test_q3_3(capsys):

	try:
		exists = os.path.exists("PP3_2.py")
		assert exists
	except:
		sys.exit()

	input_values = ['9', '4']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP3_2.input = mock_input

	PP3_2.q3()
	captured = capsys.readouterr()
	assert captured.out == "Input an integer: Input an integer that is a multiple of the first integer: success.\n"

