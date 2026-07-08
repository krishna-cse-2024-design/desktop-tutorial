var subsets = function(nums) {
    let outer = [[]];
    for (let num of nums) {
        let n = outer.length;
        for (let i = 0; i < n; i++) {
            let internal = outer[i].slice(); // Copy existing subset
            internal.push(num);
            outer.push(internal);
        }
    }
    return outer;
};