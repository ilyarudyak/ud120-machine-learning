### theory

- SVM maximizes margins - distance to nearest points;
- outliers sometimes just ignored;
- SVM is a non-linear classifier; we transform features 
with kernel functions to get separable data in higher dimensions;
- it's not the best algorithms for large data sets (!) and 
very noisy data; of course it's much slower than naive bayes; 

### mini project

- C controls trade off between smooth decision boundary and
classifying training points correctly; high values - more complex 
boundary;
- gamma defines how far the influence of a single training 
example reaches; low values - far, high values - close; 
so we can ignore some points near decision boundary;
- speed-accuracy trade off;
- when using RBF kernel you'll have to optimize C parameter;