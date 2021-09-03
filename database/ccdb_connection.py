import pandas as pd
import ccdb
from run_control import tools as db


def connecting_ccdb(calibration_connection, variation, user="anonymous"):
    """

    connect to the ccdb

    :param calibration_connection:
    :param variation: variation of interest
    :param user: Name of the user which changes the ccdb
    :return: a provider object which anable the comunication with the ccdb

    """
    provider = ccdb.AlchemyProvider()
    provider.connect(calibration_connection)
    provider.authentication.current_user_name = user

    try:
        provider.get_variation(variation)  # cheking if there is a variation
    except:
        create_variation(provider, variation)

    return provider


def reading_ccdb(provider, mis_table, variation, run=0):

    """

    read from the ccdb the misalignment table

    :param provider: provider object
    :param mis_table:
    :param variation:
    :param run:
    :return: pandas dataframe with a column for each column of the misalignment table in the ccdb

    """
    variation = provider.get_variation(variation)
    table = provider.get_type_table(mis_table)
    assignment = provider.get_assignment(table, 1, variation)

    columns = ['sector', 'layer', 'component', 'dx', 'dy', 'dz', 'dthx', 'dthy', 'dthz']
    pars = pd.DataFrame(assignment.constant_set.data_table, columns=columns)

    return pars


def create_variation(provider, variation, parent="default", comment=""):
    _ = provider.create_variation(variation, comment, parent)


def adding_to_ccdb(parameters, provider, table, variation, comment='Test'):
    """

    add to the ccdb a misalignment table with new parameters. The parameters have to be a list object

    :param parameters:
    :param provider:
    :param table:
    :param variation:
    :param comment:
    :return:
    """

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


def init_ccdb(provider, calibration_table, variation):
    """
    set all the parameters in the calibration_table to 0

    :param provider:
    :param calibration_table:
    :param variation:
    :return:
    """

    old_pars_table = reading_ccdb(provider, calibration_table, variation)
    for col in old_pars_table.columns:
        if col == "sector" or col == "layer" or col == "component":
            continue
        else:
            old_pars_table[col].values[:] = 0
    to_add = old_pars_table.values.tolist()
    adding_to_ccdb(to_add, provider, calibration_table, variation)