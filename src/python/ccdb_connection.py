import pandas as pd
import ccdb
from src.python import tools as db
from src.python import globalpath


def new_add():
    pass


def new_read():
    pass


def connecting_ccdb(calibration_connection=globalpath.CALIBRATION_CONNECTION,
                    variation=globalpath.VARIATION,
                    comment="",
                    user=globalpath.USER,
                    parent="default"):
    """

    connect to the ccdb

    :param calibration_connection:
    :param comment:
    :param parent:
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
        provider.create_variation(variation, comment, parent)
    return provider


def dumping_ccdb(mis_table=globalpath.CALIBRATION_TABLE, variation=globalpath.VARIATION, run=0, id=None):

    """

    read from the ccdb the misalignment table. If id is passed search for that table, otherwise pick the last one

    :param provider: provider object
    :param mis_table:
    :param variation:
    :param run:
    :param id:
    :return: a ccdb assignment object

    """
    provider = connecting_ccdb(globalpath.CALIBRATION_CONNECTION, variation)
    variation = provider.get_variation(variation)
    table = provider.get_type_table(mis_table)
    if id is not None:
        assignment = provider.get_assignments(table, run=run, variation=variation)
        assignment = provider.get_assignments_by_id(assignment, id)
    else:
        assignment = provider.get_assignment(table, run=run, variation=variation)
    return assignment


def reading_ccdb(mis_table=globalpath.CALIBRATION_TABLE, variation=globalpath.VARIATION, run=0, id=None, comment=""):
    assignment = dumping_ccdb(mis_table, variation, run=run, id=id)
    return convert_table_in_pd(assignment)


def convert_table_in_pd(assignment):
    """
    convert an assignment content of the calibration/rich/misalignments table in a pandas df with
    the same columns and rows
    :param assignment:
    :return:
    """

    columns = ['sector', 'layer', 'component', 'dx', 'dy', 'dz', 'dthx', 'dthy', 'dthz']
    df = pd.DataFrame(assignment.constant_set.data_table, columns=columns)
    df[df.columns[:3]] = df[df.columns[:3]].astype(float).astype(int)
    df[df.columns[3:]] = df[df.columns[3:]].astype(float)
    return df


def init_ccdb():
    adding_to_ccdb(list(map(list, globalpath.STARTING_TABLE.itertuples(index=False))),
                   table=globalpath.CALIBRATION_TABLE,
                   variation=globalpath.VARIATION)


def adding_to_ccdb(parameters, table=globalpath.CALIBRATION_TABLE, variation=globalpath.VARIATION, comment='Test'):
    """

    add to the ccdb a misalignment table with new parameters. The parameters have to be a list object

    :param parameters:
    :param provider:
    :param table:
    :param variation:
    :param comment:
    :return:
    """
    provider = connecting_ccdb(globalpath.CALIBRATION_CONNECTION, globalpath.VARIATION)
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


def old_init_ccdb(provider, calibration_table, variation):
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

if __name__=="__main__":
    init_ccdb()