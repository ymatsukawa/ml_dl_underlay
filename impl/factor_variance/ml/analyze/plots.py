import matplotlib.pyplot as plt

class Plot:
  @classmethod
  def simple(cls, x, y,
             xlegend='x legend', ylegend='ylegend', xlabel='x feature', ylabel='y feature'):
    plt.plot(x, y, 'o')
    plt.legend([xlegend, ylegend])
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
