

# This document is not complete and is still being updated
# preface
  This doc intends to offer an introduction and a technical specifiction to the control system. Although the target readers are basiclly members of our lab, I firmly believe that one can always find something interesting here.

  I started this project at the begining of 2018, months after I entered SYSU as an undergraduate. Thanks to my experience with Pascal and Arduino in high school, I got the opportunity to work for the Trap Ion Lab in school of physics and astronmy, assigned to write the control system. 

  At the very first I have little knowledge on python as well as other experiment equipments which were far more conplicated than relays or a little infrared sensor. I still remember how panic I was when the seller of an FPGA extend model trying to explain the specification to me, and how many nights I spent in the labotary. I have encountered countless troble during the procedure, as well as learned large amount of knowledge. It is this invaluable experience that helps me develope my progromming skills and got a bisic understanding of morden experimental physics. 
  
  I would like to express my gratitude to Dr. Wang Zhao, who selflessly offers any kind of guidance and spport to me. I would also like to thank prof. Le Luo for offering that opportunity and enlightened me with the beauty of atomic physics.  I appreciate the help from Mr. Sébastien Bourdeauducq in M-Lab and the help from Dr. Cui Kaifeng in Chinese Academy of Sciences for their patient guidance.

# Introduction
  This control system is designed for LabIon of school of physics and astronomy, Sun Yat-Sun university. Our lab is under prof. Le Luo's lead. 

  The main target of this system is to achieve fully automatic control of our equipments.The centre of our equipment is a linear ion trap, which are used to conduct Precision atomic molecular photophysics experiments aiming to accomplish quantum simulation and quantum computation. Another important part is an FPGA bought from M-Lab, used to control the timeline of the experiment. Others equipment includes RF signal suorces, CCD, PMT, RWG, etc.

  The system is written in python. As I expressed in preference, this control system is also the procedure of my learning about python. You may even find the trace of my learning, from repeating a similar code several times to using extremly conplicate multiple `getattr` and `setattr`. Although most of the "historic problems" will not influence the operation of the control system, there are still something I did not optimize out of caution and one should pay attention to. 

# Copyright and ownership issue
  Since this control system is my most important work at the first two years in university and I am going to mention this work when I apply a higher academic degree, I would like to clarify the copyright and ownership of this job.
  The timeline control part of this system is based on M-Lab's python gateware (imported as python modules), part of M-Lab's Artiq system, which make the FPGA able to be controled by python instead of VHDL. The gateware code as well as other parts of the Artiq system are not my work and are not included here, but at M-Lab's github page <https://github.com/m-labs/artiq>. The codes published here is an upgrade, specifically design for our Lab, with several gui interfeces, easy-to-control timeline sequence, and integration with other hareware.
  And I would like to declere that all the codes published here are writen by myself except the codes in `artiq-master/other_subgui`, where portion of the contribution are made by other members of our Lab(specific recorded in the py file).
+
# Fast user guide
  This section intends to offer a basic instruction of the control system, requires zero knowledge of python. 
## before using the system
  Before using the system as well as modified it, one should bare in mind the different of "low time resolusion timeline" and "high time resolution timeline" when designing the experimental system. The word "timeline" here refers to a sequence of hardware output, and the low time resolution timeline always relays to the equipment which cannot reach a high time resolution(in this case, 10ns level). The typical representation are our DC source, RF source, etc, most of whom can only be controled through GPIB, LAN, etc. This will lead to a low time resolution, unless those hardwares allow the computer to upload the entire timeline at one singal communication. (Still, it will creat some inconvenience when cooperate with other equipments.)

  The high time resolution timeline, on the other hand, can reach to a extremely high time resolution. The only programmable hardware in our lab is the artiq-kasli FPGA. By upgrading the entire timeline(writed on python, describe the ttl output sequence regardless of the actual physical process it control), the FPGA is able to conduct the time sequence, **and the comoputer is not able to control the ttl sequence when the FPGA is outputing**(except the emergence stop)

  An example may help the reader to understand the difference. During an atomic experiment, laser sequences are used to accomplish the manipulation of the atom and its quantum state, Such as Doppler cooling, state flipping, and state detecting. 
  
  Now, if physically the duration between those steps can be a relatively long and inaccurate time, then the corresponding ttl sequence(control the laser sequence) should be wrote in different timeline file and called separately by the control system, because writing them in the same file can reach nothing except giving more burden to the hareware. The other hardwares, especially those with a low time resolution, can change their output during this break.

  If the ttl sequence(equal to high time resolution laser sequence in this case) needs to cooperate with other hareware, for example, a RF signal source, which should output a signal at a exact time during the ttl sequence. Under this circumstance, it is important to reiterate that this synchronous hardware cannot be controled by the computer because now it is now part of the high time resolution timeline. The only way to integrate it into the high time resolution timeline, is to use its trigger(if it has) and assign a ttl port from the FPGA to control it. The setting of the trigger and the parameters of the signal can be set by computer before the executing of the timeline, of course.
