import scipy.optimize
import scipy.signal

def find_peaks(abs_spectrum, npeaks=3):
    ''' This will find the highest `npeaks` peaks and return a list of peak wavenumbers.
    `abs_spectrum` should be shape (N, 2)
    '''
    peaks, _ = scipy.signal.find_peaks(abs_spectrum[:, 1], distance=1)
    peaks = sorted(peaks, key=lambda x: abs_spectrum[x, 1], reverse=True)[:npeaks]
    wavenumbers = abs_spectrum[peaks, 0]
    return wavenumbers