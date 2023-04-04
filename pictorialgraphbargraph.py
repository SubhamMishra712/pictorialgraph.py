import matplotlib.pyplot as plt

# Input the waste data for a particular country
waste_data = []

# Get input from the user for the current year's waste data
for i in range(12):
    waste_data.append(float(input(f"Enter waste for month {i+1}: ")))

# Define the x-axis labels for the waste data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Create a pictorial graph of the waste data
plt.pie(waste_data, labels=months, autopct='%1.1f%%')

# Set the title
plt.title('Waste by Month in Country X')

# Show the graph
plt.show()

# Input the past waste data for a particular country
past_waste_data = []
past_years = []

# Get input from the user for past years' waste data
num_years = int(input("Enter number of years: "))
for i in range(num_years):
    year = int(input(f"Enter year {i+1}: "))
    past_years.append(year)
    waste = float(input(f"Enter waste for year {year}: "))
    past_waste_data.append(waste)

# Create a bar graph of the past waste data
plt.bar(past_years, past_waste_data)

# Set the title and axis labels
plt.title('Total Waste by Year in Country X')
plt.xlabel('Year')
plt.ylabel('Waste (tons)')

# Show the graph
plt.show()
