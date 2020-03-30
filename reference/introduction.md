
# preference 
  This doc intends to offer an introduction and technical specifiction to the control system. Although the target readers are basiclly members of our lab, 

# Introduction
  This control system is designed for LabIon of school of physics and astronomy, Sun Yat-Sun university. Our lab is under prof. Le Luo's lead. 

  The main target of this system is to achieve fully automatic control of our equipments including a linear ion trap, which are used to conduct Precision atomic molecular photophysics experiments aiming to accomplish quantum simulation and quantum computation.

  The system is written in python. 
# Structure of the system
## Main hardware 
  - FPGA
  Our experiment system is revolved around an FPGA with high time resolution, which are used to control laser on and off. This FPGA is developed by M-Lab who offers a basic python getware. Specificlly, we use this FPGA to generate a square wave pulse with nanosecond-level time resolution, as the control signal to an Isolation switch. This switch allows and blocks an RF signal to an AOM and finally generate a laser pulse.
  - DC Source
  A 16-channel DC source is used to control 10 of 12 blades of the ion traps to alter the shape of the potential well and **compensate the micromotion?**. This DC source's resolution is less than 30uV and each channel can be controled seperately.
  - Microwave generator



## software
  The control system accomplish fully automatic control of the experiment equipments through several gui pannels, without any needed of programing.
  ### high accuracy timeline control sysyem
  laser sequency is the center of our experiment, and the timeline control system is of vital importance. M-Lab offers a geteare, the artiq system, that allows us to use python code to control the FPGA. However, the original getware requires users to write the timeline in python code, which is less convinience and hard to coorperate with other equipment. based on the artiq system, we develope it to our timeline control system, with a full-featured(within our experiment) gui pannel and no longer need to write any python code. 
  - brief introduction to artiq python getware
    This part intend to offer a fast introduction of the artiq system to interest readers, especially members of our Lab. The offical guidance can be view in [website]<http://m-labs.hk/experiment-control/resources/> and [manual]<https://m-labs.hk/artiq/manual/>. Here we mainly introduce the part we developed in our control system. 
  - structure of the timeline control system
  
  ### general hardware control system
# technical specification 
