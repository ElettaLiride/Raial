import pandas as pd
import ccdb
import debugging_tools as db
import numpy as np

def connecting_ccdb(calibration_connection, user="anonymous"):
    provider = ccdb.AlchemyProvider()
    provider.connect(calibration_connection)
    provider.authentication.current_user_name = user
    return provider

def reading_ccdb(provider, mis_table, variation, run=0):

    variation = provider.get_variation(variation)  # That is how you get variation
    table = provider.get_type_table(mis_table)
    assignment = provider.get_assignment(1, table, variation)

    columns = ['sector', 'layer', 'component', 'dx', 'dy', 'dz', 'dthx', 'dthy', 'dthz']
    pars = pd.DataFrame(assignment, columns=columns)

    return pars


def adding_to_ccdb(parameters, provider, table, variation, comment=""):
    if isinstance(parameters,list):
        provider.create_assignment(
            data=parameters,
            path=table,
            variation_name=variation,
            min_run=0,
            max_run=ccdb.INFINITE_RUN,
            comment=comment)

    else:
        print('some problem here: line {}'.format(db.line_numb()))
        raise ValueError

    return 0


