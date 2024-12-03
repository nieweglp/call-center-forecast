## Partitioned Datasets

The dataset has been partitioned into three separate Parquet files to manage size limitations and facilitate efficient processing. Each partition represents a distinct time range within the overall dataset.

### Partition Details

1. **Partition 1**
   - **File Path**: `dataset/assistance_train_dataset_1.parquet`
   - **Date Range**: March 6, 2022, to October 31, 2022
   - **Description**: This partition contains call records from the early part of the dataset, covering the initial months of data collection.

2. **Partition 2**
   - **File Path**: `dataset/assistance_train_dataset_2.parquet`
   - **Date Range**: November 1, 2022, to May 31, 2023
   - **Description**: This partition includes call records from the middle period of the dataset, capturing seasonal trends and variations.

3. **Partition 3**
   - **File Path**: `dataset/assistance_train_dataset_3.parquet`
   - **Date Range**: June 1, 2023, to November 30, 2023
   - **Description**: This partition contains the most recent call records, providing insights into the latest patterns and behaviors.

### Usage Instructions

- **Loading Data**: Use Python pands or PySpark or any other compatible tool to load each Parquet file as needed. Ensure that your environment has access to the specified file paths.
- **Combining Partitions**: If you need to work with the entire dataset, you can load all three partitions and union them in your data processing pipeline.
- **Analysis**: Each partition can be analyzed independently or in combination, depending on your specific requirements and the focus of your analysis.

These partitions allow for more manageable data processing and can be used to explore different time periods within the dataset.
