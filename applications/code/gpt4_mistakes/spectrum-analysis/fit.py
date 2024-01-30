s = np.loadtxt(
    'https://raw.githubusercontent.com/whitead/numerical_stats/master/unit_12/lectures/spectrum.txt')
# clean up to be like an absorption spectrum
s[:, 1] /= np.max(s[:, 1])
ints = np.array(find_peaks(s, 4))

true = [609, 645, 670]

result = len(ints) == 4
for t in true:
    result = result and np.any(np.abs(ints - t) < 5)
