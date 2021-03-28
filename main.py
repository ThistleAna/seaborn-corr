# Making correlation of the table using seaborn, visualise using graph

import matplotlib.pyplot as plt
import seaborn as sb

# Load the database
database = sb.load_dataset('tips')
print(database)

graph= sb.FacetGrid(database,col='sex',row='smoker')
graph.map(plt.scatter,'total_bill','tip')
# Show everything
plt.show()


