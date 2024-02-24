import matplotlib.pyplot as plt
import pandas as pand
import cartopy.crs as ccrs

# Read january data
jan_data = pand.read_csv(r"C:\Users\Tony\Documents\BigData\Data\January.csv", usecols=[1, 4, 8, 9, 10, 11])

# Extract columns for january
janBikeType = jan_data['rideable_type']
janStationName = jan_data['start_station_name']
janStartLat = jan_data['start_lat']
janStartLong = jan_data['start_lng']
janEndLat = jan_data['end_lat']
janEndLong = jan_data['end_lng']

# Create a Cartopy map
plt.figure(figsize=(10, 6))
ax = plt.axes(projection=ccrs.PlateCarree())

stride = 50
for i in range(0, len(janStartLat), stride):
    # Plot starting points
    if not janStationName[i]=="":
        plt.scatter(janStartLong[i], janStartLat[i], color='blue', transform=ccrs.PlateCarree())

plt.scatter(janStartLong[0], janStartLat[0], color='blue', label='Station', transform=ccrs.PlateCarree())
# Add map features
ax.coastlines()
ax.gridlines(draw_labels=True)

# Add legend
plt.legend()

# Show the plot
plt.title('Starting Stations')
plt.show()

# Read february data
feb_data = pand.read_csv(r"C:\Users\Tony\Documents\BigData\Data\February.csv", usecols=[1, 8, 9, 10, 11])

# Extract columns for february
febBikeType = feb_data['rideable_type']
febStartLat = feb_data['start_lat']
febStartLong = feb_data['start_lng']
febEndLat = feb_data['end_lat']
febEndLong = feb_data['end_lng']

# Create a Cartopy map
plt.figure(figsize=(10, 6))
ax = plt.axes(projection=ccrs.PlateCarree())

# Plot starting points
plt.scatter(febStartLong, febStartLat, color='blue', label='Start', transform=ccrs.PlateCarree())

# Add map features
ax.coastlines()
ax.gridlines(draw_labels=True)

# Add legend
plt.legend()

# Show the plot
plt.title('Starting Points for Febuary')
plt.show()

# Read march data
march_data = pand.read_csv(r"C:\Users\Tony\Documents\BigData\Data\March.csv", usecols=[1, 8, 9, 10, 11])

# Extract columns for march
marchBikeType = march_data['rideable_type']
marchStartLat = march_data['start_lat']
marchStartLong = march_data['start_lng']
marchEndLat = march_data['end_lat']
marchEndLong = march_data['end_lng']

# Create a Cartopy map
plt.figure(figsize=(10, 6))
ax = plt.axes(projection=ccrs.PlateCarree())

# Plot starting points
plt.scatter(marchStartLong, marchStartLat, color='blue', label='Start', transform=ccrs.PlateCarree())

# Add map features
ax.coastlines()
ax.gridlines(draw_labels=True)

# Add legend
plt.legend()

# Show the plot
plt.title('Starting Points for March')
plt.show()

# Read april data
april_data = pand.read_csv(r"C:\Users\Tony\Documents\BigData\Data\April.csv", usecols=[1, 8, 9, 10, 11])

# Extract columns for april
aprilBikeType = april_data['rideable_type']
aprilStartLat = april_data['start_lat']
aprilStartLong = april_data['start_lng']
aprilEndLat = april_data['end_lat']
aprilEndLong = april_data['end_lng']

# Create a Cartopy map
plt.figure(figsize=(10, 6))
ax = plt.axes(projection=ccrs.PlateCarree())

# Plot starting points
plt.scatter(aprilStartLong, aprilStartLat, color='blue', label='Start', transform=ccrs.PlateCarree())

# Add map features
ax.coastlines()
ax.gridlines(draw_labels=True)

# Add legend
plt.legend()

# Show the plot
plt.title('Starting Points for April')
plt.show()

# Read May data
may_data = pand.read_csv(r"C:\Users\Tony\Documents\BigData\Data\May.csv", usecols=[1, 8, 9, 10, 11])

# Extract columns for May
mayBikeType = may_data['rideable_type']
mayStartLat = may_data['start_lat']
mayStartLong = may_data['start_lng']
mayEndLat = may_data['end_lat']
mayEndLong = may_data['end_lng']

# Create a Cartopy map
plt.figure(figsize=(10, 6))
ax = plt.axes(projection=ccrs.PlateCarree())

# Plot starting points
plt.scatter(mayStartLong, mayStartLat, color='blue', label='Start', transform=ccrs.PlateCarree())

# Add map features
ax.coastlines()
ax.gridlines(draw_labels=True)

# Add legend
plt.legend()

# Show the plot
plt.title('Starting Points for May')
plt.show()

# Read june data
june_data = pand.read_csv(r"C:\Users\Tony\Documents\BigData\Data\June.csv", usecols=[1, 8, 9, 10, 11])

# Extract columns for June
juneBikeType = june_data['rideable_type']
juneStartLat = june_data['start_lat']
juneStartLong = june_data['start_lng']
juneEndLat = june_data['end_lat']
juneEndLong = june_data['end_lng']

# Create a Cartopy map
plt.figure(figsize=(10, 6))
ax = plt.axes(projection=ccrs.PlateCarree())

# Plot starting points
plt.scatter(juneStartLong, juneStartLat, color='blue', label='Start', transform=ccrs.PlateCarree())

# Plot ending points
plt.scatter(juneEndLong, juneEndLat, color='red', label='End', transform=ccrs.PlateCarree())

plt.plot([juneStartLong[0], juneEndLong[0]], [juneStartLat[0], juneEndLat[0]], color='orange', label='Electric Bike', transform=ccrs.PlateCarree())

