### naive bayes

- It's actually really easy to implement.
- Big feature spaces there is between 20,000 and 200,000 words 
in the English language.
- It's really simple to run, it's really efficient.

- There are a few things that Naive Bayes doesn't do as well that 
you also want to be careful of. *Example: So, historically when Google 
first sent it out, when people searched for Chicago Bulls, which is 
a sports team comprised of two words, Chicago Bulls. Would show many 
images of bulls, animals, and of cities, like Chicago*.

### svm

- So they work really well in complicated domains where there is 
a clear margin of separation.

- They don't perform so well in very large data sets, because the 
training time happens to be cubic in the size of the data set.
- They also don't work well with lots and lots of noise. So when 
the class are very overlapping you have to count independent evidence.
That's where then a Naive Bayes classifier would be better.

### decision trees

- So they're really easy to use and they're beautiful to grow on. 
- They're, they're graphically, in some sense, allow you to interpret 
the data really well, and you can really understand them much better 
then say the result of a support vector machine.

- One of the things that's true about decision trees is they're prone 
to over-fitting. Especially if you have data that has lots and lots 
of features and a complicated decision tree it can over fit the data.

- One of the things that's also really cool about decision trees, 
though, is that you can build bigger classifiers out of decision trees 
in something called ensemble methods.
