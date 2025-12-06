This research aims to design and validate a Reinforcement Learning (RL) based control strategy for VRFB that achieves several critical goals:

Overcharging and over-discharging happen when VRFB keeps operating beyond safe SOC limits, leading to heating, side reactions, imbalance, and permanent performance loss. Q-Learning prevents this by switching modes at the right time.
Heat builds up during cycling, and Q-Learning keeps the temperature safe by adjusting current and flow rate to balance heat generation and cooling. It will try to maintain a temperature near 37 degrees. 
Q-Learning minimizes resistive and activation heat while improving cooling through optimal flow control.
Q-Learning minimizes resistive and activation losses by adjusting current and flow rate, ensuring more of the current contributes to useful battery reactions
Q-Learning reduces crossover by avoiding deep SOC extremes and stabilizing cycling behavior, which slows the natural drift toward 50% SOC and preserves capacity.
