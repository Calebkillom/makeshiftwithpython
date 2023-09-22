#!/usr/bin/python3
# This is a script to practise and cover **kwargs


def Person(**kwargs):
    """function that prints key, value pairs passed to it."""
    for key, value in kwargs.items():
        print(key, "->", value)


def print_kwargs(**kwargs):
    """function that prints the entire dict."""
    print(kwargs)


Person(Name='Rahul', Sex='Male', Age=38, City='Hyderabad', Mobile=123456789)
print_kwargs(kwargs_1="Whale", kwargs_2=5, kwargs_3=False, kwargs_4=2.1)
