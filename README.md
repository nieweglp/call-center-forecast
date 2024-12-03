
![image](https://github.com/user-attachments/assets/910d7539-fbbd-48e8-adc8-687e5aca9fc2)

# Falck Digital Technology - Call Center Roadside Assistance Services

## Time-Series Forecasting

**Data Time Period:** March 2022 to November 2023  
**Estimated Time to Complete:** 4-8 hours

### Goal

Using Python, develop a predictive machine learning model to forecast daily call volumes for Falck Digital Technology’s Roadside Assistance Services in Denmark for December 2023. The goal is to accurately predict the total number of calls for each day in December 2023, leveraging historical data and any relevant external factors. Once completed, submit your predictions in the specified format to pedro.rodrigues@falck.com.

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
   
### Information on data processing (EN)

Acting on behalf of Falck Digital Technology Poland Sp. z o.o. based in Warsaw (00-838) at Prosta 67, registered in the Register of Entrepreneurs maintained by the District Court for the Capital City of Warsaw – Economic Court, 12th Commercial Division of the National Court Register under KRS number 0000964322, NIP 5272997346, pursuant to Article 13 of the Regulation (EU) 2016/679 of the European Parliament and of the Council of 27 April 2016 on the protection of natural persons with regard to the processing of personal data and on the free movement of such data, and repealing Directive 95/46/EC (General Data Protection Regulation) (OJ L 119, p. 1) (hereinafter: "GDPR"), we hereby inform you that:

1. The Data Controller of personal data processed in the recruitment process is Falck Digital Technology Poland Sp. z o.o. based in Warsaw (00-838) at Prosta 67. Contact with the Data Controller is possible via email at: DPO@falck.com.
2. For any matters related to the processing of your personal data by the Controller, you can contact the Data Protection Officer at: iod@falck.pl.
3. Personal data will be processed for the purpose of conducting the current recruitment process, and with your consent, also for future recruitments based on your consent (Article 6(1)(a) GDPR).
4. In recruitment processes, the Controller expects the provision of personal data (e.g., in a CV or resume) only to the extent specified in labor law. If a candidate provides other data not required by the Controller, it is assumed that they have consented to its processing, which can be withdrawn at any time without affecting the lawfulness of processing based on consent before its withdrawal. If applications contain information not relevant to the recruitment purpose, they will not be used or considered in the recruitment process.
5. Data collected in recruitment processes will be processed:
   - to fulfill legal obligations related to the employment process, primarily the Labor Code – the legal basis for processing is the legal obligation of the Controller (Article 6(1)(c) GDPR in connection with the Labor Code);
   - to conduct the recruitment process for data not required by law, and for future recruitment processes – the legal basis for processing is consent (Article 6(1)(a) GDPR);
   - to establish or defend against potential claims – the legal basis for processing is the legitimate interest of the Controller (Article 6(1)(f) GDPR).
6. The Data Controller does not transfer data outside the EU/EEA.
7. Personal data processed based on the legitimate interest of the Controller are processed for the period necessary to fulfill that interest or until a valid objection to their processing is raised. If processing is based on consent, data are processed until consent is withdrawn. Data processed based on a legal obligation are processed until the obligation ceases to exist under specific legal provisions.
8. The Data Controller does not transfer data outside the EU/EEA.
9. The data subject has the following rights:
   - the right to information about personal data processing;
   - the right to obtain a copy of the data;
   - the right to rectify data;
   - the right to delete data;
   - the right to restrict processing;
   - the right to data portability;
   - the right to withdraw consent.
10. The data subject also has the right to lodge a complaint with the President of the Personal Data Protection Office regarding unlawful processing of their personal data. This authority is competent to consider the complaint, but the right to lodge a complaint only concerns the lawfulness of personal data processing, not the recruitment process itself.

Providing data contained in recruitment documents is not mandatory, but it is a condition for applying for employment.
