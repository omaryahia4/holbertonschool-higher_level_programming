#!/usr/bin/python3
''' lists cities from given state from the database hbtn_0e_0_usa '''


def list_all_cities():
    import MySQLdb
    import sys
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("""SELECT cities.name FROM cities JOIN states \
            ON states.id = cities.state_id WHERE states.name=%s
            ORDER BY cities.id""", (sys.argv[4],))
    query_rows = cur.fetchall()
    if query_rows is None:
        print("")
    for i in range(len(query_rows)):
        if len(query_rows)-1 == i:
            print("{}".format(query_rows[i][0]))
        else:
            print("{}, ".format(query_rows[i][0]), end="")
    cur.close()
    conn.close()


if __name__ == "__main__":
    list_all_cities()
