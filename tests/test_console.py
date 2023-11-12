#!/usr/bin/python3
"""
testes the console
"""
import unittest
from unittest.mock import patch
from io import StringIO
import os
import json
import console
import tests
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):
    """
    tests console
    """
    @classmethod
    def setUpClass(self):
        """
        set up
        """
        self.typing = console.HBNBCommand()

    @classmethod
    def tearDownClass(self):
        """
        teardown method
        """
        os.remove("file.json")

    def test_docstring_test_console(self):
        """
        tests docstring
        """
        self.assertTrue(len(console.__doc__) >= 1)

    def test_console_doc(self):
        """
        tests for doc
        """
        self.assertTrue(len(self.__doc__) >= 1)

    def emptyline(self):
        """
        tests for empty line
        """
        with patch('sys.stdout', new=StringIO()) as f_output:
            self.typing.onecmd("\n")
            self.assertEqual(f_output.getvalue(), '')

    def test_create(self):
        """
        cmd output for create
        """
        with patch('sys.stdout', new=StringIO()) as f_output:
            self.typing.onecmd("create")
            self.assertEqual("** class name missing **\n",
                             f_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as f_output:
            self.typing.onecmd("create ClassSom")
            self.assertEqual("** class doesn't exist **\n",
                             f_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as f_output:
            self.typing.onecmd("create User")
            self.typing.onecmd("create User")

    def test_all(self):
        """
        tets all
        """
        with patch('sys.stdout', new=StringIO()) as f_output:
            self.typing.onecmd("all NonExist")
            self.assertEqual("** class doesn't exist **\n",
                             f_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as f_output:
            self.typing.onecmd("all Place")
            self.assertEqual("[]\n", f_output.getvalue())

    def test_destroy(self):
        """
        tests destroy function
        """
        with patch('sys.stdout', new=StringIO()) as f_output:
            self.typing.onecmd("destroy")
            self.assertEqual(" ** class name missing **\n",
                             f_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as f_output:
            self.typing.onecmd("destriy union")
            self.assertEqual(" ** class doesn't exist **\n",
                             f_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as f_output:
            self.typing.onecmd("destroy BaseModel")
            self.assertEqual(" ** instance id missing **\n",
                             f_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as f_output:
            self.typing.onecmd("destroy BaseModel 11111")
            self.assertEqual(" ** no instance found **\n",
                             f_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as f_output:
            self.typing.onecmd("User.destroy(11111)")
            self.assertEqual(" ** no instance found **\n",
                             f_output.getvalue())

    def test_update(self):
        """
        tests update
        """
        with patch('sys.stdout', new=StringIO()) as f_output:
            self.typing.onecmd("update")
            self.assertEqual(" ** class name missing **\n",
                             f_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as f_output:
            self.typing.onecmd("update union")
            self.assertEqual(" ** class doesn't exist **\n",
                             f_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as f_output:
            self.typing.onecmd("update BaseModel")
            self.assertEqual(" ** instance id missing **\n",
                             f_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as f_output:
            self.typing.onecmd("update User 1111")
            self.assertEqual(" ** no instance found **\n",
                             f_output.getvalue())

    def test_show(self):
        """
        tests show cmd
        """
        with patch('sys.stdout', new=StringIO()) as f_output:
            self.typing.onecmd("show")
            self.assertEqual(" ** class name missing **\n",
                             f_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as f_output:
            self.typing.onecmd("show BaseModel")
            self.assertEqual(" ** instance id missing **\n",
                             f_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as f_output:
            self.typing.onecmd("Place.show(11111)")
            self.assertEqual(" ** no instance found **\n",
                             f_output.getvalue())

    def test_count(self):
        """
        tests count
        """
        with patch('sys.stdout', new=StringIO()) as f_output:
            self.typing.onecmd("BaseModel.count()")
            self.assertEqual(int, type(eval(f_output.getvalue())))


if __name__ == "__main__":
    unittest.main()
