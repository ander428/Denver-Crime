from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt


class DenverMap(Basemap):
    def __init__(self):
        self.map = Basemap(projection='lcc', resolution='h',
                    lat_0=39.75, lon_0=-104.791,
                    width=5E4, height=3.5E4)

    def show(self):
        self.map.readshapefile('./Data/Roads/roads', 'Streets',
            drawbounds = True, color='grey')
        self.map.readshapefile('./Data/Neighborhoods/statistical_neighborhoods',
            'Neighborhoods',drawbounds = True, color='red')
        plt.show()

dm = DenverMap()
dm.show()
