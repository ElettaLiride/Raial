import pandas as pd
import tools as db


def changing_parameters1(parameters, table, sector=4, layer=0, component=0):
    if isinstance(table, pd.DataFrame):
        print("dentro primo if")
        if isinstance(parameters, list):
            table['sector']=table['sector'].astype(int)
            table['layer']=table['layer'].astype(int)
            table['component']=table['component'].astype(int)

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


def changing_parameters(parameters, table, module=None):
    if module is None:
        module = [4, 0, 0]

    sector = module[0]
    layer = module[1]
    component = module[2]

    if isinstance(table, pd.DataFrame):
        if isinstance(parameters, list):
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
