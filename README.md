Simulator details:

I used the gem5 simulator found here: https://github.com/gem5/gem5
I am using this version of booksim: https://github.com/MEEPproject/booksim
I followed this tutorial to get gem5 working: https://github.com/gem5/gem5-resources/tree/stable/src/gpu/DNNMark
The benchmark that I ran is called fwd softmax, and it doesn't take very long to run (13.589ms or real time)


What's in this repository:

Two important files are:
-parse_gem5_trace.py is my python script that takes the output from debug.log and produces a trace file. I had to manually identify which destinations corresponded to which source, but I think it's close enough
-project.cfg is the booksim configuration file. Because of the weirdness with this version of booksim you have to run booksim like this: ./booksim2/booksim examples/project.cfg (make sure you're in the booksim directory, not the booksim 2 directory)

In the m5out folder there are a bunch of files:
-stats.txt is a long, detailed file that has a lot of information about the results of the gem5 simulation. I've included a bunch of relevant statistics about the system in a later section that I found here.
-config.ini is a description of the system. It's also very long since this simulation includes basically all the components of a real computer (cpu, ram, storage, memory controllers, a GPU, etc.). This is also a source for configuration details
-config.system.ruby.dot.svg (or .pdf) should be a graphical representation of the configuration of the Ruby memory system, which is the part of the simulation we're mostly interested in.  
-config.dot.svg (or .pdf) should be a graphical representation of the whole system. It's pretty complicated, so I don't know how useful it will be, but we can maybe use it as a jumping off point to make a similar picture with less detail


-System statistics: this simulated system is an X86 architecture. The CPU runs at 2GHz, there is only 500 Mb of ram that is addressable, although it is configured with 8Gb. The CPU has 16Mb of L3 cache, 256Kb of L2 cache, and 32 Kb of L1 Cache. The GPU is a gfx902 running at 1GHz. Throughout the simulation we recorded 3,662,552 messages. 