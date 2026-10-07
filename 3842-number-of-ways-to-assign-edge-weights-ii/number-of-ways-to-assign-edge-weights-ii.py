
# Submitted by Krishna Mittal on 07/10/2026

import numpy

totals = [0] * 100_000
totals[1] = total = 1
for at in range(2, 100_000):
    totals[at] = (total := (2*total) % 1_000_000_007)

log2s = numpy.empty(200_000, dtype=numpy.int64)
spans = numpy.empty(200_000, dtype=numpy.uint32)
for at in range(1, 18):
    spans[1 << at:2 << at] = (1 << at) - 1
    log2s[1 << at:2 << at] = at

def assignEdgeWeights(
    _edges: List[List[int]], 
    queries: List[List[int]],
    totals=numpy.asarray(totals, dtype=numpy.uint32),
    ancestors=[0]*100_001,
    spans=spans, log2s=log2s,
    dtypes=(numpy.uint8,)*9 + (numpy.uint16,)*8 + (numpy.uint32,)*3,    
) -> List[int]:
    cnt = len(_edges) + 1
    edges = [[] for _ in range(cnt + 1)]
    for at, to in _edges:
        edges[at].append(to)
        edges[to].append(at)
    
    tour = []        
    ids = [0] * (cnt + 1)    
    rank = -1    
    depths = [0] * (cnt + 1)        
    seen = bytearray(cnt + 1)
    pending = [1]
    while True:
        if seen[at := pending[-1]]:
            if at != 1:
                tour.append(ancestors[at])
                del pending[-1]
                continue
            break
        else:
            seen[at] = 1
            tour.append(at)
            ids[at] = rank = rank + 1
            depth = depths[at] + 1
            for to in edges[at]:
                edges[to].remove(at)
                ancestors[to] = at
                depths[to] = depth
                pending.append(to)

    dtype = dtypes[cnt.bit_length()]
    ids = numpy.asarray(ids, dtype=dtype)    
    depths = numpy.asarray(depths, dtype=dtype)
    depths[ids] = depths    
    
    tour = ids[tour]    

    cnt = tour.size
    dtype = dtypes[cnt.bit_length()]
    tails = numpy.empty(cnt, dtype=dtype)    
    tails[tour] = indices = numpy.arange(cnt, dtype=dtype)

    bases = numpy.empty(cnt, dtype=dtype)    
    bases[tour[::-1]] = indices[::-1]    
        
    mins = numpy.empty((cnt.bit_length(), cnt), dtype=ids.dtype.type)
    mins[0, :] = tour
    for level in range(mins.shape[0] - 1):
        span = 1 << level
        to = mins[level + 1]
        numpy.minimum(
            tour[:cnt - 2*span + 1],
            tour[span:cnt - span + 1],
            out=to[:cnt - 2*span + 1]
        )
        tour = to
    
    queries = ids[queries]         
    solution = depths[queries].sum(axis=1)

    ats = bases[queries].min(axis=1)
    tos = tails[queries].max(axis=1)        
    lengths = tos - ats
    lengths += 1            
    levels = log2s[lengths]
    tos -= spans[lengths]
    depths += depths # double depths so as to speed-up subsequent operation    
    solution -= depths[numpy.minimum(mins[levels, ats], mins[levels, tos])]    
    return totals[solution].tolist()          

Solution = repeat(namedtuple('Solution', ('assignEdgeWeights',))(
    assignEdgeWeights
)).__next__
        