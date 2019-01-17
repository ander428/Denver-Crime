from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

m = Basemap(projection='lcc', resolution='h',
                lat_0=39.3, lon_0=-104.991,
                width=0.9E6, height=0.6E6)

m.drawcoastlines()
m.drawcountries(linewidth=2)
m.drawstates(color='b')
m.drawcounties(color='darkred')

plt.title('Basemap of Colorado')
plt.show()
