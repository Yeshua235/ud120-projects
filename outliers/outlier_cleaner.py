#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    ### your code goes here
    errors = (net_worths - predictions) ** 2
    cleaned_data = list(zip(ages, net_worths, errors))
    cleaned_data.sort(key=lambda x: x[2])
    cleaned_data = cleaned_data[:int(len(cleaned_data) * 0.9)]
    
    return cleaned_data

