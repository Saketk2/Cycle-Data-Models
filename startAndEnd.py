import matplotlib.pyplot as plt
import pandas as pand
import cartopy.crs as ccrs

# Read january data
jan_data = pand.read_csv(r"C:\Users\Tony\Documents\BigData\Data\January.csv", usecols=[1, 8, 9, 10, 11])

# Extract columns for january
janBikeType = jan_data['rideable_type']
janStartLat = jan_data['start_lat']
janStartLong = jan_data['start_lng']
janEndLat = jan_data['end_lat']
janEndLong = jan_data['end_lng']

# Create a Cartopy map
plt.figure(figsize=(10, 6))
ax = plt.axes(projection=ccrs.PlateCarree())

stride = 2000
for i in range(0, len(janStartLat), stride):
    if janBikeType[i]=="electric_bike":
        plt.plot([janStartLong[i], janEndLong[i]], [janStartLat[i], janEndLat[i]], color='orange', transform=ccrs.PlateCarree())

    if janBikeType[i]=="classic_bike":
        plt.plot([janStartLong[i], janEndLong[i]], [janStartLat[i], janEndLat[i]], color='green', transform=ccrs.PlateCarree())

    if janBikeType[i]=="docked_bike":
        plt.plot([janStartLong[i], janEndLong[i]], [janStartLat[i], janEndLat[i]], color='magenta', transform=ccrs.PlateCarree())

# Plot starting points
plt.scatter(janStartLong, janStartLat, color='blue', label='Start', transform=ccrs.PlateCarree())

# Plot ending points
plt.scatter(janEndLong, janEndLat, color='red', label='End', transform=ccrs.PlateCarree())

plt.plot([janStartLong[0], janEndLong[0]], [janStartLat[0], janEndLat[0]], color='orange', label='Electric Bike', transform=ccrs.PlateCarree())

plt.plot([janStartLong[0], janEndLong[0]], [janStartLat[0], janEndLat[0]], color='green', label='Classic Bike', transform=ccrs.PlateCarree())

# Add map features
ax.coastlines()
ax.gridlines(draw_labels=True)

# Add legend
plt.legend()

# Show the plot
plt.title('Starting and Ending Points for January')
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

for i in range(0, len(febStartLat), stride):
    if febBikeType[i]=="electric_bike":
        plt.plot([febStartLong[i], febEndLong[i]], [febStartLat[i], febEndLat[i]], color='orange', transform=ccrs.PlateCarree())

    if febBikeType[i]=="classic_bike":
        plt.plot([febStartLong[i], febEndLong[i]], [febStartLat[i], febEndLat[i]], color='green', transform=ccrs.PlateCarree())

    if febBikeType[i]=="docked_bike":
        plt.plot([febStartLong[i], febEndLong[i]], [febStartLat[i], febEndLat[i]], color='yellow', transform=ccrs.PlateCarree())

# Plot starting points
plt.scatter(febStartLong, febStartLat, color='blue', label='Start', transform=ccrs.PlateCarree())

# Plot ending points
plt.scatter(febEndLong, febEndLat, color='red', label='End', transform=ccrs.PlateCarree())

plt.plot([febStartLong[0], febEndLong[0]], [febStartLat[0], febEndLat[0]], color='orange', label='Electric Bike', transform=ccrs.PlateCarree())

plt.plot([febStartLong[0], febEndLong[0]], [febStartLat[0], febEndLat[0]], color='green', label='Classic Bike', transform=ccrs.PlateCarree())

# Add map features
ax.coastlines()
ax.gridlines(draw_labels=True)

# Add legend
plt.legend()

# Show the plot
plt.title('Starting and Ending Points for Febuary')
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

for i in range(0, len(marchStartLat), stride):
    if marchBikeType[i]=="electric_bike":
        plt.plot([marchStartLong[i], marchEndLong[i]], [marchStartLat[i], marchEndLat[i]], color='orange', transform=ccrs.PlateCarree())

    if marchBikeType[i]=="classic_bike":
        plt.plot([marchStartLong[i], marchEndLong[i]], [marchStartLat[i], marchEndLat[i]], color='green', transform=ccrs.PlateCarree())

    if marchBikeType[i]=="docked_bike":
        plt.plot([marchStartLong[i], marchEndLong[i]], [marchStartLat[i], marchEndLat[i]], color='yellow', transform=ccrs.PlateCarree())

# Plot starting points
plt.scatter(marchStartLong, marchStartLat, color='blue', label='Start', transform=ccrs.PlateCarree())

