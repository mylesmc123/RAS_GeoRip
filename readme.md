# RAS GeoRip

https://github.com/mylesmc123/RAS_GeoRip.git

## Context

Several LWI models were identified on the AWS S3 bucket. The repo to identify and map these model perimeters is located at:
https://github.com/mylesmc123/s3_model_finder.git

The output webapp can be seen here:
https://lwi-aws-s3-hec-ras-models.onrender.com

![image](https://github.com/mylesmc123/RAS_GeoRip/assets/64209352/425d3f7a-0a2a-4728-86b2-93d9f5b9bd27)


### Purpose

The purpose of this repo is take an output list of the s3_model_finder ("s3_model_finder\output\Processed Models.json"), and use that list to extract the 'best' geometry from each model that has already been downloaded from the s3. The local model's data directory for each region is located at: 
"V:\projects\p00542_cpra_2020_lwi_t10\99_import\S3"

To identify the 'best' geometry fo reach model, the following criteria are used:

    1.  Check the highest plan number's geometry ##.
    2.  Check the geometry used in the highest plan ##.
    3.  Pull descriptions from each g file.

After a best g## is determined, the structures within the geometry will be extracted and merged in to the Coast-Wide RAS model's geometry.
