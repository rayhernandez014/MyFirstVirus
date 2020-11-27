# MyFirstVirus
This is a code that emulates the behavior of a simple virus, created with didactic purposes.

Basically, when executed, it runs a certain "malicious code" and infects every single .py file located in the same folder without affecting the "original code" written in those victims. By "infect" I mean that both the algorithm that auto-replicates the "malicious code" and the "malicious code" per se are integrated in the "original code" without affecting its original functionality, making it capable of affecting new .py files. As I said, the virus was created with didactic purposes, so in this case, what could potentially be a malicious behavior was substituted with a simple "print" function.

It's written in Python and is based in a YouTube tutorial from the channel "NeuralNine": https://youtu.be/qNy_amMuVZQ, but I added multithreading to avoid the malicious behavior to interrupt the original functionality.

This virus does not have the capability to (and was not created to) manifest a real malicious behavior, neither to be useful in a real cyberattack. This was created just to study the basic logic of a virus.