# Plot ending points
plt.scatter(marchEndLong, marchEndLat, color='red', label='End', transform=ccrs.PlateCarree())

plt.plot([marchStartLong[0], marchEndLong[0]], [marchStartLat[0], marchEndLat[0]], color='orange', label='Electric Bike', transform=ccrs.PlateCarree())

plt.plot([marchStartLong[0], marchEndLong[0]], [marchStartLat[0], marchEndLat[0]], color='green', label='Classic Bike', transform=ccrs.PlateCarree())

# Add map features
ax.coastlines()
ax.gridlines(draw_labels=True)

# Add legend
plt.legend()

# Show the plot
plt.title('Starting and Ending Points for March')
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

for i in range(0, len(aprilStartLat), stride):
    if aprilBikeType[i]=="electric_bike":
        plt.plot([aprilStartLong[i], aprilEndLong[i]], [aprilStartLat[i], aprilEndLat[i]], color='orange', transform=ccrs.PlateCarree())

    if aprilBikeType[i]=="classic_bike":
        plt.plot([aprilStartLong[i], aprilEndLong[i]], [aprilStartLat[i], aprilEndLat[i]], color='green', transform=ccrs.PlateCarree())

    if aprilBikeType[i]=="docked_bike":
        plt.plot([aprilStartLong[i], aprilEndLong[i]], [aprilStartLat[i], aprilEndLat[i]], color='yellow', transform=ccrs.PlateCarree())

# Plot starting points
plt.scatter(aprilStartLong, aprilStartLat, color='blue', label='Start', transform=ccrs.PlateCarree())

# Plot ending points
plt.scatter(aprilEndLong, aprilEndLat, color='red', label='End', transform=ccrs.PlateCarree())

plt.plot([aprilStartLong[0], aprilEndLong[0]], [aprilStartLat[0], aprilEndLat[0]], color='orange', label='Electric Bike', transform=ccrs.PlateCarree())

plt.plot([aprilStartLong[0], aprilEndLong[0]], [aprilStartLat[0], aprilEndLat[0]], color='green', label='Classic Bike', transform=ccrs.PlateCarree())

# Add map features
ax.coastlines()
ax.gridlines(draw_labels=True)

# Add legend
plt.legend()

# Show the plot
plt.title('Starting and Ending Points for April')
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

for i in range(0, len(mayStartLat), stride):
    if mayBikeType[i]=="electric_bike":
        plt.plot([mayStartLong[i], mayEndLong[i]], [mayStartLat[i], mayEndLat[i]], color='orange', transform=ccrs.PlateCarree())

    if mayBikeType[i]=="classic_bike":
        plt.plot([mayStartLong[i], mayEndLong[i]], [mayStartLat[i], mayEndLat[i]], color='green', transform=ccrs.PlateCarree())

    if mayBikeType[i]=="docked_bike":
        plt.plot([mayStartLong[i], mayEndLong[i]], [mayStartLat[i], mayEndLat[i]], color='yellow', transform=ccrs.PlateCarree())

# Plot starting points
plt.scatter(mayStartLong, mayStartLat, color='blue', label='Start', transform=ccrs.PlateCarree())

# Plot ending points
plt.scatter(mayEndLong, mayEndLat, color='red', label='End', transform=ccrs.PlateCarree())

plt.plot([mayStartLong[0], mayEndLong[0]], [mayStartLat[0], mayEndLat[0]], color='orange', label='Electric Bike', transform=ccrs.PlateCarree())

plt.plot([mayStartLong[0], mayEndLong[0]], [mayStartLat[0], mayEndLat[0]], color='green', label='Classic Bike', transform=ccrs.PlateCarree())

# Add map features
ax.coastlines()
ax.gridlines(draw_labels=True)

# Add legend
plt.legend()

# Show the plot
plt.title('Starting and Ending Points for May')
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

for i in range(0, len(juneStartLat), stride):
    if juneBikeType[i]=="electric_bike":
        plt.plot([juneStartLong[i], juneEndLong[i]], [juneStartLat[i], juneEndLat[i]], color='orange', transform=ccrs.PlateCarree())

    if juneBikeType[i]=="classic_bike":
        plt.plot([juneStartLong[i], juneEndLong[i]], [juneStartLat[i], juneEndLat[i]], color='green', transform=ccrs.PlateCarree())

    if juneBikeType[i]=="docked_bike":
        plt.plot([juneStartLong[i], juneEndLong[i]], [juneStartLat[i], juneEndLat[i]], color='yellow', transform=ccrs.PlateCarree())

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
plt.title('Starting and Ending Points for June')
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

