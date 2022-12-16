# Classification Project

## Project Description
Are charter schools any better concerning student discipline?  I explore the state of Texas's public education student discipline data by using classification methods and models.

## Project Goals
-Using data from TEA website, try to determine if school district type can be predicted by student discipline and enrollment numbersdiscipline -Develop a model to determine if a district is charter or traditional. -This information on district discipline may be useful to parents and future employees.
## Initial Thoughts

Hypothesis
Null H: Mean of disciplined students is the same for charter schools and traditional schools. Alt H: Mean of disciplined students is not the same for charter schools and traditional schools.

## The Plan
* Aqcuire the data from TEA website

* Prepare
*Renamed columns for ease of coding and to shorten column names.

*Removed data columns that did not meet project needs.

*Checked for duplicates, nulls, and -999 and removed those columns.

*Removed districts that did not have both enrollment and disciplined numbers.

*Encoded target variable, charter_status, as 'charter_encoded' {'Yes': 1, 'No': 0}, then dropped 'charter_status' column.

*Outliers were not removed.

*Created a pivot table to access items under the 'heading name' column to create 2 new columns.

*Feature engineered a new column from pivoted columns.

*Merged the pivot table onto the dataframe.

*Reset the index.

*Split data into train, validate, and test (50/30/20).


* Explore data to help predict charter school status with discipline data
    * Answer the following initial question
        * How likely is a school with high numbers a charter school?
        * Does enrollment affect status?
        * Why do some school districts have such high discipline numbers?
        * Does combination does the of enrollment and disciplined better predict status? 
        * The data captured 1122 individual school districts, will the ratio of school district types be similar to the discipline data?

* Develop 4 model to predict if a a district is a charter school
    * Use drivers identified through exploration to build different predictive models
    * Evaluate models on train and validate data
    * Select best model base on accuracy
    * Evaluate the best model on the test data

* Draw conclusions

### Data dictionary

| Feature | Definition | Values |
|:--------|:-----------|:-------
|dist_name| Scool District Name| Categorical|
|charter_encoded| Is the district type a charter school?| {'Yes': 1, 'No': 0} |
|enrollment| # of students enrolled in the district| Numerical |
|disciplined| # of student discipline incidents|Numerical'|
|discipline_percent| # disciplined/# enrolled|Numerical|

## Steps to Reproduce
1. #go to : https://rptsvr1.tea.texas.gov/adhocrpt/Disciplinary_Data_Products/Download_All_Districts.html
#download the csv for 2018/19, 2019/20, 2020/21, and 2021/22 School Years
#upload csv files:
df22 = pd.read_csv('DISTRICT_summary_22.csv')
df21 = pd.read_csv('DISTRICT_summary_21.csv')
df20 = pd.read_csv('DISTRICT_summary_20.csv')
df19 = pd.read_csv('DISTRICT_summary_19.csv')
3. Put the data in the file containing the cloned repo.
4. Run notebook.

## Takeaways and Conclusions
After modeling with 4 models, I have concluded that even though I had a "best" it didn't predict charter school status any better than baseline.

## Recommendations
Revisit this data over the holidays and feature engineer more variables, and look into other discipline reports that break it down by school.  I think this will better help in future modeling.

## Next Steps
I will use this data for another individual project and I would use more of the discipline data types and not just the whole number.  I will be able to break down the discipline by socio-economic staus, race, ethnicity, special. ed. services receiver, location, and by offense.