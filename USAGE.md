Once the package is installed it can be called using command:<br /> 
boids<br />
This will run the default settings of:<br /> 
count: 50<br /> 
attraction: 0.01<br /> 
alert: 100<br /> 
formation: 10000<br /> 
strength: 0.125<br /> 

It can also be called with arguments:<br />
-h or --help : displays the help for each call<br />        
--argfile "file name" : if passed a yaml file will use this to call the arguments<br /> 
--count "number of boids" : takes an interger that is the number of boids<br /> 
--attraction "strength of attraction" : takes a float that is the strenght of the attraction between the boids<br /> 
--alert "alert distance" : takes a float that is the distance at which the boids try to avoid each other<br /> 
--formation "matching distance" : takes a float that is the distance at which the boids try to match speeds<br /> 
--strength "how much the boids want to be together" : takes a float that is the strength with which the boids want to come together<br /> 
--save "do you want to save the output" : takes a bool of True or False as the wether you wish to save the animation, must have animation software to do this<br /> 
--name "file name" : takes a string which is the file name if you want to save, if this is not provided it will save as a file called 'boids_1.mp4'<br /> 

Example calls of this are:<br />
boids --count 10 --attraction 0.1 --alert 10 --save True --name boids.mp4<br /> 
boids --argfile data.yml 

