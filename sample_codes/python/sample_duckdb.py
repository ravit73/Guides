import duckdb

print(duckdb.__version__)


# vytvoreni in-memory databaze
# con = duckdb.connect(database=':memory:')
# con.execute("INSTALL httpfs;")
# con.execute("LOAD httpfs")

# pripojeni k existujici databazi

mydb = duckdb.connect('C:/Users/radek.vitek/OneDrive - AKKA/AzureDevops/duckdb/smallwarehouse.db')

# definice URL CNB kurzu
kurzy = 'https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/rok.txt?2025'

myrates = \
        mydb.read_csv(kurzy, sep='|')


#mydb.execute("SELECT * from myrates").fetchall()

myrates.execute("""
                DROP TABLE IF EXISTS myrates;
                SELECT * FROM myrates;
                """)


mydb.close()
print("Code is OK")