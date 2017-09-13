### theory

- the problem with accuracy that we sometimes interested in 
true/false positive/negative (for example we're really interested in
right diagnosis);

- we may use confusion matrix 2x2: actual vs. predicted;

- recall: true positive / (true positive + false negative);
precision: true positive / (true positive + false positive);
in case of HC: TP = 10, FN = 6 (in row, we identified someone else (N), but it's HC (F)), 
FP = 0 (in column, we identified HC (P), but it's someone else (F));

### mini-project

- in testing set we have 29 elements and 25 of them non-POI; so 
guessing 0 POI gives us 25/29 = 86%;

- we predict initially 4 POI and also have 4 PI in testing set;
but they're all different - we don't have a single *true positive*;

- 