# Supply Chain Optimization

This project aims to improve supply chain distribution routes by using optimization techniques to make logistics more efficient. The main objective is to reduce transportation costs, shorten delivery times, and improve supply chain management by finding the best routes for shipping goods. The project has two versions with different levels of optimization:

**Version 1 (PuLP)**: This version uses the PuLP library to solve linear programming problems. The goal is to minimize transportation costs by finding the best routes across a network of supply and demand points.

**Version 2 (Optimized)**: Building on Version 1, Version 2 uses more advanced techniques to handle more complex problems. It takes into account additional variables and constraints, offering better solutions for real-world challenges.

## Problem Definition: 

Supply chain optimization is essential for efficiently moving products from suppliers (such as factories or ports) to consumers (like retailers or warehouses). The challenge is selecting the best shipping routes while considering factors like transportation costs, travel distances, and time constraints.

In this project, the goal is to determine the most efficient routes for shipping goods. The aim is to reduce transportation costs and delivery times, all while ensuring that constraints like route availability and vehicle capacities are respected.

## Tools and Technologies

- **Python**: Used throughout the project for coding the optimization models, handling large datasets, and performing complex calculations.
- **PuLP**: Open-source Python library used to define and solve linear programming problems. Version 1 of the project uses PuLP to formulate the supply chain optimization problem.
- **Pandas**: Used for managing and manipulating supply chain data (e.g., distances, costs, inventory levels).
- **NumPy**: A library for performing numerical operations essential for solving optimization problems.
- **Matplotlib/Plotly** (Optional): Used for visualizing results such as optimized routes and supply chain networks (optional but helpful for interpretation).

## Methodology

The optimization process is based on mathematical programming, primarily linear programming (LP), to determine the best supply chain routes. In **Version 1**, PuLP is employed to create a model that minimizes transportation costs, subject to constraints such as route capacity and delivery times.

**Version 2** extends the model by incorporating more layers of complexity, such as varying shipping capacities and multi-criteria optimization. This version helps achieve a better balance between minimizing both costs and delivery times.

## Challenges

Supply chain route optimization comes with its own set of challenges:

- **Multiple Variables**: Optimization must account for a variety of factors like cost, time, and capacity.
- **Large Datasets**: Supply chain problems often involve large datasets, including distances, transportation costs, and inventory levels.
- **Complex Constraints**: Factors like delivery time windows, route capacity, and demand fulfillment add further complexity.

## Benefits

Optimization offers several key benefits to supply chain management:

- **Cost Reduction**: By finding the most efficient routes, transportation costs can be minimized.
- **Time Savings**: Shorter and more efficient routes lead to faster deliveries and overall supply chain efficiency.
- **Better Decision-Making**: Optimization models enable supply chain managers to make informed decisions based on comprehensive data analysis.

## Future Work

There are several ways to improve and expand this project:

- **Incorporating More Variables**: Future versions could include real-time data like weather, traffic, and shipping updates.
- **Scalability**: The algorithms can be optimized to handle larger datasets or more complex supply chain networks.
- **Advanced Techniques**: Integration of advanced algorithms (e.g., genetic algorithms, machine learning) to solve more complex supply chain problems efficiently.

## Conclusion

This project demonstrates how optimization techniques can significantly enhance supply chain logistics, making them more cost-effective and timely. Using Python and the PuLP library, the project solves a classic supply chain route optimization problem. **Version 2** improves the model by considering additional complex constraints, providing a more robust solution to real-world logistics challenges.

# OUTPUT OF THE TASK

**Version 1 (PuLP)** :

![Image](https://github.com/user-attachments/assets/2fcca81f-b2b8-40a9-baa4-bfadc9df5182)

**Version 2 (Optimized)** : 




![Image](https://github.com/user-attachments/assets/fc429340-0f66-418b-acb4-f82756ee8db4)

