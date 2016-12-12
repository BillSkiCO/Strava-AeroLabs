#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    dbconnect.py: connects to our MySQL database

    Initial Implementation: 12/10/2016 [William Golembieski]
    Last Modification: 12/11/2016 [William Golembieski]

"""
__author__ = "William Golembieski"
__email__ = "BillGolembieski@projectui23.com"

from MySQLdb import connect
from config import DB_HOST, DB_USER, DB_PASS, DB_DATABASE_NAME


def connection():
    """
    Connect to our database using MySQLdb.connect with values stored in config.py
    :return: cursor, database connection
    """
    conn = connect(host=DB_HOST,
                   user=DB_USER,
                   passwd=DB_PASS,
                   db=DB_DATABASE_NAME)

    # Define a cursor. This allows us to work with individual records instead of whole tables.
    # Effectively a pointer to a row. Warning: SLOW USAGE
    cursor = conn.cursor()

    return cursor, conn