## start the control system 
  Click the `start.py` python file and the entire system will be lunched.

  In case of some unpredicable things happen, here I offer the specific method to start the system which is actually that py file do:
  - Open cmd, run `activate artiq-kasli`. You may need to use `cd` to change your path.
  - Run `artiq_master`. You need to set the path to where there is a folder named `repository`.
  - Open another cmd and run `activate artiq-kasli` and still you may need to use `cd` to change your path.
  - In the new cmd, run `artiq_dashboard` to open the gui provided py artiq. Although theoretically we don't need that gui, it is important when we want to test and monitor the operation of the system.
  - Open a now cmd for the third time and run `activate artiq-kasli` and still you may need to use `cd` to change your path.
  - In the third cmd, run `python main_control_gui20.py` to lunch the main control pannel.
## The main control pnnnel
  <!-- ![avatar](picture/main_control_gui.png) -->
  <div  align="center">    
  <img src="picture/main_control_gui.png" width = "500" height = "500" alt="图片名称" align=center />
  </div>

  <div  align="center">    
  <img src="https://github.com/mingshenli/artiq-kasli-SYSU-tailab/picture/main_control_gui.png" width = "500" height = "500" alt="图片名称" align=center />
  </div>
  ![image]("https://github.com/mingshenli/artiq-kasli-SYSU-tailab/picture/main_control_gui.png")

  ### basic propertise
  
  This interface is the main pannel of our control system. The most important function of this pannel is to plan the low-time-resolution hardwares' timeline. One can specify any output value of any equipment with a parameter scan mode(linear, random etc.). Different equipments can scan the output value simultaneously. This function is designed to change the harewares' output before a corresponding laser sequence.  After every move of the hareware scan the laser sequency will execute for a given loop times(1 for now), after which the hardware scan will move to next values. The laser sequence will not change, for now.

  Besides, some important hardwares' control pannel can be activated through it, for example, the DC source and the PMT. Those sub-pannel are synchronous to the hardware timeline. For example, one can disable a DC channel from the sub-pannel even if the hardware time is calling it.
    
  ### specific function of each elements
  We are going to introduce each element from top to button.

  - `activate timeline set`:lunch a sub-interface which is used to set the timeline.  
  - `activate pulse monitor`:Lunch the watch window for a PMT. 
  - `start count`:Start to rcord the data from the PMT for a given time length. The new data will follow old data. See **还没补上** for detial. 
  - `clear data`:delete all the data record by PMT.
  - `save`:Save the PMT data in the form of txt.
  - `activate DC set`:Lunch the sub-interface for the 16channel DC source. 
  - `run timeline`:Run the time line for a certain number of times with a hareware scan plan. The number of times are set by `round time` and the hareware scan plan is dertermined by several elements in main control pannel. 
  - `round time`  
  - `add`
  - `clean hardware set`
  - `update_manually`
  - list:scan mode
  - `hareware name`
  - `parameter`
  - `start value`
  - `Len`
  - `scan mode`
  - `scan time length`
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
