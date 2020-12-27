# Advanced Regression Assignment

## Subjective Questions

**Question 1**

What is the optimal value of alpha for ridge and lasso regression? What will be the changes in the model if you choose double the value of alpha for both ridge and lasso? What will be the most important predictor variables after the change is implemented?

**Ans.**	
Optimal Value of Alpha for Ridge: 3 <br>
Most important predictor: NorthRidge neighborhood <br>
On doubling alpha, R2 score drops from 0.66 to 0.65 <br>
Most important predictor after doubling: NorthRidge neighborhood <br>

Optimal Value of Alpha for Lasso: 0.0001 <br>
Most important predictor: Adjacent to positive off-site feature <br>
On doubling alpha, R2 score drops from 0.67 to 0.66 <br>
Most important predictor after doubling: Meadow Village neighborhood <br>

**Question 2**

You have determined the optimal value of lambda for ridge and lasso regression during the assignment. Now, which one will you choose to apply and why?

**Ans.**	
Optimal Value of Alpha for Ridge: 3 <br>
R2 score of Ridge on Test data: 0.66 <br>

Optimal Value of Alpha for Lasso: 0.0001 <br>
R2 score of Lasso on Test data: 0.67 <br>

We will use Lasso as it gives a better accuracy and builds a simpler model by eliminating extra features.

**Question 3**

After building the model, you realised that the five most important predictor variables in the lasso model are not available in the incoming data. You will now have to create another model excluding the five most important predictor variables. Which are the five most important predictor variables now?

**Ans.**  
The next five most important features after our initial five are:
<li> Commercial MSZoning
<li> Old Town neighborhood
<li> Stone Brook neighborhood
<li> Edwards neighborhood
<li> Bark Side neighborhood

**Question 4**

How can you make sure that a model is robust and generalisable? What are the implications of the same for the accuracy of the model and why?

**Ans.**  
First we do recusive feature elimination and then apply lasso feature selection to ensure that the model is simple but not simpler.