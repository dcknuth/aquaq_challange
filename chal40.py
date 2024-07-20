# find the sum of the "prominences"
filename = 'input40.txt'
#filename = 'test40-2.txt'
#filename = 'test40.txt'

with open(filename) as f:
    ls = f.read().strip().split()
topo = list(map(int, ls))

peaks = []
# find peaks
last_topo = topo[0]
for i, elevation in enumerate(topo[1:-1]):
    if last_topo == elevation:
        print("Error: we assumed the elevation was always moving")
    if last_topo < elevation and elevation > topo[i+2]:
        peaks.append([elevation, i+1])
    last_topo = elevation
# find minimum drop to reach a higher peak (look each direction)
peak_prominences = []
for i, peak in enumerate(peaks):
    elevation, j = peak
    # look left
    left_prominence = -1
    k = i - 1
    while k >= 0:
        if peaks[k][0] >= elevation:
            left_prominence = elevation - min(topo[peaks[k][1]:j])
            break
        k -= 1
    # look right
    right_prominence = -1
    k = i + 1
    while k < len(peaks):
        if peaks[k][0] >= elevation:
            right_prominence = elevation - min(topo[j:peaks[k][1]])
            break
        k += 1
    # which is lower or only or top peak
    if left_prominence < 0 and right_prominence < 0:
        peak_prominences.append([elevation, j])
    elif left_prominence < 0:
        peak_prominences.append([right_prominence, j])
    elif right_prominence < 0:
        peak_prominences.append([left_prominence, j])
    elif left_prominence < right_prominence:
        peak_prominences.append([left_prominence, j])
    else:
        peak_prominences.append([right_prominence, j])

# sum those minimum drops to reach a higher peak
total_p = 0
for p, i in peak_prominences:
    total_p += p

print(total_p)
