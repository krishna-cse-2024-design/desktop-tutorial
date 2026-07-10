func pathExistenceQueries(n int, nums []int, maxDiff int, queries [][]int) []int {
    idx := make([]int, n)
    for i := range idx {
        idx[i] = i
    }
    sort.Slice(idx, func (i, j int) bool { return nums[idx[i]] < nums[idx[j]] })
    r := make([]int, n)
    arr := make([]int, n)
    for i, g, b := 0, 0, -1; i < n; i++ {
        u := idx[i]
        if nums[u] > b {
            g = u
        }
        r[u], b = g, nums[u] + maxDiff
        arr[u] = idx[i + sort.Search(n - 1 - i, func (j int) bool { return nums[idx[j + i + 1]] > b })]
    }
    dp := [][]int{arr}
    for b := 2; b < n; b <<= 1 {
        arr2 := make([]int, n)
        for i := range arr2 {
            arr2[i] = arr[arr[i]]
        }
        dp = append(dp, arr2)
        arr = arr2
    }
    res := make([]int, len(queries))
    m := len(dp)
    for i, q := range queries {
        u, v := q[0], q[1]
        switch {
            case r[u] != r[v]:
            res[i] = -1
            continue
            case nums[v] < nums[u]:
            u, v = v, u
        }
        for u != v {
            k := sort.Search(m, func (k int) bool { return nums[dp[k][u]] >= nums[v] })
            if k == 0 {
                res[i]++
                u = v
            } else {
                res[i] += 1 << (k - 1)
                u = dp[k - 1][u]
            }
        }
    }
    return res
}