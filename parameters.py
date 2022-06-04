import numpy as np

def edt(impulse, fs = 44100):
    '''
    Input ndarray normalized impulse response in dBFS, return Early Decay
    Time value in seconds.
    
    Parameters
    ----------
    impulse: ndarray
        Numpy array containing the impulse response signal in dBFS
    fs: int
        The sample rate of the impluse response array.
    method: str, optional.
        Optional string to determine the desired smoothing method:
            + 'hilbert' for a Hilbert transform
            + 'median' to apply a median filter.
            + 'savgol' to apply a Savitzky-Golay filter.
    window_len: int
        The length of the filter window, must be a positive odd integer.
    polyorder: int
        The order of the polynomial used to fit the samples. 
        This value value must be less than window_length.
    '''
    #if impulse > 0 :
    #    raise ValueError('Input should have no positive values.')
    
    vectorT = np.arange(len(impulse))/fs 
    index_edt = np.where(((impulse <= -1) & (impulse >= -10)))
    coeff_edt = np.polyfit(vectorT[index_edt[0]],
                       impulse[index_edt[0]], 1)
    
    fit_edt = coeff_edt[0]*vectorT + coeff_edt[1]
    edt = len(fit_edt[fit_edt>=-10])/fs
    
    return edt

def t60(impulse, fs = 44100, method = 't30'):
    '''
    Input ndarray normalized impulse response in dBFS, returns the t60 value
    in seconds. Method should be chosen according to the background noise 
    level of the input signal.
    
    Parameters
    ----------
    impulse: ndarray
        Numpy array containing the impulse response signal in dBFS
    fs: int
        The sample rate of the impluse response array.
    method: str, optional.
        Optional string to determine the desired t60 method:
            + 't10' calculate from t10.
            + 't20' calculate from t20.
            + 't30' calculate from t30.
    '''
    
    #if impulse > 0 :
    #    raise ValueError('Input should have no positive values.')
    
    vectorT = np.arange(len(impulse))/fs 
    
    if method == 't10':
        index_t10 = np.where(((impulse <= -5) & (impulse >= -15)))
        coeff_t10 = np.polyfit(vectorT[index_t10[0]], impulse[index_t10[0]], 1)
        fit_t10 = coeff_t10[0]*vectorT + coeff_t10[1]
        t10 = len(fit_t10[fit_t10>=-10])/fs
        t60 = t10*6
        
    elif method == 't20':
        index_t20 = np.where(((impulse <= -5) & (impulse >= -25)))
        coeff_t20 = np.polyfit(vectorT[index_t20[0]], impulse[index_t20[0]], 1)
        fit_t20 = coeff_t20[0]*vectorT + coeff_t20[1]
        t20 = len(fit_t20[fit_t20>=-20])/fs
        t60 = t20*3

    elif method == 't30':
        index_t30 = np.where(((impulse <= -5) & (impulse >= -35)))
        coeff_t30 = np.polyfit(vectorT[index_t30[0]], impulse[index_t30[0]], 1)
        fit_t30 = coeff_t30[0]*vectorT + coeff_t30[1]
        t30 = len(fit_t30[fit_t30>=-30])/fs
        t60 = t30*2
        
    else:
        raise ValueError('Invalid Method.')
        
    return t60
        
def d50(impulse, fs):
    '''
    Input ndarray normalized impulse response in dBFS, return d50 value.
    The function uses Numpy to integrate the impulse.
    
    Parameters
    ----------
    impulse: ndarray
        Numpy array containing the impulse response signal in dBFS
    fs: int
        The sample rate of the impluse response array.
    '''
    t = round(0.050 * fs)
    d50 = 100 * (np.sum(impulse[:t]) / np.sum(impulse))
    
    return d50

def c80(impulse, fs):
    '''
    Input ndarray normalized impulse response in dBFS, return c80 value.
    The function uses Numpy to integrate the impulse.
    
    Parameters
    ----------
    impulse: ndarray
        Numpy array containing the impulse response signal in dBFS
    fs: int
        The sample rate of the impluse response array.
    '''
    t = round(0.080 * fs)
    c80 = 10 * np.log10(np.sum(impulse[:t]) / np.sum(impulse[t:]))
    
    return c80

