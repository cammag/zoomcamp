import pandas as pd
import sqlalchemy
import argparse
import os

def main(paramns):
    user = paramns.user
    password = paramns.password
    host = paramns.host
    port = paramns.port
    database = paramns.database
    table = paramns.table
    url = paramns.url

    file_name = 'output.csv'

    os.system(f'cp {url} {file_name}')

    engine = sqlalchemy.create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')

    df = pd.read_csv(file_name)
    pd.to_datetime(df.tpep_pickup_datetime)
    pd.to_datetime(df.tpep_dropoff_datetime)

    df.head(100000).to_sql(name=table, con=engine, if_exists='append')

#user
#password
#host
#port
#databasename
#table name
#url

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Ingest some csv data to postgres.')
    parser.add_argument('--user', help='username for postgres')
    parser.add_argument('--password', help='password for postgres')
    parser.add_argument('--host', help='host for postgres')
    parser.add_argument('--port', help='port for postgres')
    parser.add_argument('--database', help='database name for postgres')
    parser.add_argument('--table', help='tablename for postgres')
    parser.add_argument('--url', help='url for the data source')

    args = parser.parse_args()

    main(args)