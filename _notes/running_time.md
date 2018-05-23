### naive bayes

- *full set*: accuracy=`92.0%` fit_time=`0.1359s` pred_time=`0.0154s`;

### SVM

#### linear kernel
- *full set*: accuracy=`96.0%` fit_time=`23.1004s` pred_time=`2.0995s`
- *small set*: accuracy=`85.5%` fit_time=`0.0088s` pred_time=`0.0880s`

#### rbf kernel

- *small set*: accuracy=`59.0%` fit_time=`0.0110s` pred_time=`0.1068s`
- *small set, optimize C*: C=`10` accuracy=`59.0%`; C=`100` accuracy=`76.2%`; C=`1000` accuracy=`90.2%`;
C=`10000` accuracy=`88.1%`;
- *full set, C=`1000`*: accuracy=`96.8%` fit_time=`16.8104s` pred_time=`1.6953s`;

### decision trees

- min_samples_split=`40`, percentile=`1`: accuracy=`96.7%` fit_time=`4.8998s` pred_time=`0.0019s`;
- min_samples_split=`40`, percentile=`10`: accuracy=`97.8%` fit_time=`73.1424s` pred_time=`0.0321s`;
