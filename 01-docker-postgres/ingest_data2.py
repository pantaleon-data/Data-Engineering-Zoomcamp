#!/usr/bin/env python
# coding: utf-8

#!/usr/bin/env python

import click
import pandas as pd
from sqlalchemy import create_engine


@click.command()
@click.option('--target-table', default='zones', show_default=True)
@click.option('--pg-user', default='root', show_default=True)
@click.option('--pg-pass', default='root', show_default=True)
@click.option('--pg-host', default='localhost', show_default=True)
@click.option('--pg-port', default=5432, show_default=True, type=int)
@click.option('--pg-db', default='ny_taxi', show_default=True)

def run(target_table, pg_user, pg_pass, pg_host, pg_port, pg_db):

    csv_url = "https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv"

    engine = create_engine(
        f'postgresql+psycopg2://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}'
    )

    df = pd.read_csv(csv_url)

    df.to_sql(
        name=target_table,
        con=engine,
        if_exists='replace',
        index=False,
    )
    print("ok")


if __name__ == "__main__":
    run()