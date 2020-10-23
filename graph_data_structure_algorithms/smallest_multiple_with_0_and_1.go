/**
 * @input A : Integer
 * 
 * @Output string.
 */
 
import (
    "fmt"    
)

type Node struct {
    ans string
    val int
}
func multiple(A int )  (string) {
    queue := []Node{}
    isChecked := make([]bool, A)
    
    
    sol := int64(0)
    for {
        q := queue[0]
        queue = queue[1:]
        
        res := q % int64(A)
        
        if res == 0{
            sol = q
            break   
        }
        
        queue = append(queue, int64(10)*q, int64(10)*q + 1)
        
    }
    
    return fmt.Sprintf("%d", sol)
}
