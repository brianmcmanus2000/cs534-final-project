# Simulator details: <br/>

I used the gem5 simulator found here: https://github.com/gem5/gem5 <br/>
I am using this version of booksim: https://github.com/MEEPproject/booksim <br/>
I followed this tutorial to get gem5 working: https://github.com/gem5/gem5-resources/tree/stable/src/gpu/DNNMark <br/>
The benchmark that I ran is called fwd softmax, and it doesn't take very long to run (13.589ms of real time) <br/>


# What's in this repository:

Two important files are:<br/>
-parse_gem5_trace.py is my python script that takes the output from debug.log and produces a trace file. I had to manually identify which destinations corresponded to which source, but I think it's close enough<br/>
-project.cfg is the booksim configuration file. Because of the weirdness with this version of booksim you have to run booksim like this: ./booksim2/booksim examples/project.cfg (make sure you're in the booksim directory, not the booksim 2 directory)<br/>

In the m5out folder there are a bunch of files:<br/>
-stats.txt is a long, detailed file that has a lot of information about the results of the gem5 simulation. I've included a bunch of relevant statistics about the system in a later section that I found here.<br/>
-config.ini is a description of the system. It's also very long since this simulation includes basically all the components of a real computer (cpu, ram, storage, memory controllers, a GPU, etc.). This is also a source for configuration details<br/>
-config.system.ruby.dot.svg (or .pdf) should be a graphical representation of the configuration of the Ruby memory system, which is the part of the simulation we're mostly interested in.<br/>
-config.dot.svg (or .pdf) should be a graphical representation of the whole system. It's pretty complicated, so I don't know how useful it will be, but we can maybe use it as a jumping off point to make a similar picture with less detail<br/>


# System statistics <br/>
This simulated system is an X86 architecture. The CPU runs at 2GHz, there is only 500 Mb of ram that is addressable, although it is configured with 8Gb. The CPU has 16Mb of L3 cache, 256Kb of L2 cache, and 32 Kb of L1 Cache. The GPU is a gfx902 running at 1GHz. Throughout the simulation we recorded 3,662,552 messages.<br/>

# Other Useful Information<br/>
This link should go to a google drive folder with the trace file I generated and an image I took from a presentation that is a nice representation of our architecture (since I believe we're using the same setup) <br>
Google Drive Link: https://drive.google.com/drive/folders/1DPO8vvwNfp9LAea37TbJYsuiSpnfurqp?usp=sharing <br>
Presentation Source: https://www.gem5.org/assets/files/hpca2023-tutorial/gem5-tutorial-hpca23-gpu.pdf