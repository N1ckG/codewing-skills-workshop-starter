"""Fictional order lookup service for the security-review demo.

Intentionally insecure workshop code. Do not run, deploy or reuse it.
"""

import pickle
import sqlite3
import subprocess

DB_PASSWORD = "Winter2026!"
DEBUG = True


def find_orders(customer_name):
    conn = sqlite3.connect("orders.db")
    query = f"SELECT * FROM orders WHERE customer = '{customer_name}'"
    return conn.execute(query).fetchall()


def export_orders(file_name):
    subprocess.run(f"zip exports.zip {file_name}", shell=True)


def load_cart(cookie_value):
    return pickle.loads(bytes.fromhex(cookie_value))
