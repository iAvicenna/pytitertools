#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import math
import statistics
import pytitertools as ptt


class TestGMT(unittest.TestCase):
    
    def test_wronginputs(self):
        
        titers = ['20','40','100']
        
        with self.assertRaises(AssertionError):    # test the test
            with self.assertRaises(ValueError):
                ptt.gmt(titers)
        
        with self.assertRaises(ValueError):
            ptt.gmt(titers, ci_method='test')
            
        with self.assertRaises(ValueError):
            ptt.gmt(titers, ci_level=1.2)
            
        with self.assertRaises(ValueError):
            ptt.gmt(titers=[20,40,100])
            
        
            
    
    def test_nonthresholded(self):
        '''
        means and std of titers without thresholds should come out the same
        as computing them manually. Also test inequality.
        '''
        
        titers = ['20','40','100']
        
        log2_titers = [math.log2(20/10), math.log2(40/10), math.log2(100/10)]
        
        mean = sum(log2_titers)/len(log2_titers)
        sd = statistics.stdev(log2_titers)
        
        result1 = ptt.gmt(titers)
        
        with self.assertRaises(AssertionError):    # test the test
            self.assertAlmostEqual(0,result1['mean'],places=2)
            self.assertAlmostEqual(0,result1['sd'],places=2)
        
        self.assertAlmostEqual(mean,result1['mean'],places=2)
        #self.assertAlmostEqual(sd,result['sd'],places=2)
        
        titers = ['20','40']
        result2 = ptt.gmt(titers)
        
        
        
if __name__ == '__main__':
    
    unittest.main()
        
    
    

