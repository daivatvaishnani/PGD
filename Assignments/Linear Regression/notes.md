Advanced Regression

    Apply model selection principles in the regression framework
    Extend the linear regression framework to problems which are not strictly 'linear' and understand the difference between linear and nonlinear regression problems
    Select appropriate evaluation metrics for regression problems

    1. Generalized Linear Regression
        Real life data is not limited to follow only linear trends.
        Linear Regression may not be a good predictor always, we neeed to look at non-linear models as well.
        
        Generalized Regression Framework (Extending the regression framework)
            - Conduct exploratory data analysis by examining scatter plots of explanatory and dependent variables. 
            - Choose an appropriate set of functions which seem to fit the plot well, build models using them, and compare the results.
            - While constructing the regression model, instead of using the raw explanatory variables in the current form, we create some function of the explanatory variables to best explain the data points.
            
            "Raw attributes, as they appear in the training data, may not be the ones best suited to predict the response variable value with.

            In the blood pressure example, the attributes weight and height are individually not indicative of the blood pressure, though a derived feature such as BMI could predict it well. The derived features could be combinations of two or more attributes and/or transformations of individual attributes. These combinations and transformations could be linear or non-linear."

            - In general, create features from other predictor variables, that are more likely to predict the target. 
            - Feature Extraction: https://machinelearningmastery.com/discover-feature-engineering-how-to-engineer-features-and-how-to-get-good-at-it
            
            "Summarising the important takeaways from the lecture:

            1. In generalised regression models, the basic algorithm remains the same as linear regression- we compute the values of coefficients which result in the least possible error (best fit). The only difference is that we now use the features ϕ1(x),ϕ2(x),ϕ3(x)....ϕk(x) instead of the raw attributes.

            2. The term 'linear' in linear regression refers to the linearity in the coefficients, i.e. the target variable y is linearly related to the model coefficients. It does not require that y should be linearly related to the raw attributes or features - feature functions could be non-linear as well."

    2. Regularized Regression - Ridge and Lasso Regression
    

    3. Model evaluation
    