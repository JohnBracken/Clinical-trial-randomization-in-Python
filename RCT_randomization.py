#The following code is an example of a randomization scheme for enrolling patients
#into a randomized controlled trial with two different arms.  A patient could
#be randomized into either of the two arms (but not both).  One arm is the control arm, and patients randomized to
#this arm would receive standard-of-care treatment.  The other arm is the experimental arm, and patients
#enrolled into this arm would receive the new experimental treatment.  This randomization scheme is similar to tossing
#a coin, with the probability of a "success" on the coin flip (ie. heads, but could also be tails) being equal
#to 0.5 using a fair coin.  In this case, an endovascular treatment trial is simulated for the treatment of stroke.
#One patient arm will be the control arm, in which patients who are suffering from an ischemic stroke are treated
#with tissue plasminogen activator (tPA) only if they are randomized into this arm, which is the standard
#of care approach.  The other arm is the experimental arm, and patients randomized into this arm will be treated
#with both tPA, and they will also be treated with  with a stent retriever device percutaneously to remove the clot.



#Import the numeric Python library for statistical analysis.
import numpy as np



#Set the probability of a "success" on a coin flip (ie. heads), which is 50%.  In this case, a patient with a heads
#outcome would be randomized into the experimental arm.
p = 0.5



#Set the total number of coin flips, which is actually equal to the total number of patients enrolled in the trial
#across both arms.  In this case, let's assume a fairly large, multicenter trial encompassing 500 patients.
n = 500



#Calculate the number of patients randomized into the experimental arm.  Coin flips adhere to a binomial
#probability distribution.
exp_arm = np.random.binomial(n, p, 1)



#Number of patients randomized into the control arm.
control_arm =  n - exp_arm



#Print the results of the randomization.
print("Number of patients to receive tPA only (control group): ", control_arm[0])
print("Number of patients to receive tPA and endovascular treatment (experimental arm): ", exp_arm[0])





