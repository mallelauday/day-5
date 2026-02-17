# day-5
Step-1:store full name and calculate length excluding spaces.
Step-2:Computes PLI= Length % 3.
Step-3: Takes input size and read request list using a for loop.
Step-4: Classify each request:
       <0 ->invalid
       0->No demand
       1-20->Low
       21-50->Moderate 
       >=51->High
Step-5:Apply PLI rule:
      PLI=0->removes Low
      PLI=1->removes High
      PLI=2->keeps only Modearate
Step-6: Prints final report with count and valid.
