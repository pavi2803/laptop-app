# Laptop Recommendation App

This Laptop Recommendation App is designed to help users find the best laptops based on their specific requirements such as company, type, RAM, and price. The app filters laptops from a dataset and displays the results, including a comparison of the highest and lowest prices, screen resolutions, memory, CPU, and other relevant details.

## Features

- **User Input:** Users can input their preferences for the laptop's company, type, RAM, and price in their preferred currency (Rupees, Dollars, or Euros).
- **Filtered Results:** The app processes the input and filters the laptops that match the user's criteria.
- **Price Comparison:** The app provides a comparison of the maximum and minimum prices of the laptops that meet the criteria, along with other details such as company, product name, screen resolution, memory, and CPU.
- **Responsive Output:** The results are displayed in a user-friendly HTML table, and if no laptops match the criteria, a "No Results" page is shown.

## Installation

1. **Clone the repository:**
    
    ```bash
    bashCopy code
    git clone https://github.com/yourusername/laptop-recommendation-app.git
    cd laptop-recommendation-app
    
    ```
    
2. **Install the required dependencies:**
    
    ```bash
    bashCopy code
    pip install -r requirements.txt
    
    ```
    
3. **Prepare the dataset:**
    
    Ensure that you have the `laptops.csv` file in the root directory of the project. This file should contain the relevant data with columns for `Company`, `TypeName`, `Ram`, `ScreenResolution`, `Memory`, `Cpu`, and `Price` in various currencies.
    
4. **Run the app:**
    
    ```bash
    bashCopy code
    python app.py
    
    ```
    
5. **Access the app:**
    
    Open your web browser and navigate to `http://localhost:5000`.
    

## Usage

1. On the homepage, you will be prompted to enter your laptop preferences, including the company, type, RAM, and preferred currency.
2. Submit the form to get a list of laptops that match your criteria.
3. The results page will display the laptops along with the highest and lowest price comparisons, and other details like screen resolution, memory, and CPU.
4. If no laptops match your criteria, a "No Results" page will be shown.

## Code Overview

- **`app.route("/input", methods=["GET", "POST"])`:** Handles the user input and processes the request based on the selected criteria.
- **`fetch_details_cpu(company, typename, ram, price)`:** Filters the dataset based on the user's input and returns the relevant data.
- **Rendering:** The app uses Flask's `render_template` to display the results in an HTML table or show a "No Results" page if no matches are found.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

This README provides a clear and concise overview of the app, its features, installation steps, and usage instructions.
