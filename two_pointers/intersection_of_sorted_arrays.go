/**
 * @input A : Integer array
 * @input B : Integer array
 * 
 * @Output Integer array.
 */
func intersect(A []int , B []int )  ([]int) {
    res := []int{}
    
    ai, bi := 0, 0
    nA, nB := len(A), len(B)
    
    var a, b int
    
    for ai < nA && bi < nB{
        a = A[ai]
        b = B[bi]
        
        if a == b {
            res = append(res, a)
            ai++
            bi++
        }else if a > b{
            bi++
        }else {
            ai++
        }
    }
    
    return res
}
