#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rpy2.robjects as ro
from rpy2.robjects.packages import importr

def gmt(titers: list, ci_method: str="quap", ci_level: float=0.95,
        options: list=None):
    '''
    Parameters
    ----------
    titers : list
        list of titers whose gmt is to be calculated. each titer should be string
        with thresholded titers denoted by < or >
    ci_method : str, optional
        The method to use when calculating confidence intervals. 
        The default is "quap".
    ci_level : float, optional
        The confidence level to use when calculating confidence intervals. 
        The default is 0.95.
    options : list, optional
        Options for the sampler. The default is None.

    Returns
    -------
    dictionary which contains mean of log2(titer/10) values, standard deviation
    of log2(titer/10) values and the confidence interval for these.

    '''

    if not isinstance(titers,list):
        raise ValueError(f'titers must be a list but is {type(list)}')
    if not all([isinstance(x,str) for x in titers]):
        raise ValueError(f'titers must only contain strings but contains {set([type(x) for x in titers]).difference([str])}')

    if ci_method not in ['quap', 'ETI', 'HDI', 'BCI', 'SI']:
        raise ValueError('ci_method must be one of the following: quap, ETI, HDI, BCI or SI')

    if not isinstance(ci_level, float):
        raise ValueError('ci_level must be a float but is {type(ci_level)}')
    if ci_level<0 or ci_level>1:
        raise ValueError('ci_level must be between 0 and 1')
        
    if options is not None:
        if not isinstance(options,list):
            raise ValueError('options must be a list but is {type(options)}') 
        options = ro.StrVector(options)
    else:   
        options = ro.ListVector([])

    titertools = importr('titertools')
    gmt = titertools.gmt
    
    titers = ro.StrVector(titers)        
    result = gmt(titers, ci_method, ci_level, options)
    
    mean = result[0]
    sd = result[1]
    
    mean_lower = result[2]
    sd_lower = result[3]

    mean_upper = result[4]  
    sd_upper = result[5]
    
    return {
        'mean':mean,
        'mean_lower':mean_lower,
        'mean_upper':mean_upper,
        'sd':sd,
        'sd_lower':sd_lower,
        'sd_upper':sd_upper
        }

