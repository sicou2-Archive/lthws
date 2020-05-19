# from pytest import *
# import unittest.mock


# def yes_or_no():
#     answer = input("Do you want to quit?")
#     if answer == 'yes':
#         return("Quitter!")
#     elif answer == 'no':
#         return("Awesome")
#     else:
#         return("Bang!")


# def test_quitting():
#     with mock.patch('builtins.input', return_value="yes"):
#         assert yes_or_no() == "Quitter!"

#     with mock.patch('builtins.input', return_value="no"):
#         assert yes_or_no() == "Awesome!"


# from pytest import *
# from unittest import mock
# import ex47
# import io


# def test_white():
#     print("Help")


# def foo():
#     print("Something")

# # Solution one: testing print with @patch


# @mock.patch('sys.stdout', new_callable=io.StringIO)
# def test_foo_one(mock_stdout):
#     foo()
#     assert mock_stdout.getvalue() == 'Something\n'

# # Solution two: testing print with with-statement


# def test_foo_two():
#     with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
#         foo()
#     assert fake_sedout.getvalue() == 'Something\n'

# # Solution three: testing print with-statement and assert_has_calls


# def test_foo_three():
#     with mock.patch('sys.stdout') as fake_sedout:
#         foo()

#     fake_stdout.assert_has_calls([
#         mock.call.write('Something'),
#         mock.call.write('\n')
#     ])


# def bar():
#     ans = input("Enter yes or no")
#     if ans == "yes":
#         return "you entered yes"
#     if ans == "no":
#         return "you entered no"


# def test_bar_yes():
#     original_input = mock.builtins.input
#     mock.builtins.input = lambda _: "yes"
#     assert_equal(bar(), "you entered yes")
#     mock.builtins.input = original_input


# def test_bar_no():
#     original_input = mock.builtins.input
#     mock.builtins.input = lambda _: "no"
#     assert_equal(bar(), "you entered no")
#     mock.builtins.input = original_input
