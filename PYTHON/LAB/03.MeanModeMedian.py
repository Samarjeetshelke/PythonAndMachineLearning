import statistics as st
import numpy as np
import scipy as sp

lis = [12,43,56,1,88,89,134];


print("Mean Mode Median Using Statistic:");
print(f"The Mean of the list:{st.mean(lis)}");
print(f"The Mode of the list:{st.mode(lis)}");
print(f"The Median of the list:{st.median(lis)}");

print(f"Mean Mode Median Without Anything:");
print(f"Mean: {sum(lis)/len(lis)}");

data = np.array(lis)
print(f"Mean :{st.mean(data)}")


print(f"Mean Mode Median Using Scipy:")
