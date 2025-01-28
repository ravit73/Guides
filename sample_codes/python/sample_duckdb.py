import duckdb

print(duckdb.__version__)

# vytvoreni in-memory databaze
# con = duckdb.connect(database=':memory:')

# vytvoreni extensions pro připojení k httpfs
# con.install_extension("httpfs")
# con.load_extension("httpfs")

# pripojeni k existujici databazi nebo vytvoření databáze na disku
with duckdb.connect('C:/Users/radek.vitek/OneDrive - AKKA/AzureDevops/duckdb/smallwarehouse.db') as mydb:
    
    
    # definice URL CNB kurzu
    kurzy = 'https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/rok.txt?2025'

    # nacteni dat z URL a ulozeni do typu dataframe duckdb.duckdb.DuckDBPyRelatio
    myrates = mydb.read_csv(kurzy, sep='|')

    # vytvoreni tabulky rates ve schématu test z relace myrates
    mydb.execute("""
                CREATE OR REPLACE TABLE test.rates AS
                SELECT * FROM myrates;
                """)
    
# if mydb:
#     print("DB not closed")
# else:
#     print("Code is OK")
print("Code is OK")