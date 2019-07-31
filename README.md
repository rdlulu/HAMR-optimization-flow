# HAMR-optimization-flow
Heat Assisted Magnetic Recording (HAMR) optimization flow demo

## Description
 This procedural flow demonstrates typical HAMR optimization process. Disclaimer: the code only demonstrate the very basic ideas and algorithms, but not in anyway represents the actual code/method used in production. Some modules are omitted but does not affect the overall understanding of the flow.
 HAMR is a technique to enable ultra-high data storage density on the hard disk drive, enabling data centers to store 5 times or more data with minimal cost increases. HAMR also increases sequential data-rate by ~2x. HAMR requires specially designed heads encompassing a magnetic writer (M.W), an optical Near Field Transducer (NFT) unit, and a Thermal-Mechanical (T.M) unit which compensates for the correct spacing between the disk and the head.  
 In the simulation, the goal is to reach the highest possible Areal Density Capacity (A.D.C.) with the optimal setting on all three components. A.D.C. = B.P.I (Bits per inch) * T.P.I(Tracks per inch). In spite of un-avoidable variations of head design and geometrics, this flow needs to find the best configurations regardless. Due to large manufacturing quantities (in the millions), the optimization flow needs to be as fast as possible.
 Typical flow:
 1. Load head, resistance/noise measurement
 2. optical power calibration
 3. head-disk-spacing calibration
 4. optical power + write field calibration
 5. un-bounded Bit Error Rate (BER) optimization
 6. bounded Bit Error Rate (BER) optimization under different T.P.I.
 7. Down-Track Thermal Gradient (D.T.T.G) measurement
 8. Cross-Track Thermal Gradient (C.T.T.G) measurement
 9. Write Track Width (W.T.W) measurement
 10. Data-rate capability measurement
 11. performance repeatability check
 12. Unload head, resistance/noise check
 Control parameters:
 1. Geometrics: NFT width, NFT height, NFT/MW distance, MW width,...
 2. Optical: Laser power, laser coupling efficiency
 3. Magnetic: write current, write overshoot current, write overshoot duration
 4. T-M: heater power
 
 
---
Requirements
----
Python
---
Installation intructions
----
1. Open Jupyter Notebook
2. Copy and Paste Code
3. Click Run

---
License
----

- None
                              
Contributors
----

