# 🌍 Countries Info App (API + Data Analysis)

## 📌 Description

This project is a Python application that works with a public API to fetch and analyze information about countries.

The program allows the user to:

* Get a list of countries by region (continent)
* Display key information about each country
* Perform statistical analysis on population data
* Search for a specific country and display its details
* Save processed data into a JSON file

---

## 🚀 Features

### 🌎 1. Fetch Countries by Region

The user can input a region (e.g., Asia, Europe, Africa), and the program will:

* Retrieve countries from the API
* Display:

  * Country name
  * Capital
  * Population

---

### 📊 2. Data Analysis

The program calculates:

* Country with the **maximum population**
* Country with the **minimum population**
* **Average population** across selected countries

---

### 🔍 3. Country Search

The user can search for a specific country and get:

* Country name
* Capital
* Population
* Region (continent)

---

### 💾 4. JSON Storage

Processed data is saved into a `.json` file for later use.

---

## 🛠️ Technologies Used

* Python 3
* requests (API calls)
* pandas (data analysis)
* json (data storage)

---

## 🌐 API Used

* https://restcountries.com

---

## 📦 Installation

```bash
pip install -r requirements.txt.
```

---

## ▶️ Usage

Run the script:

```bash
python main.py
```

Then:

1. Enter a region (e.g., `Asia`)
2. View countries and statistics
3. Optionally search for a country

---

## ⚠️ Notes

* Some countries may not have a capital — handled safely in code
* Input should match valid region names
* Internet connection is required

---

## 📈 Example Output

```
The countries in continent: Asia
--------------------------------
Country: Kazakhstan
Capital: Astana
Population: 19000000
--------------------------------

Max population: China (1,400,000,000)
Min population: Maldives (500,000)
Average population: 150,000,000
```

---

## 🎯 Purpose

This project demonstrates:

* Working with REST APIs
* JSON parsing
* Data processing with pandas
* Writing clean and structured Python code

---

## 🏆 Author

Aldiyar — aspiring competitive programmer and developer 🚀
