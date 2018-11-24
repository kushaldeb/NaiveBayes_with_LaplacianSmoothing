# NaiveBayes_with_LaplacianSmoothing
Implementing Naive Bayes with Laplacian smothing on tennis data to predict Play is YES or NO.
<br/>
<hr/>
In this case Laplacian smoothing will be applied whenever we select "Outlook = overcast" because in the given dataset "Outlook = overcast" always results in "Play = yes".<br/>
Hence,    P(no|Outlook=overcast) = 0<br/>
Here the overall probability for "no" will become 0. To avoid this we apply Laplacian Smoothing.<hr/>
