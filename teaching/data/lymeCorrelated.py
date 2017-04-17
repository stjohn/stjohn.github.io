import linear_algebra
import statistics


ny = [5399,5100,5565,4460,4165,5741,4134,2385,3118]
nj = [2887,2698,3363,2432,3134,3214,4598,3320,3398]
ct = [1403,1348,1810,1788,3058,2738,2751,1964,2004]

print "NY", statistics.mean(ny)
print "NJ", statistics.mean(nj)
print "CT", statistics.mean(ct)

print "cor(NY, NJ)", statistics.correlation(ny,nj)
print "cor(NY, CT)", statistics.correlation(ny,ct)
print "cor(NJ, CT)", statistics.correlation(nj,ct)
