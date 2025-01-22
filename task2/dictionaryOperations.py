# DB = {
#    "TB1": {  # Table 1
#         "columns": ["col1", "col2", "col3"],  # Column names
#         "rows": [
#             [value1, value2, value3],  # Row 1
#             [value4, value5, value6],  # Row 2
#             ...
#         ]
#    },
#    "TB2": {  # Table 2
#         "columns": ["colA", "colB", "colC"],  # Column names
#         "rows": [
#             [value1, value2, value3],  # Row 1
#             [value4, value5, value6],  # Row 2
#             ...
#         ]
#    },
#    # ...
# }

class Table:
    def __init__(self, tableName, attributes):
        self.tableName = tableName
        self.attributes = attributes
        self.rows = []

    def insertRow(self, row):
        self.rows.append(row)

    def getRow(self, primaryKey):
        for row in self.rows:
            if row[0] == primaryKey:
                return row
        return None

    def deleteRow(self, primaryKey):
        for row in self.rows:
            if row[0] == primaryKey:
                self.rows.remove(row)

    def showTable(self):
        print("Table Name: ", self.tableName)
        print("Attributes: ", self.attributes)
        print("Rows: ", self.rows)

class Database:
    def __init__(self):
        self.tables = {}

    def createTable(self, tableName, attributes):
        table = Table(tableName, attributes)
        self.tables[tableName] = table

    def getTable(self, tableName):
        return self.tables[tableName]

    def deleteTable(self, tableName):
        del self.tables[tableName]

    def showDatabase(self):
        for tableName in self.tables:
            self.tables[tableName].showTable()

if __name__ == "__main__":
    db = Database()

    db.createTable("TB1", ["stdID", "stdName", "branch"])
    db.createTable("TB2", ["profID", "profName", "subject"])

    tb1 = db.getTable("TB1")

    tb1.insertRow([202301000, "Harry", "potion"])
    tb1.insertRow([202301001, "Ron", "Defense Against the Dark Arts"])
    tb1.insertRow([202301002, "Hermione", "Transfiguration"])
    tb1.showTable()

    print()

    print(tb1.getRow(202301001))
    tb1.deleteRow(202301001)
    tb1.showTable()

    print()

    tb2 = db.getTable("TB2")
    tb2.insertRow([101, "Snape", "Potions"])
    tb2.insertRow([102, "McGonagall", "Transfiguration"])
    tb2.insertRow([103, "Tralawney", "Divination"])
    db.showDatabase()

    print()

    db.deleteTable("TB1")

    print()

    db.showDatabase()
