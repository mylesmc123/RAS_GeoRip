# RAS GeoRip

https://github.com/mylesmc123/RAS_GeoRip.git
## Description

Several LWI models were identified on the AWS S3 bucket. The repo to identify and map these model perimters is located at:
https://github.com/mylesmc123/s3_model_finder.git

The purpose of this repo is take an output list of the s3_model_finder, and use that list to extract the 'best' geometry from each model that has already been downloaded from the s3. The local model's data directory for each region is located at: 
"V:\projects\p00542_cpra_2020_lwi_t10\99_import\S3"

To identify the 'best' geometry fo reach model, the following criteria are used:

    1.  Check the highest plan number's geometry ##.
    2.  Check the geometry used in the highest plan ##.
    3.  Pull descriptions from each g file.

After a best g## is determined, the structures within the geometry will be extracted and merged in to the Coast-Wide RAS model's geometry.