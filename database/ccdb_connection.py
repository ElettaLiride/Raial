import pandas as pd
import ccdb
import tools as db


def connecting_ccdb(calibration_connection, variation, user="anonymous"):
    provider = ccdb.AlchemyProvider()
    provider.connect(calibration_connection)
    provider.authentication.current_user_name = user

    try:
        provider.get_variation(variation)  # cheking if there is a variation
    except:
        create_variation(provider, variation)

    return provider


def reading_ccdb(provider, mis_table, variation, run=0):
    variation = provider.get_variation(variation)  # That is how you get variation
    table = provider.get_type_table(mis_table)
    assignment = provider.get_assignment(table, 1, variation)

    columns = ['sector', 'layer', 'component', 'dx', 'dy', 'dz', 'dthx', 'dthy', 'dthz']
    pars = pd.DataFrame(assignment.constant_set.data_table, columns=columns)

    return pars


def create_variation(provider, variation, parent="default", comment=""):
    parent_var = provider.create_variation(variation, comment, parent)


def adding_to_ccdb(parameters, provider, table, variation, comment=""):
    if isinstance(parameters, list):
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
