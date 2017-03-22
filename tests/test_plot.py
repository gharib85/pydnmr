# Currently not functional. Tried to use the path modification from The
# Hitchhiker's Guide to Python to get imports within test folder to work,
# but no dice. This has been a problem with other projects.
# TODO: resolve the problem of tests not being able to import project modules

# PyCharm keeps refering to this file as 'SimplePlot', the name of the
# file it was copied from?!

# noinspection PyUnresolvedReferences

import pytest
import pydnmr

def test_dnmrplot_2spin_type():

    WINDNMR_DEFAULT = (165.00, 135.00, 1.50, 0.50, 0.50, 0.5000)
    x, y = pydnmr.nmrplot.dnmrplot_2spin(*WINDNMR_DEFAULT)
    assert type(x) == 'list'


# if __name__ == '__main__':
#
#     import pyqtgraph as pg
#     WINDNMR_DEFAULT = (165.00, 135.00, 1.50, 0.50, 0.50, 0.5000)
#     x, y = pydnmr.nmrplot.dnmrplot_2spin(*WINDNMR_DEFAULT)
#     plt = pg.plot(x, y)
#     plt.show()