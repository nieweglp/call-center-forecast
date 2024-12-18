
![image](https://github.com/user-attachments/assets/910d7539-fbbd-48e8-adc8-687e5aca9fc2)

# Falck Digital Technology - Call Center Roadside Assistance Services

## Time-Series Forecasting

**Data Time Period:** March 2022 to November 2023
**Estimated Time to Complete:** 4-8 hours

### Goal

Using Python, develop a predictive machine learning model to forecast daily call volumes for Falck Digital Technology’s Roadside Assistance Services in Denmark for December 2023. **_The goal is to accurately predict the total number of calls for each day in December 2023_**, leveraging historical data and any relevant external factors. Once completed, submit your predictions in the specified format to pedro.rodrigues@falck.com.

### Instructions

1. **Download the Dataset:**
   - **Source:** [Download the dataset here in /dataset](/dataset)
   - **Description:** The dataset contains anonymized and synthesized data closely resembling real-world data from Falck’s Denmark roadside assistance call center services. It includes call records from March 2022 to November 2023. Note: The data is not aggregated. Each row in this raw data represents a unique call in the call center system.

2. **Data Engineering and Feature Enrichment:**
   - **Prepare Dataset:** Prepare your dataset needed to train a machine learning algorithm. Don’t forget to aggregate to the Date level.

3. **Model Training and Prediction:**
   - **Model Training:** Train your best machine learning model to generate predictions for the 31 days of December 2023.
   - **Output Format:** The predictions should be saved in a `.json` file with the following format as a list with 31 numeric predictions:

     ```json
     {
       "predictions": [
     <pred_dec1>,
     <pred_dec2>,
     ...,
     <pred_dec31>
     ]
     }
     ```
   - **Submission:** Send the `.json` file to pedro.rodrigues@falck.com with the subject “[pytech_contest]”.

### Evaluation Measure

- **Metric:** We will use MAPE (Mean Absolute Percentage Error) to evaluate the accuracy of your predictions over the 31 days of December 2023. This will be used to rank all participants.

### Tips

While the core task is to generate accurate predictions, here are some optional tips that can help you improve your model's performance:

1. **Cleaning:** Consider addressing missing values, outliers, and inconsistencies in the dataset. Adding relevant features might also enhance prediction accuracy.
2. **Aggregation:** Aggregate the data to the `EmitDate` level to facilitate more effective time-series analysis.
3. **Feature Enrichment:** Enhance your analysis by incorporating external data sources or fields that could influence roadside assistance call volumes, such as weather conditions, public holidays, or local events. Be creative in identifying and integrating these features to uncover seasonality and trends.

# Contest Rules

## Organizer

The contest is organized by Falck Digital Technology Poland Sp. z o.o., based in Warsaw.

## Participants

The contest is open to individuals who are of legal age. Employees and co-workers of Falck Digital Technology are not eligible to participate.

## Contest Objective

Participants are required to develop a predictive machine learning model using Python to forecast daily call volumes for Falck’s Roadside Assistance Services in Denmark for December 2023.

## Participation Conditions

- Participation is voluntary and free.
- Participants must download the dataset and submit their predictions in the specified format.
- Predictions should be submitted via email to pedro.rodrigues@falck.com with the subject “[pytech_contest]”.

## Contest Deadline

- All answers must be submitted by the end of the day on Sunday, December 15, 2024.
- The competition results and winners will be announced by Friday, December 20, 2024, at the latest.

## Evaluation and Prizes

- Submissions will be evaluated based on the Mean Absolute Percentage Error (MAPE) of the predictions.
- The participant with the most accurate predictions will be awarded a prize.
- Winners will be notified via email.

### There are three prizes to be won:

1. **1st prize:** High-end gaming laptop - MSI Vector 16 HX i9-14900HX/32GB/1TB/Win11 RTX4080 240Hz
2. **2nd prize:** VR headset - OCULUS Meta Quest 3 512GB
3. **3rd prize:** Noise cancelling headphones - Sony WH-1000XM5

## Final Provisions

- The organizer reserves the right to modify the contest rules.
- Additional prizes may be awarded at the organizer's discretion.

# Personal Data Protection Policy
- https://brandportal.falck.com/m/25920523dcaea8ac/original/Personal-Data-Protection-Policy-v3-2021-01-06.pdf

# Falck Data Ethics Policy
- https://brandportal.falck.com/m/d8a08a0c3eeb471/original/Falck-Data-Ethics-Policy.pdf
