/**
 * @input A : Integer array
 * 
 * @Output Integer
 */
func solve(A []int )  (int) {
    
    dp := map[int][]int{}
    
    root := 0
    for i, a := range A {
        if a == -1 {
            root = i
            continue
        }
        
        if _, ok := dp[a]; !ok {
            dp[a] = []int{}
        }
        
        dp[a] = append(dp[a], i)
    }
    
    var process func(int) int
    
    mx := 0
    process = func(k int) int {
        if len(dp[k]) == 0{
            return 0
        }
        
        // d1 >= d2
        d1, d2 := 0, 0
        for _, v := range dp[k] {
            curr := process(v) + 1
            
            if curr >= d1 {
                d1, d2 = curr, d1
            } else if curr > d2 {
                d1, d2 = d1, curr
            }
        }
        
        mx = max(mx, d1 + d2)
        
        return d1
    }
    
    process(root)
    return mx
}


func max(a, b int) int {
    if a > b {
        return a
    }
    
    return b
}