plt.plot([juneStartLong[0], juneEndLong[0]], [juneStartLat[0], juneEndLat[0]], color='green', label='Classic Bike', transform=ccrs.PlateCarree())

# Add map features
ax.coastlines()
ax.gridlines(draw_labels=True)

# Add legend
plt.legend()

# Show the plot
plt.title('Starting Points for June')
plt.show()

# Read July data
july_data = pand.read_csv(r"C:\Users\Tony\Documents\BigData\Data\July.csv", usecols=[1, 8, 9, 10, 11])

# Extract columns for July
julyBikeType = july_data['rideable_type']
julyStartLat = july_data['start_lat']
julyStartLong = july_data['start_lng']
julyEndLat = july_data['end_lat']
julyEndLong = july_data['end_lng']

# Create a Cartopy map
plt.figure(figsize=(10, 6))
ax = plt.axes(projection=ccrs.PlateCarree())

# Plot starting points
plt.scatter(julyStartLong, julyStartLat, color='blue', label='Start', transform=ccrs.PlateCarree())

# Add map features
ax.coastlines()
ax.gridlines(draw_labels=True)

# Add legend
plt.legend()

# Show the plot
plt.title('Starting Points for July')
plt.show()

# Read august data
aug_data = pand.read_csv(r"C:\Users\Tony\Documents\BigData\Data\August.csv", usecols=[1, 8, 9, 10, 11])

# Extract columns for August
augBikeType = aug_data['rideable_type']
augStartLat = aug_data['start_lat']
augStartLong = aug_data['start_lng']
augEndLat = aug_data['end_lat']
augEndLong = aug_data['end_lng']

# Create a Cartopy map
plt.figure(figsize=(10, 6))
ax = plt.axes(projection=ccrs.PlateCarree())

# Plot starting points
plt.scatter(augStartLong, augStartLat, color='blue', label='Start', transform=ccrs.PlateCarree())

# Add map features
ax.coastlines()
ax.gridlines(draw_labels=True)

# Add legend
plt.legend()

# Show the plot
plt.title('Starting Points for August')
plt.show()

# Read september data
sep_data = pand.read_csv(r"C:\Users\Tony\Documents\BigData\Data\September.csv", usecols=[1, 8, 9, 10, 11])

# Extract columns for september
sepBikeType = sep_data['rideable_type']
sepStartLat = sep_data['start_lat']
sepStartLong = sep_data['start_lng']
sepEndLat = sep_data['end_lat']
sepEndLong = sep_data['end_lng']

# Create a Cartopy map
plt.figure(figsize=(10, 6))
ax = plt.axes(projection=ccrs.PlateCarree())

# Plot starting points
plt.scatter(sepStartLong, sepStartLat, color='blue', label='Start', transform=ccrs.PlateCarree())

# Add map features
ax.coastlines()
ax.gridlines(draw_labels=True)

# Add legend
plt.legend()

# Show the plot
plt.title('Starting Points for September')
plt.show()

# Read october data
oct_data = pand.read_csv(r"C:\Users\Tony\Documents\BigData\Data\October.csv", usecols=[1, 8, 9, 10, 11])

# Extract columns for october
octBikeType = oct_data['rideable_type']
octStartLat = oct_data['start_lat']
octStartLong = oct_data['start_lng']
octEndLat = oct_data['end_lat']
octEndLong = oct_data['end_lng']

# Create a Cartopy map
plt.figure(figsize=(10, 6))
ax = plt.axes(projection=ccrs.PlateCarree())

# Plot starting points
plt.scatter(octStartLong, octStartLat, color='blue', label='Start', transform=ccrs.PlateCarree())

# Add map features
ax.coastlines()
ax.gridlines(draw_labels=True)

# Add legend
plt.legend()

# Show the plot
plt.title('Starting Points for October')
plt.show()

# Read november date
nov_data = pand.read_csv(r"C:\Users\Tony\Documents\BigData\Data\November.csv", usecols=[1, 8, 9, 10, 11])

# Extract columns for November
novBikeType = nov_data['rideable_type']
novStartLat = nov_data['start_lat']
novStartLong = nov_data['start_lng']
novEndLat = nov_data['end_lat']
novEndLong = nov_data['end_lng']

# Create a Cartopy map
plt.figure(figsize=(10, 6))
ax = plt.axes(projection=ccrs.PlateCarree())

# Plot starting points
plt.scatter(novStartLong, novStartLat, color='blue', label='Start', transform=ccrs.PlateCarree())

# Add map features
ax.coastlines()
ax.gridlines(draw_labels=True)

# Add legend
plt.legend()

# Show the plot
plt.title('Starting Points for November')
plt.show()

# Read December data
dec_data = pand.read_csv(r"C:\Users\Tony\Documents\BigData\Data\December.csv", usecols=[1, 8, 9, 10, 11])

# Extract columns for december
decBikeType = dec_data['rideable_type']
decStartLat = dec_data['start_lat']
decStartLong = dec_data['start_lng']
decEndLat = dec_data['end_lat']
decEndLong = dec_data['end_lng']

# Create a Cartopy map
plt.figure(figsize=(10, 6))
ax = plt.axes(projection=ccrs.PlateCarree())

# Plot starting points
plt.scatter(decStartLong, decStartLat, color='blue', label='Start', transform=ccrs.PlateCarree())

# Add map features
ax.coastlines()
ax.gridlines(draw_labels=True)

# Add legend
plt.legend()

# Show the plot
plt.title('Starting Points for December')
plt.show()

print(len(janStartLat))
print(len(febStartLat))
print(len(marchStartLat))
print(len(aprilStartLat))
print(len(mayStartLat))
print(len(juneStartLat))
print(len(julyStartLat))
print(len(augStartLat))
print(len(sepStartLat))
print(len(octStartLat))
print(len(novStartLat))
print(len(decStartLat))