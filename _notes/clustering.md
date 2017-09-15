### theory

- K-means clustering is by far the most popular clustering algo;
- We randomly choose centers for clusters, classify points and 
change cluster centers by optimizing squared distance (to points from 
this cluster build in the previous step);
- Usually we have to choose ## of clusters manually; 
- This is high-climbing algorithm and it's susceptible to local minimums;
so in many cases we have to run it multiple times;