for i in range(0, len(julyStartLat), stride):
    if julyBikeType[i]=="electric_bike":
        plt.plot([julyStartLong[i], julyEndLong[i]], [julyStartLat[i], julyEndLat[i]], color='orange', transform=ccrs.PlateCarree())

    if julyBikeType[i]=="classic_bike":
        plt.plot([julyStartLong[i], julyEndLong[i]], [julyStartLat[i], julyEndLat[i]], color='green', transform=ccrs.PlateCarree())

    if julyBikeType[i]=="docked_bike":
        plt.plot([julyStartLong[i], julyEndLong[i]], [julyStartLat[i], julyEndLat[i]], color='yellow', transform=ccrs.PlateCarree())

# Plot starting points
plt.scatter(julyStartLong, julyStartLat, color='blue', label='Start', transform=ccrs.PlateCarree())

# Plot ending points
plt.scatter(julyEndLong, julyEndLat, color='red', label='End', transform=ccrs.PlateCarree())

plt.plot([julyStartLong[0], julyEndLong[0]], [julyStartLat[0], julyEndLat[0]], color='orange', label='Electric Bike', transform=ccrs.PlateCarree())

plt.plot([julyStartLong[0], julyEndLong[0]], [julyStartLat[0], julyEndLat[0]], color='green', label='Classic Bike', transform=ccrs.PlateCarree())

# Add map features
ax.coastlines()
ax.gridlines(draw_labels=True)

# Add legend
plt.legend()

# Show the plot
plt.title('Starting and Ending Points for July')
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

for i in range(0, len(augStartLat), stride):
    if augBikeType[i]=="electric_bike":
        plt.plot([augStartLong[i], augEndLong[i]], [augStartLat[i], augEndLat[i]], color='orange', transform=ccrs.PlateCarree())

    if augBikeType[i]=="classic_bike":
        plt.plot([augStartLong[i], augEndLong[i]], [augStartLat[i], augEndLat[i]], color='green', transform=ccrs.PlateCarree())

    if augBikeType[i]=="docked_bike":
        plt.plot([augStartLong[i], augEndLong[i]], [augStartLat[i], augEndLat[i]], color='yellow', transform=ccrs.PlateCarree())

# Plot starting points
plt.scatter(augStartLong, augStartLat, color='blue', label='Start', transform=ccrs.PlateCarree())

# Plot ending points
plt.scatter(augEndLong, augEndLat, color='red', label='End', transform=ccrs.PlateCarree())

plt.plot([augStartLong[0], augEndLong[0]], [augStartLat[0], augEndLat[0]], color='orange', label='Electric Bike', transform=ccrs.PlateCarree())

plt.plot([augStartLong[0], augEndLong[0]], [augStartLat[0], augEndLat[0]], color='green', label='Classic Bike', transform=ccrs.PlateCarree())

# Add map features
ax.coastlines()
ax.gridlines(draw_labels=True)

# Add legend
plt.legend()

# Show the plot
plt.title('Starting and Ending Points for August')
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

for i in range(0, len(sepStartLat), stride):
    if sepBikeType[i]=="electric_bike":
        plt.plot([sepStartLong[i], sepEndLong[i]], [sepStartLat[i], sepEndLat[i]], color='orange', transform=ccrs.PlateCarree())

    if sepBikeType[i]=="classic_bike":
        plt.plot([sepStartLong[i], sepEndLong[i]], [sepStartLat[i], sepEndLat[i]], color='green', transform=ccrs.PlateCarree())

    if sepBikeType[i]=="docked_bike":
        plt.plot([sepStartLong[i], sepEndLong[i]], [sepStartLat[i], sepEndLat[i]], color='yellow', transform=ccrs.PlateCarree())

# Plot starting points
plt.scatter(sepStartLong, sepStartLat, color='blue', label='Start', transform=ccrs.PlateCarree())

# Plot ending points
plt.scatter(sepEndLong, sepEndLat, color='red', label='End', transform=ccrs.PlateCarree())

plt.plot([sepStartLong[0], sepEndLong[0]], [sepStartLat[0], sepEndLat[0]], color='orange', label='Electric Bike', transform=ccrs.PlateCarree())

plt.plot([sepStartLong[0], sepEndLong[0]], [sepStartLat[0], sepEndLat[0]], color='green', label='Classic Bike', transform=ccrs.PlateCarree())

# Add map features
ax.coastlines()
ax.gridlines(draw_labels=True)

