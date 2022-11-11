import numpy as np
import matplotlib.pyplot as plt


category_names = ['A+','A','A-','B+','B','B-','C+','C','C-','D+','D','D-','F','W']
results = {
    
    'Yu, Albert': [37,33,5,8,5,1,1,1,0,1,2,0,0,1],
    #'Yu, Albert: '[38.95, 34.74, 5.27, 8.43, 5.27, 1.06, 1.06, 1.06, 0, 1.06, 2.11, 0, 0, 1.06],
    'Unger, David': [1,20,14,5,11,5,2,5,1,2,0,1,5,1],
    #'Unger, David: ' [1.37, 27.4, 19.18, 6.85, 15.07, 6.85, 2.74, 6.85, 1.37, 2.74, 0, 1.37, 6.85, 1.37],
    'Nguyen, Ha Khanh': [7,76,16,18,14,11,12,6,5,5,1,3,10,3],
    #'Nguyen, Ha Khanh: ' [3.75, 40.65, 8.56, 9.63, 7.49, 5.89, 6.42, 3.21, 2.68, 2.68, 0.54, 1.61, 5.35, 1.61],
    
    
}


def survey(results, category_names):
    """
    Parameters
    ----------
    results : dict
        A mapping from question labels to a list of answers per category.
        It is assumed all lists contain the same number of entries and that
        it matches the length of *category_names*.
    category_names : list of str
        The category labels.
    """
    labels = list(results.keys())
    data = np.array(list(results.values()))
    data_cum = data.cumsum(axis=1)
    category_colors = plt.colormaps['RdYlGn'](
        np.linspace(0.15, 0.85, data.shape[1]))

    fig, ax = plt.subplots(figsize=(9.2, 5))
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, np.sum(data, axis=1).max())

    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        rects = ax.barh(labels, widths, left=starts, height=0.5,
                        label=colname, color=color)

        r, g, b, _ = color
        text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
        ax.bar_label(rects, label_type='center', color=text_color)
    ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 1),
              loc='center left', fontsize='small')

    return fig, ax


survey(results, category_names)
plt.title('STAT400 2021-fa')
plt.show()