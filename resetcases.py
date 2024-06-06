import sqlite3

db_path = 'db.sqlite3' 

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Delete migration history for the 'cases' app
cursor.execute("DELETE FROM django_migrations WHERE app='cases';")
print("Deleted migration history for 'cases' app")

# List of tables related to the 'cases' app
tables_to_drop = [
    'cases_criminalcase_associated_case_files',
    'cases_criminalcase',
    'cases_crimetype',
    'cases_crimesubcategory',
    # Add any other related tables here
]

# Drop the tables
for table_name in tables_to_drop:
    cursor.execute(f"DROP TABLE IF EXISTS {table_name};")
    print(f"Dropped table {table_name}")

conn.commit()
conn.close()
