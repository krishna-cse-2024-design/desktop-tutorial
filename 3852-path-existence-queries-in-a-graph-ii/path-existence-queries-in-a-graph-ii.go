func pathExistenceQueries(n int, nums []int, maxDiff int, queries [][]int) []int {
    idx := make([]int, n)
	pos := make([]int, n)

	for i := 0; i < n; i++ {
		idx[i] = i
	}

	sort.Slice(idx, func(i, j int) bool {
		return nums[idx[i]] < nums[idx[j]]
	})

	for i := 0; i < n; i++ {
		pos[idx[i]] = i
	}

	m := 0
	for t := n; t > 0; t >>= 1 {
		m++
	}

	f := make([][]int, n)
	for i := range f {
		f[i] = make([]int, m)
	}

	left := 0

	for i := 0; i < n; i++ {
		for left < i &&
			nums[idx[i]]-nums[idx[left]] > maxDiff {
			left++
		}

		f[i][0] = left
	}

	for j := 1; j < m; j++ {
		for i := 0; i < n; i++ {
			f[i][j] = f[f[i][j-1]][j-1]
		}
	}

	res := make([]int, 0, len(queries))

	for _, q := range queries {

		x := pos[q[0]]
		y := pos[q[1]]

		if x > y {
			x, y = y, x
		}

		if x == y {
			res = append(res, 0)
			continue
		}

		step := 0

		for i := m - 1; i >= 0; i-- {
			if f[y][i] > x {
				y = f[y][i]
				step += 1 << i
			}
		}

		if f[y][0] <= x {
			res = append(res, step+1)
		} else {
			res = append(res, -1)
		}
	}

	return res
}