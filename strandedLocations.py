import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

# Read january data
jan_data = pd.read_csv(r"C:\Users\Tony\Documents\BigData\Data\September.csv", usecols=[1, 4, 8, 9, 10, 11])
feb_data = pd.read_csv(r"C:\Users\Tony\Documents\BigData\Data\October.csv", usecols=[1, 4, 8, 9, 10, 11])
dec_data = pd.read_csv(r"C:\Users\Tony\Documents\BigData\Data\November.csv", usecols=[1, 4, 8, 9, 10, 11])

# Extract columns for january
janBikeType = jan_data['rideable_type']
janStationName = jan_data['start_station_name']
janStartLat = jan_data['start_lat']
janStartLong = jan_data['start_lng']
janEndLat = jan_data['end_lat']
janEndLong = jan_data['end_lng']

febBikeType = feb_data['rideable_type']
febStationName = feb_data['start_station_name']
febStartLat = feb_data['start_lat']
febStartLong = feb_data['start_lng']
febEndLat = feb_data['end_lat']
febEndLong = feb_data['end_lng']

decBikeType = dec_data['rideable_type']
decStationName = dec_data['start_station_name']
decStartLat = dec_data['start_lat']
decStartLong = dec_data['start_lng']
decEndLat = dec_data['end_lat']
decEndLong = dec_data['end_lng']

# Create a Cartopy map
plt.figure(figsize=(10, 6))
ax = plt.axes(projection=ccrs.PlateCarree())

stride = 50
for i in range(0, len(janStartLat), stride):
    # Plot starting points
    #if len(janStationName[i])==0:
    if pd.isnull(janStationName[i]):
        plt.scatter(janStartLong[i], janStartLat[i], color='red', transform=ccrs.PlateCarree())

stride = 50
for i in range(0, len(febStartLat), stride):
    # Plot starting points
    #if len(janStationName[i])==0:
    if pd.isnull(febStationName[i]):
        plt.scatter(febStartLong[i], febStartLat[i], color='red', transform=ccrs.PlateCarree())

stride = 50
for i in range(0, len(decStartLat), stride):
    # Plot starting points
    #if len(janStationName[i])==0:
    if pd.isnull(decStationName[i]):
        plt.scatter(decStartLong[i], decStartLat[i], color='red', transform=ccrs.PlateCarree())
    

plt.scatter(janStartLong[0], janStartLat[0], color='red', label='Stranded', transform=ccrs.PlateCarree())

# Add map features
ax.coastlines()
ax.gridlines(draw_labels=True)

# Add legend
plt.legend()

# Show the plot
plt.title('Stranded Bikes in Fall')
plt.show()