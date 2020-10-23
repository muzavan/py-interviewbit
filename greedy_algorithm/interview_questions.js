module.exports = { 
 //param A : array of integers
 //return an integer
    bulbs : function(A){
        let numFlip = 0;
        
        for(let bulb of A){
            const currBulb = (bulb + numFlip) % 2;
            
            if (currBulb === 0){
                numFlip += 1;
            }
            
        }
        
        return numFlip;
    }
};
