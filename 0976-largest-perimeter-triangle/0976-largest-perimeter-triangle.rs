impl Solution {
    pub fn largest_perimeter(nums: Vec<i32>) -> i32 {
        let mut newNums = nums;
        newNums.sort();
        let n = newNums.len();
        for i in (2..n).rev() {
            println!("{}", i);
            if newNums[i] < newNums[i-1] + newNums[i-2] {
                return newNums[i] + newNums[i-1] + newNums[i-2];
            }
        }
        
        return 0;
    }
}