import pandas as pd
from run_control import tools as db



def changing_one_component_parameters(table, module, parameters):
    '''

    :param table:
    :param module:
    :param parameters:
    :return:
    '''

    sector = module[0]
    layer = module[1]
    component = module[2]

    if isinstance(table, pd.DataFrame):
        if isinstance(parameters, list):
            table['sector'] = table['sector'].astype(int)
            table['layer'] = table['layer'].astype(int)
            table['component'] = table['component'].astype(int)

            table.loc[((table['sector'] == sector) & (table['layer'] == layer) & (
                        table['component'] == component)), table.columns.tolist()] = [sector, layer,
                                                                                      component] + parameters
        else:
            print('some problem here: line {}'.format(db.line_numb()))
            raise ValueError
    else:
        print('some problem here: line {}'.format(db.line_numb()))
        raise ValueError

    return table


def changing_one_parameter(table, module, parameter):
    """
    change a parameter of the module in the ccdb table given.

    :param table: pd.Dataframe describing the ccdb table (dataframe columns == table columns)
    :param module: list of three int (sector, layer, component)
    :param parameter: list of len 2, name of parameter value of parameter
    :return: pd.Dataframe, the table changed
    """

    sector = module[0]
    layer = module[1]
    component = module[2]

    if isinstance(table, pd.DataFrame):
        if isinstance(parameter, list):
            table['sector'] = table['sector'].astype(int)
            table['layer'] = table['layer'].astype(int)
            table['component'] = table['component'].astype(int)

            table.loc[((table['sector'] == sector) & (table['layer'] == layer) & (
                    table['component'] == component)), parameter[0]] = parameter[1]
    else:
        print('some problem here: line {}'.format(db.line_numb()))
        raise ValueError

    return table

