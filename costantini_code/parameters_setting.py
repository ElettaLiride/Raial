import pandas as pd
import tools as db


def changing_one_component_parameters(table, module=None, parameters=None):
    if module is None:
        module = [4, 0, 0]

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


def changing_one_parameter(table, module=None, parameter=None):
    if module is None:
        module = [4, 0, 0]

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
