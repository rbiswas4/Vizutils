"""
"""
__all__ = ['filtSubplots']
import matplotlib.pyplot as plt


def filtSubplots(sharey=True, survey='lsst'):
    """
    Quick creation of subplots for filters ordered as ugrizy
    rather than alphabetically
    """
    if survey != 'lsst':
        raise NotImplementedError('Not implemented for survey {0} and only implemented for survey {1}'.format(survey, 'lsst'))

    fig, al = plt.subplots(2, 3, sharey=sharey)
    f ,ax = plt.subplots(2, 3, sharey=sharey)

    ax[1, 0] = al[0, 0]
    ax[0, 0] = al[0, 1]
    ax[0, 2] = al[0, 2]
    ax[0, 1] = al[1, 0]
    ax[1, 2] = al[1, 1]
    ax[1, 1] = al[1, 2]

    return fig, ax, al
