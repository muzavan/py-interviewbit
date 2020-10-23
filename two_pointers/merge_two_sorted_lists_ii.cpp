/**
 * @input A : Integer array
 * @input n1 : Integer array's ( A ) length
 * @input B : Integer array
 * @input n2 : Integer array's ( B ) length
 * 
 * @Return Returns a array of size n1 + n2 with A and B merged. 
 */
int* merge(int* A, int n1, int* B, int n2) {
    int* nA = (int*) malloc((n1 + n2) * sizeof(int));
    
    int ai = 0;
    int bi = 0;
    int a, b;
    
    while(ai < n1 && bi < n2){
        a = A[ai];
        b = B[bi];
        
        if(a < b){
            nA[ai+bi] = a;
            ai++;
        }
        else{
            nA[ai+bi] = b;
            bi++;
        }
    }
    
    if (ai == n1){
        for(; bi < n2; bi++){
            nA[ai+bi] = B[bi];
        }
    }
    else{
        for(; ai < n1; ai++){
            nA[ai+bi] = A[ai];
        }
    }
    
    A = nA;
    
    return A;
}
