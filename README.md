# Champicker
A simple ML model trained to classify which team is more likely to win a match based on what champions are selected in League of Legends.

## Data
The whole dataset has been created with the usage of Riot Games API. The first version consists of ~10.000 records.
 
Sample records:

| Red_Win      | Blue_Win | Red_Champions     | Blue_Champions|
| :---        | :----       | :---          | :--- |
| False      | True       | [875, 120, 127, 235, 147]   | [24, 56, 161, 22, 432] |
| True   | False        | [58, 35, 518, 147, 235]     | [122, 245, 777, 429, 117] |

## Model
There have been many classification models built to check which one will be the most suitable one for this problem. After the whole analysis **Random Forest Classifier** got the best results with **54.3%** accuracy and **58.2%** F1 score.

## Access
The model's prediction can be accessed using the HTTP POST method. It has been built using FastAPI and can be run in Docker environment.

## Deployment
For the sake of practice the API has been deployed on AWS EC2 instance and shut down to prevent any billing.