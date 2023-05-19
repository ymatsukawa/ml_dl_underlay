import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

class Plot:
  @classmethod
  def simple(cls, x, y,
             xlegend='x legend', ylegend='ylegend', xlabel='x feature', ylabel='y feature'):
    plt.plot(x, y, 'o')
    plt.legend([xlegend, ylegend])
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

  @classmethod
  def linear(cls, x, y,
             xlabel='x feature', ylabel='y feature'):
    plt.grid(True)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.gca().get_xaxis().set_major_locator(ticker.MaxNLocator(integer=True))
    plt.plot(x, y)

    plt.tight_layout()
    plt.show()
