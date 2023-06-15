#include <stdio.h>
#include <Python.h>

void print_python_bytes(PyObject *p)
{
	char *str;
	Py_ssize_t length, z;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
		printf("  [ERROR] Invalid Bytes Object\n");
	else
	{
		PyBytes_AsStringAndSize(p, &str, &length);
		printf("  size: %lu\n", length);
		printf("  trying string: %s\n", str);
		if (length > 10)
			length = 10;
		else
			length++;
		printf("  first %lu bytes: ", length);
		for (z = 0; z < length - 1; z++)
			printf("%02x ", str[z] & 0xff);
		printf("%02x\n", str[length - 1] & 0xff);
	}
}

void print_python_list(PyObject *p)
{
	Py_ssize_t z;
	PyObject *list;

	if (PyList_Check(p))
	{
		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %lu\n", PyList_Size(p));
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		for (z = 0; z < PyList_Size(p); z++)
		{
			list = PySequence_GetItem(p, z);
			printf("Element %lu: %s\n", z,
					list->ob_type->tp_name);
			if (strcmp(list->ob_type->tp_name, "bytes") == 0)
				print_python_bytes(list);
		}
	}
}
