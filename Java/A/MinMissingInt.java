package Java.A;
class MinMissingInt {
    public int min_int(int[] A) {
        // Implement your solution here
        int i = 0; 
        do{
            if (A[i] > 0 && A[i] != i+1 && A[i] <= A.length && A[i] != A[A[i] - 1]){
                int t = A[i];
                A[i] = A[A[i] - 1];
                A[t - 1] = t;
            }
            else{
                i++;
            }
        } while(i < A.length);
        for (i = 0; i < A.length; i++){
            if (A[i] != i+1)
                return i+1;
        }
        return A.length + 1;
    }
    public static void main(String[] args){
        int [] A = {2, 3};
        MinMissingInt s = new MinMissingInt();
        System.out.println(s.min_int(A));
    }
}
