from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

class DenverMap:
    def __init__(self):
        self.map = Basemap(projection='lcc', resolution='h',
                    lat_0=39.75, lon_0=-104.791,
                    width=5E4, height=3.5E4)
        #self.data = readData("./MapData.csv")

    def show(self):
        self.map.readshapefile('./Data/Roads/roads', 'Streets',
            drawbounds = True, color='grey')
        self.map.readshapefile('./Data/Neighborhoods/statistical_neighborhoods',
            'Neighborhoods',drawbounds = True, color='red')
        plt.show()

    def plot(self, x, y):
        self.map.plot(x, y, marker="D",color='m')

    def getMap(self):
        return self.map

# dm = DenverMap()
# dm.show()
