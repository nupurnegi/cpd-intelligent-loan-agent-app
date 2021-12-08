### 1.0 Install required packages
# pip install --user ibm_watson_machine_learning --upgrade | tail -n 1
# pip install --user pyspark==3.0.0 --upgrade | tail -n 1

### 1.1 Package Imports
import pandas as pd
import numpy as np
import json
import os

### 2.0 Load data
df = pd.read_csv("german_credit_data.csv")
df.head()

### 2.1 Drop Some Features
#Some columns are data attributes that we will not want to use in the machine learning model. We can drop those columns / features:
df = df.drop(columns=['CUSTOMERID', 'FIRSTNAME', 'LASTNAME', 'EMAIL', 'STREETADDRESS', 'CITY', 'STATE', 'POSTALCODE'], axis=1, errors='ignore')
df.head(5)

### 2.2 Check for missing data
# Check if we have any NaN values and see which features have missing values that should be addressed
print(df.isnull().values.any())
df.isnull().sum()

### 2.3 Categorize Features
#We will categorize some of the columns / features based on wether they are categorical values or continuous (i.e numerical) values.
TARGET_LABEL_COLUMN_NAME = 'RISK'
columns_idx = np.s_[0:] # Slice of first row(header) with all columns.
first_record_idx = np.s_[0] # Index of first record

string_fields = [type(fld) is str for fld in df.iloc[first_record_idx, columns_idx]] # All string fields
all_features = [x for x in df.columns if x != TARGET_LABEL_COLUMN_NAME]
categorical_columns = list(np.array(df.columns)[columns_idx][string_fields])
categorical_features = [x for x in categorical_columns if x != TARGET_LABEL_COLUMN_NAME]
continuous_features = [x for x in all_features if x not in categorical_features]

print('All Features: ', all_features)
print('\nCategorical Features: ', categorical_features)
print('\nContinuous Features: ', continuous_features)
print('\nAll Categorical Columns: ', categorical_columns)


### 3.0 Create a model
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()
df_data = spark.createDataFrame(df)
df_data.head()


### 3.1 Split the data into training and test sets
spark_df = df_data
(train_data, test_data) = spark_df.randomSplit([0.8, 0.2], 24)

print("Number of records for training: " + str(train_data.count()))
print("Number of records for evaluation: " + str(test_data.count()))

### 3.2 Use StringIndexer to encode a string column of labels to a column of label indices
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.feature import OneHotEncoder, StringIndexer, IndexToString, VectorAssembler, SQLTransformer
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from pyspark.ml import Pipeline, Model

#Create StringIndexer columns whose names are same as the categorical column with an appended _IX.
categorical_num_features = [x + '_IX' for x in categorical_features]
si_list = [StringIndexer(inputCol=nm_in, outputCol=nm_out) for nm_in, nm_out in zip(categorical_features, categorical_num_features)]

# Encode our target label column (i.e Risk or No Risk). 
# Also, creates an label convert which performs an inverse map to get back a 'Risk' or 'No Risk' label from the encoded prediction.
si_label = StringIndexer(inputCol=TARGET_LABEL_COLUMN_NAME, outputCol="label").fit(spark_df)
label_converter = IndexToString(inputCol="prediction", outputCol="predictedLabel", labels=si_label.labels)

# Construct all encoded categorical features plus continuous features into a vector
va_features = VectorAssembler(inputCols=categorical_num_features + continuous_features, outputCol="features")

### 3.3 Create a pipeline, and fit a model using RandomForestClassifier 
classifier = RandomForestClassifier(featuresCol="features")
feature_filter = SQLTransformer(statement="SELECT * FROM __THIS__")
pipeline = Pipeline(stages= si_list + [si_label, va_features, classifier, label_converter, feature_filter])

model = pipeline.fit(train_data)

predictions = model.transform(test_data)
evaluatorDT = BinaryClassificationEvaluator(rawPredictionCol="prediction",  metricName='areaUnderROC')
area_under_curve = evaluatorDT.evaluate(predictions)

evaluatorDT = BinaryClassificationEvaluator(rawPredictionCol="prediction",  metricName='areaUnderPR')
area_under_PR = evaluatorDT.evaluate(predictions)
#default evaluation is areaUnderROC
print("areaUnderROC = %g" % area_under_curve, "areaUnderPR = %g" % area_under_PR)


### 3.4 evaluate more metrics by exporting them into pandas and numpy
from sklearn.metrics import classification_report
y_pred = predictions.toPandas()['prediction']
y_pred = ['Risk' if pred == 1.0 else 'No Risk' for pred in y_pred]
y_test = test_data.toPandas()[TARGET_LABEL_COLUMN_NAME]
print(classification_report(y_test, y_pred, target_names=['Risk', 'No Risk']))

## 4.0 Save the model and test data
from ibm_watson_machine_learning import APIClient

wml_credentials = {
  "apikey": "vZckTa66fQ5vJRD3GUMU_MyiqhK_pu8lmphZNOf2AnA-",
  "url": "https://us-south.ml.cloud.ibm.com"
}
client = APIClient(wml_credentials)

### 4.1 Get Space ID of your deployment
MODEL_NAME = "RISK MODEL"
DEPLOYMENT_SPACE_NAME = "Intelligent Loan Agent - Deployment Space"

all_spaces = client.spaces.get_details()['resources']
space_id = None
for space in all_spaces:
    if space['entity']['name'] == DEPLOYMENT_SPACE_NAME:
        space_id = space["metadata"]["id"]
        print("\nDeployment Space GUID: ", space_id)

if space_id is None:
    print("WARNING: Your space does not exist. Create a deployment space before proceeding to the next cell.")
client.set.default_space(space_id)

### 4.2 publish the model
sofware_spec_uid = client.software_specifications.get_id_by_name('spark-mllib_3.0-py37')
metadata = {
            client.repository.ModelMetaNames.NAME: MODEL_NAME,
            client.repository.ModelMetaNames.TYPE: 'mllib_3.0',
            client.repository.ModelMetaNames.SOFTWARE_SPEC_UID: sofware_spec_uid
        }
published_model = client.repository.store_model(model, metadata, training_data=df,  pipeline=pipeline)
published_model_uid = client.repository.get_model_uid(published_model)

loaded_model = client.repository.load(published_model_uid)

### 4.3 Deploy the model
deploy_meta = {
     client.deployments.ConfigurationMetaNames.NAME: 'Deployment of RISK MODEL',
     client.deployments.ConfigurationMetaNames.ONLINE: {}
}
created_deployment = client.deployments.create(published_model_uid, meta_props=deploy_meta)
scoring_endpoint = client.deployments.get_scoring_href(created_deployment)
print('MODEL_URL :' + scoring_endpoint)
