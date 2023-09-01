# RAS GeoRip

https://github.com/mylesmc123/RAS_GeoRip.git

## Context

Several LWI models were identified on the AWS S3 bucket. The repo to identify and map these model perimeters is located at:
https://github.com/mylesmc123/s3_model_finder.git

The output webapp can be seen here:
https://lwi-aws-s3-hec-ras-models.onrender.com

![image](https://github.com/mylesmc123/RAS_GeoRip/assets/64209352/425d3f7a-0a2a-4728-86b2-93d9f5b9bd27)


### Purpose

The purpose of this repo is take an output list of the s3_model_finder ("s3_model_finder\output\Processed Models.json"), and use that list, and append in additional models locally extracted from .zip. After the list of models is finalized, extract the 'best' geometry from each model that has already been downloaded from the s3. The local model's data directory for each region is located at: 
"V:\projects\p00542_cpra_2020_lwi_t10\99_import\S3"

To identify the 'best' geometry fo reach model, the following criteria are used:

    1.  Check the highest geometry ##.
    2.  Check the geometry used in the highest plan ##.
    3.  Pull descriptions from each g file.
    4.  For each plan, pull description and which g file is used.

After a best g## is determined, the structures within the geometry files will be extracted and mapped. Once structure locations are reviewed, they will be merged in to the Coast-Wide RAS model's geometry file.

### Request to Regions (9/1/2023)

Based on preliminary findings from the georip notebook a data request was made to the regions to provide the following data:

1.	Review spreadsheet of model inventory to ensure all your models are there.
2.	Fill in Column J to specify the best geometry file number (Ex: g.01).

The spreadsheet sent is: "./model_list.xlsx".

The memo data request sent is "./Data Request to Regions.docx"

Once it has been returned, we will have a final list of models and geometry files to use for the next steps:

#### TODO

1.  Read each best g file in the returned excel sheet from the regions.
2.  Get desctiption, and structures from best g files.
3.  Map structures with descriptions as popups.
4.  Create merged g file for coast-wide model.