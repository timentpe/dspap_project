# DSPAP — Data Science Principles and Applications
### GPS Data Analysis of Car Trips in Lyon
#### Authors : Célestin GABORIAU, Timothée POULY, Assia RACHID, Quentin THIBAULT

## 📌 Project Description
This project focuses on analyzing GPS data from car trips in the Lyon metropolitan area.  
The main objectives are to:

- Explore and clean raw GPS datasets  
- Produce various maps and geospatial visualizations  
- Identify mobility patterns and trends
  

This repository contains the code, notebooks, and tools required to reproduce the analysis.

---

## 📂 Repository Structure

dspap_project/

│

├── data/ # (Empty) Data files must be added manually

├── infos/ # Information concerning the datas

├── notebooks/ # Jupyter notebooks for exploration and analysis

├── src/ # Python code (preprocessing, analysis, visualization)

├── Output/ # Generated maps, figures, and results

├── config/ # Python dependencies

├── .gitignore/ # To not overload the servor

└── README.md



---

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/timentpe/dspap_project.git
cd dspap_project
```

## 📥 Downloading the Data

The dataset is not included in the repository.
Please download the GPS data using the following link: https://people.licit-lyon.eu/furno/courses/2025/class_06/GPS/
Put the files in data folder. 

To download the IRIS data of Lyon, use the following link : https://data.grandlyon.com/portail/fr/jeux-de-donnees/contours-iris-metropole-lyon/telechargements and download the SHP folder. 
Then, put these IRIS data into a folder named 'Lyon IRIS' into the data folder. 


## 🛠️ Installation

```bash
conda env create -f environment.yml -n DSPAP_project
conda activate DSPAP_project
pip install -r requirements.txt
```

## 📊 Usage

Launch the notebook.


## 🗺️ Outputs

Generated maps, charts, and intermediate results are stored in the notebook or the Output/ directory.
These include:

- Heatmaps
- Route visualizations
- Spatial analysis figures


## 🤝 Contributing

Contributions, issues, and feature requests are welcome.
Feel free to open a pull request or report a bug.

#### Teacher : Angelo FURNO

