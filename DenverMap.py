from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt


class DenverMap(Basemap):
    def __init__(self):
        self.map = Basemap(projection='lcc', resolution='h',
                    lat_0=39.3, lon_0=-104.991,
                    width=0.9E6, height=0.6E6)

    def show(self):
        self.map.readshapefile('./Data/roads', 'Streets',drawbounds = True, color='grey')
        plt.show()

        # new line of code
dm = DenverMap()
dm.show()
