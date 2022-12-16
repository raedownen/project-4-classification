# Classification Project

## Project Description
Companies all across the globe deal with customers leaving on a regular basis. These people are described as those who "churn". Telco is wondering, "Why are our customers leaving?" In this project I will look at data of their customers and identify drivers that might affect the chance a customer might churn.

## Project Goals
* Identify drivers of churn for Telco customers
* Use the identified drivers to develop a model to determine if a customer is likely to churn
* Churn is defined as a customer who has left Telco
* This information can be useful to help Telco find ways to retain customers who are likely to churn.

## Initial Thoughts

My initial hypothesis is that drivers of churn will be predictors of if a customer will churn in the near future.

## The Plan
* Aqcuire the data from Codeup mySQL database

* Prepare data
    * Remove redundant data columns (payment_type_id', 'internet_service_type_id', 'contract_type_id', 'customer_id', )
    * Drop customers whose total_charges are spaces; these customers are new customers (tenure=0 and churn=No)
    * Encode churn as 'churn_encoded' {'Yes': 1, 'No': 0}, then drop 'churn' column

* Explore data in search of drivers of churn
    * Answer the following initial question
        * How often do customers churn?
        * Does a customer's tenure affect churn?
        * Do higher monthly charges affect churn?
        * Does contract type affect churn? 
        * Do those with no tech support churn more?

* Develop a model to predict if a customer will churn
    * Use drivers identified through exploration to build different predictive models
    * Evaluate models on train and validate data
    * Select best model base on highest recall (because saying they didn't churn and they churned is more costly)
    * Evaluate the best model on the test data

* Draw conclusions

## Data dictionary
| Feature | Definition | Values |
|:--------|:-----------|:-------
|gender| The customer's gender| Male or Female|
|senior_citizen| Is this customer a senior citizen?| {'Yes': 1, 'No': 0} |
|partner| Does this person live with a partner?|'Yes', 'No'|
|dependents| Does this person live with dependents?| 'Yes', 'No'|
|tenure| The number of **months** a customer has been with the company| *float* |
|phone_service| Does this person subscribe to phone service?| 'Yes', 'No'|
|multiple_lines| Does this person have multiple phone lines?| 'Yes', 'No', 'No phone service'|
|online_security| Does this person subscribe to online security?| 'Yes', 'No', 'No internet service'|
|online_backup| Does this person subscribe to online backup?| 'Yes', 'No', 'No internet service'
|device_protection| Does this person subscribe to device protection?| 'Yes', 'No', 'No internet service'
|tech_support| Does this person subscribe to tech support?| 'Yes', 'No', 'No internet service'
|streaming_tv| Does this person subscribe to streaming TV?| 'Yes', 'No', 'No internet service'
|streaming_movies| Does this person subscribe to streaming movies?| 'Yes', 'No', 'No internet service'
|paperless_billing| Does this person use paperless billing?| 'Yes', 'No'
|monthly_charges| The amount a customer is currently charged per month| *float* |
|total_charges| The amount a customer has been charged since becoming a customer| *float* |
|contract_type| The length of contract the customer currently has| 'Month-to-month', 'One-year', or 'Two-year'|
|internet_service_type| Type of internet service | 'DSL', 'Fiber', 'None'|
|payment_type| The way the customer pays their bill. |'Mailed check', 'Electronic check', 'Credit card (automatic)', 'Bank transfer (automatic)'
|**Target variable**
|churn_encoded| Did the customer leave the company? | {'Yes': 1, 'No': 0}|


## Steps to Reproduce
1. Clone this repo
2. Acquire the data from Codeup mySQL "telco" database using your personal ```env.py``` file where you store your ```username```, ```password```, and ```host```
3. Put the data in the file containing the cloned repo.
4. Run notebook.

## Takeaways and Conclusions
* About 1/4 of our customers churn
* Tenure seems to be a driver of churn; we need to intice customers to stay around.
* Monthly_charges seem to be a driver of churn; we need to help lower monthly charges.
* Contract_type seems to be a driver of churn; we need to intice customers to sign longer contracts.
* Tech_support seems to be a driver of churn; we should encourage more customers to get tech support

## Recommendations
* To reduce churn, I would encourage the company to think about taking the following actions:
    * Seek out young customers and give discounts (lower monthly cost) in order to keep customers longer (increase tenure)
    * Seek out month-to-month contract customers and encourage them to sign a longer contract maybe through discounts
    * Seek out those who don't have tech support and give a free trial of tech support.

## Next Steps
* In the next iteration:
    * Look into how customers with internet add-ons are the same people then can see if they churn more or less.
    * Look into cost of add-ons and see if there are bundles that might reduce monthly charges. That could help us entice more customers to stay.