# Add legend
plt.legend()

# Show the plot
plt.title('Starting and Ending Points for September')
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

for i in range(0, len(octStartLat), stride):
    if octBikeType[i]=="electric_bike":
        plt.plot([octStartLong[i], octEndLong[i]], [octStartLat[i], octEndLat[i]], color='orange', transform=ccrs.PlateCarree())

    if octBikeType[i]=="classic_bike":
        plt.plot([octStartLong[i], octEndLong[i]], [octStartLat[i], octEndLat[i]], color='green', transform=ccrs.PlateCarree())

    if octBikeType[i]=="docked_bike":
        plt.plot([octStartLong[i], octEndLong[i]], [octStartLat[i], octEndLat[i]], color='yellow', transform=ccrs.PlateCarree())

# Plot starting points
plt.scatter(octStartLong, octStartLat, color='blue', label='Start', transform=ccrs.PlateCarree())

# Plot ending points
plt.scatter(octEndLong, octEndLat, color='red', label='End', transform=ccrs.PlateCarree())

plt.plot([octStartLong[0], octEndLong[0]], [octStartLat[0], octEndLat[0]], color='orange', label='Electric Bike', transform=ccrs.PlateCarree())

plt.plot([octStartLong[0], octEndLong[0]], [octStartLat[0], octEndLat[0]], color='green', label='Classic Bike', transform=ccrs.PlateCarree())

# Add map features
ax.coastlines()
ax.gridlines(draw_labels=True)

# Add legend
plt.legend()

# Show the plot
plt.title('Starting and Ending Points for October')
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

for i in range(0, len(novStartLat), stride):
    if novBikeType[i]=="electric_bike":
        plt.plot([novStartLong[i], novEndLong[i]], [novStartLat[i], novEndLat[i]], color='orange', transform=ccrs.PlateCarree())

    if novBikeType[i]=="classic_bike":
        plt.plot([novStartLong[i], novEndLong[i]], [novStartLat[i], novEndLat[i]], color='green', transform=ccrs.PlateCarree())

    if novBikeType[i]=="docked_bike":
        plt.plot([novStartLong[i], novEndLong[i]], [novStartLat[i], novEndLat[i]], color='yellow', transform=ccrs.PlateCarree())

# Plot starting points
plt.scatter(novStartLong, novStartLat, color='blue', label='Start', transform=ccrs.PlateCarree())

# Plot ending points
plt.scatter(novEndLong, novEndLat, color='red', label='End', transform=ccrs.PlateCarree())

plt.plot([novStartLong[0], novEndLong[0]], [novStartLat[0], novEndLat[0]], color='orange', label='Electric Bike', transform=ccrs.PlateCarree())

plt.plot([novStartLong[0], novEndLong[0]], [novStartLat[0], novEndLat[0]], color='green', label='Classic Bike', transform=ccrs.PlateCarree())

# Add map features
ax.coastlines()
ax.gridlines(draw_labels=True)

# Add legend
plt.legend()

# Show the plot
plt.title('Starting and Ending Points for November')
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

for i in range(0, len(decStartLat), stride):
    if decBikeType[i]=="electric_bike":
        plt.plot([decStartLong[i], decEndLong[i]], [decStartLat[i], decEndLat[i]], color='orange', transform=ccrs.PlateCarree())

    if decBikeType[i]=="classic_bike":
        plt.plot([decStartLong[i], decEndLong[i]], [decStartLat[i], decEndLat[i]], color='green', transform=ccrs.PlateCarree())

    if decBikeType[i]=="docked_bike":
        plt.plot([decStartLong[i], decEndLong[i]], [decStartLat[i], decEndLat[i]], color='yellow', transform=ccrs.PlateCarree())

# Plot starting points
plt.scatter(decStartLong, decStartLat, color='blue', label='Start', transform=ccrs.PlateCarree())

# Plot ending points
plt.scatter(decEndLong, decEndLat, color='red', label='End', transform=ccrs.PlateCarree())

plt.plot([decStartLong[0], decEndLong[0]], [decStartLat[0], decEndLat[0]], color='orange', label='Electric Bike', transform=ccrs.PlateCarree())

plt.plot([decStartLong[0], decEndLong[0]], [decStartLat[0], decEndLat[0]], color='green', label='Classic Bike', transform=ccrs.PlateCarree())

# Add map features
ax.coastlines()
ax.gridlines(draw_labels=True)

# Add legend
plt.legend()

# Show the plot
plt.title('Starting and Ending Points for December')
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