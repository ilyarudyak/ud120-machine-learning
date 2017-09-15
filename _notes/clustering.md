### theory

- K-means clustering is by far the most popular clustering algo;
- We randomly choose centers for clusters, classify points and 
change cluster centers by optimizing squared distance (to points from 
this cluster build in the previous step);
- Usually we have to choose ## of clusters manually; 
- This is high-climbing algorithm and it's susceptible to local minimums;
so in many cases we have to run it multiple times;

### mini-project

- n_clusters=8 - by default sklearn uses 8 clusters; usually we have 
manually choose ## of clusters;
- n_init=10 - number of different attempts to initialize parameters; 
again usually we have to do this to escape from local minimum;
- max_iter=300 - usually this is fine and ## of iterations will be
much less;