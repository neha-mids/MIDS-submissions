Neha Kumar MIDS W251  
Homework 11  

Training Videos:  

[Episode 0 Video](http://s3.us-east.cloud-object-storage.appdomain.cloud/hw11/episode0.mp4)  

[Episode 200 Video](http://s3.us-east.cloud-object-storage.appdomain.cloud/hw11/episode200.mp4)  
  
[Episode 380 Video](http://s3.us-east.cloud-object-storage.appdomain.cloud/hw11/episode380.mp4) 

Testing Videos:  
 
[Testing Run 30 Video](http://s3.us-east.cloud-object-storage.appdomain.cloud/hw11/testing_run30.mp4)  
  
[Testing Run 80 Video](http://s3.us-east.cloud-object-storage.appdomain.cloud/hw11/testing_run80.mp4)  

Responses to Questions:
1. I altered the number of nodes of the first and second layers as well as the epsilon_decay parameter. Increasing the size of the layers was an obvious choice to improve the model as it increases the ability of the model to produce a solution to an increasingly complex problem.
2. I increased the side of the first_layer from 16 to 32 to 64. I increased the density of the second layer from 8 to 16 to 32. I decreased the epsilon_decay to 0.95 and increased it to 0.99
3. I also played around with the number of epochs, switching it between 1 and 2. Increasing the epochs led to a longer time for training to complete, but did not necessarily translate to an improvement in the reward score among the testing samples.
4. Increasing the size of the first and second layers generally improved the model. Reducing the epsilon_decay to 0.95 made it more likely that the model will choose a step informed by the last step rather than generating a random step. However, random steps are very important in DRL. In this case, the model took longer to converge (696 episodes as opposed to 338 when epsilon_decay was set to 0.99) and had a lower average score among test samples (206 vs 235). The best run had the hyperparameters below: self.density_first_layer = 64,   self.density_second_layer = 16, self.num_epochs = 2, self.epsilon_decay = 0.995. The remaining parameters were left at their default values. The average reward was 245. This was the closest I got to having all test runs with a reward over 200 (2 runs of the 100 had rewards over 190).
5. Overall increasing num_epochs, and the density of the 2 layers would have a beneficial impact on the model though it may increase complexity and at some point the increased complexity of the model and the time to train doesn’t translate to as much of an improvement in the reward score of the test runs. The epislon_decay parameter must be optimized to ensure the training simulations have enough randomness for ample learning by the time it primarily relies upon the previous step to determine the next step. This randomness is critical because the model needs to explore many actions before finding the one that returns the most optimal q score rather than sticking with an action that simply returns an “ok” q score but was tested first. This is known as the exploration-exploitation trade-off.
6. The purpose of epsilon is to determine whether this run will use the Q function to determine the next best action, or if the simulation will generate a random action. Over time, the model is more likely to use to Q function as epsilon starts at 1.0 (translating to a random action) and decreases over time (multiplying epsilon by 0.995 each run in the default case)
7. Describe Q Learning: In q learning, the agent keeps a q-table in memory (states x actions). For each possible state, it experiments different actions and assigns a quality score. Over time the model has experimented with sufficient actions and begins exploiting what it has learned by selecting actions that maximize its q score. Note the q score takes into account the discounted estimated final reward to give immediate feedback on longer term goals.
  
Raw data for all runs (hyperparameters and training output, and number of training episodes to converge) in raw data pdf in this repo. 

 
