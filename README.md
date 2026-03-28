# PCA Car Dataset Analysis

## Project Description

This project performs an advanced Principal Component Analysis (PCA) on a car dataset using Python.

It includes both theoretical and practical aspects of PCA, such as eigenvalue computation, quality of representation (cos²), contributions, and graphical visualizations.

## Technologies Used

* Python
* pandas
* numpy
* matplotlib
* scikit-learn

## Dataset

The dataset is stored in an Excel file named `voiture.xlsx`.

Rows represent individuals (cars), and columns represent quantitative variables.

## Features

### Data Preprocessing

* Data loading using pandas
* Standardization using StandardScaler

### PCA Analysis

* PCA using sklearn
* Eigenvalues and explained variance
* Scree plot
* Cumulative explained variance

### Individuals Analysis

* Projection of individuals on principal components
* Calculation of distances to the center
* Cos² (quality of representation)
* Contributions of individuals to principal axes

### Variables Analysis

* Principal components (loadings)
* Correlation between variables and components
* Correlation circle visualization

### Additional Individuals

* Projection of supplementary individuals into PCA space

## How to Run

Install dependencies:

```bash id="z81xpw"
pip install pandas numpy matplotlib scikit-learn openpyxl
```

Run the script:

```bash id="q7k2lm"
python your_script_name.py
```

## Results

The project provides:

* Identification of the most important variables
* Visualization of individuals and variables in reduced space
* Interpretation tools such as cos² and contributions

## Author

Rawen ZGARNI

## Notes

This project demonstrates a full implementation of PCA, including both mathematical foundations and practical applications.
