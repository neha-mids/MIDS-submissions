
Neha Kumar  
MIDS W251  

Takeaways:  

Vocab  
- Environment: problem to be solved
- Agent: algorithm used to solve the environment (here we used DQN Agent)
- Policy: how agent acts in environment (in this case the policy produces an action, left or right, with the goal to ensure the pole does not fall over) Can have multiple policies for an agent. We have also created a random policy that performs much worse than the trained policy

Other notes:  
- The metric for evaluation is the average return. This is the sum of all the rewards at each time step, averaged over all episodes
- I am a bit puzzled how the reward is calculated. I am not sure what are the bounds of the reward, is it positive to negative infinity?
- We can see after training 20000 iterations that the trained policy is able to keep the poll upright for much longer than the random policy

