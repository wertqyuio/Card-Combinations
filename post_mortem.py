# python script that details common post-game insights
from database_helper_functions import create_connection, execute_read_query
from database_credentials import PGDATABASE, PGUSER, PGPASSWORD, PGHOST, PGPORT
# currently only reports 5 most common distributions

connection = create_connection(
    PGDATABASE, PGUSER, PGPASSWORD, PGHOST, PGPORT
)


def base_insights():
    select_distributions = '''SELECT LENGTH(LONG), LENGTH(SHORT), COUNT(*) AS FREQUENCY FROM DISTRIBUTIONS
                      GROUP BY LENGTH(LONG), LENGTH(SHORT)
                      ORDER BY FREQUENCY DESC
                      LIMIT 5; '''

    distributions = execute_read_query(connection, select_distributions)

    for distribution in distributions:
        print(
            f"Split {distribution[0]}-{distribution[1]} appeared {distribution[2]} times.")


base_insights()
