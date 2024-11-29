# Inventory Low Stock Checker

A Python library to fetch low stock items from an RDS database.
The user has to give the required query and RDS credentials.

When the stock quantity goes below a given threshold, it will be shown.

### A sample query is given below.

    query = f"""
        SELECT itemName, supplier, dateAdded, quantity
        FROM {table_name}
    """

Here the item name, supplier name, date added and quantity will be fetched from the table.

