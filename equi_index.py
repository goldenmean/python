def equ_index(A):
    total = sum(A)
    sum_left = 0
    for i in range(len(A)):
        sum_right = total - sum_left - A[i]
        if sum_left == sum_right:
            return i
		sum_left = sum_left + A[i]
    return -1
	
arr=[-7, 1, 5, 2, -4, 3, 0]
arr2=[-7, 1 ,5 ,2,-4, 3, 0]
print equ_index(arr)





/*
int equi(int arr[], int n) {
    if (n==0) return -1; 
    long long sum = 0;
    int i; 
    for(i=0;i<n;i++) sum+=(long long) arr[i]; 

    long long sum_left = 0;    
    for(i=0;i<n;i++) {
        long long sum_right = sum - sum_left - (long long) arr[i];
        if (sum_left == sum_right) return i;
        sum_left += (long long) arr[i];
    } 
    return -1; 
} 

*/

A[0]=-7 A[1]=1 A[2]=5 A[3]=2 A[4]=-4 A[5]=3 A[6]=0