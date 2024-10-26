# This file should take the cvs data and convert it into a database, or .db file
# performs the CREATE from CRUD operations
import sqlite3
import csv


def transform(data):
    """Transforms and loads data into the database"""

    payload = csv.reader(open(data, newline=""), delimiter=",")
    next(payload)

    conn = sqlite3.connect("remotehealthDB.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS remote_health")
    c.execute(
        """
              CREATE TABLE remote_health (
                    Employee_ID,
                    Gender, 
                    Age,
                    Job_Role,
                    Industry,
                    Years_of_Experience,
                    Work_Location,
                    Hours_Worked_Per_Week,
                    Number_of_Virtual_Meetings,
                    Work_Life_Balance_Rating,
                    Stress_Level,
                    Mental_Health_Condition,
                    Access_to_Mental_Health_Resources,
                    Productivity_Change,
                    Social_Isolation_Rating,
                    Satisfaction_with_Remote_Work,
                    Company_Support_for_Remote_Work,
                    Physical_Activity,
                    Sleep_Quality,
                    Region 
                  )
              """
    )
    # insert
    c.executemany(
        """INSERT INTO remote_health VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        payload,
    )
    conn.commit()
    conn.close()
    print(payload)
    return payload
