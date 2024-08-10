<div align="center">
  <center><h1>NovPhy: A Physical Reasoning Benchmark for Open-world AI Systems</h1></center>
</div>

<p align="center">
Chathura Gamage<sup>*,1</sup>, Vimukthini Pinto<sup>*,1</sup>, Cheng Xue<sup>*,1</sup><br> Peng Zhang<sup>1</sup>, Ekaterina Nikonova<sup>1</sup>, Matthew Stephenson<sup>2</sup>, Jochen Renz<sup>1</sup><br>
<sup>1</sup>School of Computing<br>
The Australian National University<br>
Canberra, Australia<br>
<sup>2</sup>Maastricht University<br>
Maastricht, The Netherlands<br>
{chathura.gamage, vimukthini.inguruwattage, cheng.xue}@anu.edu.au<br>
 </p>

Due to the emergence of AI systems that interact with the physical environment, there is an increased interest in incorporating physical reasoning capabilities into those AI systems. But is it enough to only have physical reasoning capabilities to operate in a real physical environment? In the real world, we constantly face novel situations we have not encountered before. As humans, we are competent at successfully adapting to those situations. Similarly, an agent needs to have the ability to function under the impact of novelties in order to properly operate in an open-world physical environment. To facilitate the development of such AI systems, we propose a new testbed that requires an agent to reason about physical scenarios in the presence of novelties and take actions accordingly. To create tasks in the testbed, we develop novelties representing a diverse novelty space and apply them to commonly encountered five physical scenarios in a physical environment related to applying forces and motions such as rolling, falling, and sliding of objects. We evaluate the agents on their novelty detection and adaptation performance using these tasks. According to our novelty design, we measure two capabilities of an agent: the performance on a novelty when it is applied to different physical scenarios and the performance of a physical scenario when different novelties are applied to it. We conduct a thorough evaluation with human players, learning agents, and heuristic agents. Our evaluation shows that humans' performance is far beyond the agents' performance, some agents even with good normal task performance fail drastically when there is a novelty, and some agents that can adapt to novelties adapt slower than humans. We promote the development of intelligent agents capable of performing at the human level or above when operating in open-world physical environments.

\* equal contribution

Link to the published paper: [https://www.sciencedirect.com/science/article/pii/S0004370224001346#ac0010](https://doi.org/10.1016/j.artint.2024.104198)

##### Please site this article as: V. Pinto, C. Gamage, C. Xue et al., NovPhy: A Physical Reasoning Benchmark for Open-world AI Systems, Artificial Intelligence, https://doi.org/10.1016/j.artint.2024.104198


---
#### Table of contents
1. [Physical Scenarios in NovPhy](#scenarios)
2. [Novelties in NovPhy](#novelties)
3. [Novel Tasks in NovPhy](#novel-tasks)
4. [Generating Tasks](#generating-tasks)
	1. [Task Generator](#task-generator) 	
	2. [Tasks Generted for the Baseline Analysis](#tasks-generated-for-baselines)
	3. [Creating Your Own Tasks](#creating-your-own-tasks)
5. [Baseline Agents](#BAF)
	1. [How to Run Heuristic Agents](#RHA)
	2. [How to Run Learning Agents](#RLA)
		1. [How to Run DQN and Deep Relational Baselines](#RLA)
		2. [How to Run Stable Baselines](#OLA)
	4. [How to Develop Your Own Agent](#ROA)
	5. [Outline of the Agent Code](#code)
6. [Framework](#Framework)
   1. [The Game Environment](#Env)
   2. [Symbolic Representation Data Structure](#SymbolicRepresentation)
   3. [Communication Protocols](#Protocol)
7. [Evaluation Data](#EvaluationData)
---

---



## 1. Physical Scenarios in NovPhy 
<a name="scenarios"/></a>
We consider 5 physical scenarios in NovPhy testbed. Firstly, we consider the basic physical scenarios associated with applying forces directly on the target objects, i.e., the effect of a single force and the effect of multiple forces. On top of simple forces application, we also include scenarios associated with more complex motion including rolling, falling, and sliding, which are inspired by the physical reasoning capabilities developed in human infancy. The physical scenarios we consider and the corresponding physical rules that can use to achieve the goal of the associated tasks are:

   1. **Single force:** Target objects have to be destroyed with a single force.
   2. **Multiple forces:** Target objects need multiple forces to destroy.
   3. **Rolling:** Circular objects have to be rolled along a surface to a target.
   4. **Falling:** Objects have to fall onto a target.
   5. **Sliding:** Non-circular objects have to be slid along a surface to a target.


## 2. Novelties in NovPhy
<a name="novelties"/></a>
We design a representative novelty for each hierarchy level in the open-world novelty hierarchy proposed by the DARPA SAIL-ON program novelty working group. The novelty hierarchy consists of eight novelty levels that cover a wide range of novelty types that could occur in an open-world environment. The table below shows the open-world novelty hierarchy and descriptions of representative novelties in NovPhy. 

| Novelty Level             |  Description |  Representative Novelty |
|:------------------------- |------------|-----------------------|
| 1. Objects | New classes, attributes, or representations of non-volitional entities. | A new pig/block that has a different colour to the normal pigs/blocks.
| 2. Agents | New classes, attributes, or representations of volitional entities. | A novel external agent, Fan, that blows air (horizontally from left to right) affecting the moving path of objects.
| 3. Actions | New classes, attributes, or representations of external agent behavior. | The non-novel external agent, Air Turbulence, increases the magnitude of its upward force.
| 4. Interactions | New classes, attributes, or representations of dynamic properties of behaviors impacting multiple entities. | Existing circular wood object now has magnetic properties: repels objects of its type and attracts other object types.
| 5. Relations | New classes, attributes, or representations of static properties of the relationships between multiple entities. | The slingshot which is at the left side of the tasks is now at at the right side of the tasks (i.e., the spatial relationship between the slingshot and other objects are changed).
| 6. Environments | New classes, attributes, or representations of global constraints that impact all entities. | The gravity in the environment is now inverted, which affects the behaviour of the dynamic objects.
| 7. Goals | New classes, attributes, or representations of external agent objectives. | The non-novel external agent, Air Turbulence, changes its goal from pushing objects up to pushing objects down.
| 8. Events | New classes, attributes, or representations of series of state changes. | When the first bird is dead, a storm occurs that affects the motion of the objects (by applying a force to the right direction).
	
## 3. Novel Tasks in NovPhy
<a name="novel-tasks"/></a>
We created novel task templates in NovPhy by applying the above mentioned eight novelties into the tasks of the five physical scenarios. Sceenshots of the 40 task templates with novelties and their corresponding normal task templates are shown below. 


<table align="center">
        <tr>
        	<td><img src="tasks/example_tasks/images/010101_0.png" width="500"/></td>
		<td><img src="tasks/example_tasks/images/010101_1.png" width="500"/></td>
        	<td><img src="tasks/example_tasks/images/010201_0.png" width="500"/></td>
		<td><img src="tasks/example_tasks/images/010201_2.png" width="500"/></td>
        </tr>
        <tr>
        	<td colspan=2  align="center">Objects</td>
		<td colspan=2  align="center">Agents</td>
        </tr>
        <tr>
        	<td><img src="tasks/example_tasks/images/010301_0.png" width="500"/></td>
		<td><img src="tasks/example_tasks/images/010301_3.png" width="500"/></td>
        	<td><img src="tasks/example_tasks/images/010401_0.png" width="500"/></td>
		<td><img src="tasks/example_tasks/images/010401_4.png" width="500"/></td>
        </tr>
        <tr>
        	<td colspan=2  align="center">Actions</td>
		<td colspan=2  align="center">Interactions</td>
        </tr>
	        <tr>
        	<td><img src="tasks/example_tasks/images/010501_0.png" width="500"/></td>
		<td><img src="tasks/example_tasks/images/010501_5.png" width="500"/></td>
        	<td><img src="tasks/example_tasks/images/010601_0.png" width="500"/></td>
		<td><img src="tasks/example_tasks/images/010601_6.png" width="500"/></td>
        </tr>
        <tr>
		<td colspan=2  align="center">Relations</td>
		<td colspan=2  align="center">Environments</td>
        </tr>
        <tr>
        	<td><img src="tasks/example_tasks/images/010701_0.png" width="500"/></td>
		<td><img src="tasks/example_tasks/images/010701_7.png" width="500"/></td>
        	<td><img src="tasks/example_tasks/images/010801_0.png" width="500"/></td>
		<td><img src="tasks/example_tasks/images/010801_8.png" width="500"/></td>
        </tr>
        <tr>
        	<td colspan=2  align="center">Goals</td>
		<td colspan=2  align="center">Events</td>
        </tr>
	<tr>
        	<td colspan=4  align="center">Task templates of the single force scenario. In each pair, the left figure is the normal task template and the right figure is the corresponding task template with the novelty applied.</td>
        </tr>
</table>
 
<table align="center">
        <tr>
        	<td><img src="tasks/example_tasks/images/010102_0.png" width="500"/></td>
		<td><img src="tasks/example_tasks/images/010102_1.png" width="500"/></td>
        	<td><img src="tasks/example_tasks/images/010202_0.png" width="500"/></td>
		<td><img src="tasks/example_tasks/images/010202_2.png" width="500"/></td>
        </tr>
        <tr>
        	<td colspan=2  align="center">Objects</td>
		<td colspan=2  align="center">Agents</td>
        </tr>
        <tr>
        	<td><img src="tasks/example_tasks/images/010302_0.png" width="500"/></td>
		<td><img src="tasks/example_tasks/images/010302_3.png" width="500"/></td>
        	<td><img src="tasks/example_tasks/images/010402_0.png" width="500"/></td>
		<td><img src="tasks/example_tasks/images/010402_4.png" width="500"/></td>
        </tr>
        <tr>
        	<td colspan=2  align="center">Actions</td>
		<td colspan=2  align="center">Interactions</td>
        </tr>
	        <tr>
        	<td><img src="tasks/example_tasks/images/010502_0.png" width="500"/></td>
		<td><img src="tasks/example_tasks/images/010502_5.png" width="500"/></td>
        	<td><img src="tasks/example_tasks/images/010602_0.png" width="500"/></td>
		<td><img src="tasks/example_tasks/images/010602_6.png" width="500"/></td>
        </tr>
        <tr>
		<td colspan=2  align="center">Relations</td>
		<td colspan=2  align="center">Environments</td>
        </tr>
        <tr>
        	<td><img src="tasks/example_tasks/images/010702_0.png" width="500"/></td>
		<td><img src="tasks/example_tasks/images/010702_7.png" width="500"/></td>
        	<td><img src="tasks/example_tasks/images/010802_0.png" width="500"/></td>
		<td><img src="tasks/example_tasks/images/010802_8.png" width="500"/></td>
        </tr>
        <tr>
        	<td colspan=2  align="center">Goals</td>
		<td colspan=2  align="center">Events</td>
        </tr>
	<tr>
        	<td colspan=4  align="center">Task templates of the multiple forces scenario. In each pair, the left figure is the normal task template and the right figure is the corresponding task template with the novelty applied.</td>
        </tr>
</table>

<table align="center">
        <tr>
        	<td><img src="tasks/example_tasks/images/010103_0.png" width="500"/></td>
		<td><img src="tasks/example_tasks/images/010103_1.png" width="500"/></td>
        	<td><img src="tasks/example_tasks/images/010203_0.png" width="500"/></td>
		<td><img src="tasks/example_tasks/images/010203_2.png" width="500"/></td>
        </tr>
        <tr>
        	<td colspan=2  align="center">Objects</td>
		<td colspan=2  align="center">Agents</td>
        </tr>
        <tr>
        	<td><img src="tasks/example_tasks/images/010303_0.png" width="500"/></td>
		<td><img src="tasks/example_tasks/images/010303_3.png" width="500"/></td>
        	<td><img src="tasks/example_tasks/images/010403_0.png" width="500"/></td>
		<td><img src="tasks/example_tasks/images/010403_4.png" width="500"/></td>
        </tr>
        <tr>
        	<td colspan=2  align="center">Actions</td>
		<td colspan=2  align="center">Interactions</td>
        </tr>
	        <tr>
        	<td><img src="tasks/example_tasks/images/010503_0.png" width="500"/></td>
		<td><img src="tasks/example_tasks/images/010503_5.png" width="500"/></td>
        	<td><img src="tasks/example_tasks/images/010603_0.png" width="500"/></td>
		<td><img src="tasks/example_tasks/images/010603_6.png" width="500"/></td>
        </tr>
        <tr>
		<td colspan=2  align="center">Relations</td>
		<td colspan=2  align="center">Environments</td>
        </tr>
        <tr>
        	<td><img src="tasks/example_tasks/images/010703_0.png" width="500"/></td>
		<td><img src="tasks/example_tasks/images/010703_7.png" width="500"/></td>
        	<td><img src="tasks/example_tasks/images/010803_0.png" width="500"/></td>
		<td><img src="tasks/example_tasks/images/010803_8.png" width="500"/></td>
        </tr>
        <tr>
        	<td colspan=2  align="center">Goals</td>
		<td colspan=2  align="center">Events</td>
        </tr>
	<tr>
        	<td colspan=4  align="center">Task templates of the rolling scenario. In each pair, the left figure is the normal task template and the right figure is the corresponding task template with the novelty applied.</td>
        </tr>
</table>


<table align="center">
        <tr>
        	<td><img src="tasks/example_tasks/images/010104_0.png" width="500"/></td>
		<td><img src="tasks/example_tasks/images/010104_1.png" width="500"/></td>
        	<td><img src="tasks/example_tasks/images/010204_0.png" width="500"/></td>
		<td><img src="tasks/example_tasks/images/010204_2.png" width="500"/></td>
        </tr>
        <tr>
        	<td colspan=2  align="center">Objects</td>
		<td colspan=2  align="center">Agents</td>
        </tr>
        <tr>
        	<td><img src="tasks/example_tasks/images/010304_0.png" width="500"/></td>
		<td><img src="tasks/example_tasks/images/010304_3.png" width="500"/></td>
        	<td><img src="tasks/example_tasks/images/010404_0.png" width="500"/></td>
		<td><img src="tasks/example_tasks/images/010404_4.png" width="500"/></td>
        </tr>
        <tr>
        	<td colspan=2  align="center">Actions</td>
		<td colspan=2  align="center">Interactions</td>
        </tr>
	        <tr>
        	<td><img src="tasks/example_tasks/images/010504_0.png" width="500"/></td>
		<td><img src="tasks/example_tasks/images/010504_5.png" width="500"/></td>
        	<td><img src="tasks/example_tasks/images/010604_0.png" width="500"/></td>
		<td><img src="tasks/example_tasks/images/010604_6.png" width="500"/></td>
        </tr>
        <tr>
		<td colspan=2  align="center">Relations</td>
		<td colspan=2  align="center">Environments</td>
        </tr>
        <tr>
        	<td><img src="tasks/example_tasks/images/010704_0.png" width="500"/></td>
		<td><img src="tasks/example_tasks/images/010704_7.png" width="500"/></td>
        	<td><img src="tasks/example_tasks/images/010804_0.png" width="500"/></td>
		<td><img src="tasks/example_tasks/images/010804_8.png" width="500"/></td>
        </tr>
        <tr>
        	<td colspan=2  align="center">Goals</td>
		<td colspan=2  align="center">Events</td>
        </tr>
	<tr>
        	<td colspan=4  align="center">Task templates of the falling scenario. In each pair, the left figure is the normal task template and the right figure is the corresponding task template with the novelty applied.</td>
        </tr>
</table>

<table align="center">
        <tr>
        	<td><img src="tasks/example_tasks/images/010105_0.png" width="500"/></td>
		<td><img src="tasks/example_tasks/images/010105_1.png" width="500"/></td>
        	<td><img src="tasks/example_tasks/images/010205_0.png" width="500"/></td>
		<td><img src="tasks/example_tasks/images/010205_2.png" width="500"/></td>
        </tr>
        <tr>
        	<td colspan=2  align="center">Objects</td>
		<td colspan=2  align="center">Agents</td>
        </tr>
        <tr>
        	<td><img src="tasks/example_tasks/images/010305_0.png" width="500"/></td>
		<td><img src="tasks/example_tasks/images/010305_3.png" width="500"/></td>
        	<td><img src="tasks/example_tasks/images/010405_0.png" width="500"/></td>
		<td><img src="tasks/example_tasks/images/010405_4.png" width="500"/></td>
        </tr>
        <tr>
        	<td colspan=2  align="center">Actions</td>
		<td colspan=2  align="center">Interactions</td>
        </tr>
	        <tr>
        	<td><img src="tasks/example_tasks/images/010505_0.png" width="500"/></td>
		<td><img src="tasks/example_tasks/images/010505_5.png" width="500"/></td>
        	<td><img src="tasks/example_tasks/images/010605_0.png" width="500"/></td>
		<td><img src="tasks/example_tasks/images/010605_6.png" width="500"/></td>
        </tr>
        <tr>
		<td colspan=2  align="center">Relations</td>
		<td colspan=2  align="center">Environments</td>
        </tr>
        <tr>
        	<td><img src="tasks/example_tasks/images/010705_0.png" width="500"/></td>
		<td><img src="tasks/example_tasks/images/010705_7.png" width="500"/></td>
        	<td><img src="tasks/example_tasks/images/010805_0.png" width="500"/></td>
		<td><img src="tasks/example_tasks/images/010805_8.png" width="500"/></td>
        </tr>
        <tr>
        	<td colspan=2  align="center">Goals</td>
		<td colspan=2  align="center">Events</td>
        </tr>
	<tr>
        	<td colspan=4  align="center">Task templates of the sliding scenario. In each pair, the left figure is the normal task template and the right figure is the corresponding task template with the novelty applied.</td>
        </tr>
</table>


## 4. Generating Tasks<a name="generating-tasks"/></a>

### 4.1 Task Generator<a name="task-generator"/></a>

We develop a Task Generator that can generate tasks for the task templates we designed for each novelty-scenario.<br>
1. To run the Task Generator:<br>
    1. Go to ```tasks/task_generator```
    2. Copy the task templates that you want to generate tasks into the ```input``` (task templates can be found in ```tasks/task_templates```)
    3. Run the Task Generator providing the number of tasks as an argument
     ```
        python generate_tasks.py <number of tasks to generate>
     ```
    4. Generated tasks will be available in the ```output```

### 4.2 Tasks Generated for Baseline Analysis<a name="tasks-generated-for-baselines"/></a>

We generated 350 tasks from each of the 40 normal task templates and 40 novel task templates for the baseline analysis. The generated tasks can be found in ```tasks/generated_tasks.zip```. After extracting this file, the generatd tasks can be found located in the folder structure: 
<br>
&nbsp;&nbsp;&nbsp;&nbsp;generated_tasks/<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-- index of the novelty (novelty_level_i)/ <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-- index of the scenario (type_j)/ <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-- Levels/ <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-- task files of the novelty-scenario<br>

The novelty indexes i, 1 to  8 are the novelties objects, agents, actions, interactions, relations, environments, goals, and events respectively. The scenario indexes j, xxxx01 to xxxx05 are the scenarios single force, multiple forces, rolling, falling, and sliding respectively. All the tasks of the normal task templates are in the novelty_level_0 folder under corresponding type_j subfolders.  The task templates folder (```tasks/task_templates```) also follows the same naming structure. 

### 4.3 Creating Your Own Tasks<a name="creating-your-own-tasks"/></a>

If you want to design your own task templates, you can use the interactive Task Template Designer tool we have provided, which is developed in Unity.
1. To design your own task template:<br>
    1. Open the project ```tasks/task_template_designer``` in Unity
    2. Run the application in Unity Editor and load any game level
    3. While in the game level, open the Level Editor menu by navigating to the ```Level Editor -> Edit Level``` in the top-menu of the Unity editor
    4. From the Level Editor menu you can load a game level, save the level, and add any game objects to the level
    5. Design the template by adding new game objects, adjusting their positions, and resizing them as you wish
    6. After designing the task template, save the template using the ```Save Level``` button in the Level Editor menu


2. To generate tasks using your own task template
    1. Add necessary constraints according to your template into the ```tasks/task_generator/template_constraints.xlsx``` file
    2. Run the Task Generator using the instructions given in [Section 3.1](#Task-generator)
    

## 5. Baseline Agents and the Framework<a name="BAF"></a>

Tested environments:
- Ubuntu: 18.04/20.04
- Python: 3.9
- Numpy: 1.20
- torch: 1.8.1
- torchvision: 0.9.1
- lxml: 4.6.3
- tensorboard: 2.5.0
- Java: 13.0.2/13.0.7
- stable-baselines3: 1.1.0

Before running agents, please:

1. Go to ```sciencebirdsgames``` and unzip ```Linux.zip```
2. Go to ```sciencebirdslevels/generated_tasks``` and unzip ```fifth_generation.zip```

### 5.1 How to Run Heuristic Agents<a name="RHA"></a>

1. Run Java heuristic agents: Datalab and Eagle Wings: <br>

    1. Go to ```Utils``` and in terminal run
          ```
          python PrepareTestConfig.py --os [Linux/MacOS]
          ```
    2. Go to ```sciencebirdsgames/Linux```, in terminal run
          ```sh
          java -jar game_playing_interface.jar
          ```
    3. Go to ```sciencebirdsagents/HeuristicAgents/``` and in terminal run Datalab
        ```sh
        java -jar datalab_037_v4_java12.jar 1
        ```
       or Eagle Wings
          ```sh
          java -jar eaglewings_037_v3_java12.jar 1
          ```
**Note that the integer 1 in the end controls the number of agents to be running. You can set it to different integer value that suits you the best.**

2. Run *Random Agent* and *Pig Shooter*: <br>
    1. Go to ```sciencebirdsagents/```
    2. In terminal, after grant execution permission run Random Agent
       ```sh
       ./TestPythonHeuristicAgent.sh RandomAgent
       ```
       or Pig Shooter
       ```sh
       ./TestPythonHeuristicAgent.sh PigShooter
       ```

### 5.2.1 How to Run DQN and Deep Relational Baselines<a name="RLA"></a>

#### For Symbolic Agent
1. Go to ```sciencebirdsagents/Utils```
2. Open ```Parameters.py``` and set ```agent``` to be DQNDiscreteAgent and ```network``` to be DQNSymbolicDuelingFC_v2 for DQN and DQNRelationalSymbolic for Deep Relationa, and ```state_repr_type``` to be "symbolic"

#### For Image Agent
1. Go to ```sciencebirdsagents/Utils```
2. Open ```Parameters.py``` and set ```agent``` to be DQNDiscreteAgent and ```network``` to be DQNImageResNet for DQN and DQNRelationalImage for Deep Relationa and ```state_repr_type``` to be "image"


1. Go to ```sciencebirdsagents/```
2. In terminal, after grant execution permission, train the agent for within template training 
    ```sh
    ./TrainLearningAgent.sh within_template
    ```
   and for within scenatio
    ```sh
    ./TrainLearningAgent.sh benchmark
    ```
3. Models will be saved to ```sciencebirdsagents/LearningAgents/saved_model```
4. To test learning agents, go the folder ```sciencebirdsagents```:
    1. test within template performance, run
    ```
    python TestAgentOfflineWithinTemplate.py
    ```
    2. test within capability performance, run
    ```
    python TestAgentOfflineWithinCapability.py
    ```
    

### 5.2.2 How to Run Stable Baselines 3 Agents<a name="OLA"></a>

#### For Symbolic Agent
1. Go to ```sciencebirdsagents/Utils```
2. Open ```Parameters.py``` and set ```agent``` to be "ppo" or "a2c" and ```state_repr_type``` to be "symbolic"


#### For Image Agent
1. Go to ```sciencebirdsagents/Utils```
2. Open ```Parameters.py``` and set ```agent``` to be "ppo" or "a2c" and ```state_repr_type``` to be "image"


1. Go to ```sciencebirdsagents/```
2. In terminal, after grant execution permission, train the agent for within template training 
    ```sh
    ./TrainAndTestOpenAIStableBaselines.sh within_template
    ```
   and for within scenatio
    ```sh
    ./TrainAndTestOpenAIStableBaselines.sh benchmark
    ```
3. Models will be saved to ```sciencebirdsagents/OpenAIModelCheckpoints``` and tensorboard log will be saved to ```OpenAIStableBaseline```
    


### 5.3 How to Develop Your Own Agent <a name="ROA"></a>

We provide a gym-like environment. For a simple demo, which can be found at ```demo.py```

```python
from SBAgent import SBAgent
from SBEnvironment.SBEnvironmentWrapper import SBEnvironmentWrapper

# for using reward as score and 50 times faster game play
env = SBEnvironmentWrapper(reward_type="score", speed=50)
level_list = [1, 2, 3]  # level list for the agent to play
dummy_agent = SBAgent(env=env, level_list=level_list)  # initialise agent
dummy_agent.state_representation_type = 'image'  # use symbolic representation as state and headless mode
env.make(agent=dummy_agent, start_level=dummy_agent.level_list[0],
         state_representation_type=dummy_agent.state_representation_type)  # initialise the environment

s, r, is_done, info = env.reset()  # get ready for running
for level_idx in level_list:
    is_done = False
    while not is_done:
        s, r, is_done, info = env.step([-100, -100])  # agent always shoots at -100,100 as relative to the slingshot

    env.current_level = level_idx+1  # update the level list once finished the level
    if env.current_level > level_list[-1]: # end the game when all game levels in the level list are played
        break
    s, r, is_done, info = env.reload_current_level() #go to the next level
```
    
### 5.4 Outline of the Agent Code <a name="Code"></a>

The ```./sciencebirdsagents``` folder contains all the relevant source code of our agents. Below is the outline of the code (this is a
simple description. Detailed documentation in progress):

1. ```Client```:
    1. ```agent_client.py```: Includes all communication protocols.
2. ```final_run```: Place to store tensor board results.
3. ```HeuristicAgents```
    1. ```datalab_037_v4_java12.jar```: State-of-the-art java agent for Angry Birds.
    2. ```eaglewings_037_v3_java12.jar```: State-of-the-art java agent for Angry Birds.
    3. ```PigShooter.py```: Python agent that shoots at the pigs only.
    4. ```RandomAgent.py```: Random agent that choose to shoot from $x \in (-100,-10)$ and $y \in (-100,100)$.
    5. ```HeuristicAgentThread.py```: A thread wrapper to run multi-instances of heuristic agents.
4. ```LearningAgents```
    1. ```RLNetwork```: Folder includes all DQN structures that can be used as an input to ```DQNDiscreteAgent.py```.
    2. ```saved_model```: Place to save trained models.
    3. ```LearningAgent.py```: Inherited from SBAgent class, a base class to implement learning agents.
    4. ```DQNDiscreteAgent.py```: Inherited from LearningAgent, a DQN agent that has discrete action space.
    5. ```LearningAgentThread.py```: A thread wrapper to run multi-instances of learning agents.
    6. ```Memory.py```: A script that includes different types of memories. Currently, we have normal memory,
       PrioritizedReplayMemory and PrioritizedReplayMemory with balanced samples.
5. ```SBEnvironment```
    1. ```SBEnvironmentWrapper.py```: A wrapper class to provide gym-like environment.
    2. ```SBEnvironmentWrapperOpenAI.py```: A wrapper class to provide gym-like environment for OpenAI Stable Baseline 3 agents.
    3. ```Server.py```: A wrapper class for the game server for the OpenAI Stable Baseline 3 agents.
6. ```StateReader```: Folder that contains files to convert symbolic state representation to inputs to the agents.
7. ```Utils```:
    1. ```Config.py```: Config class that used to pass parameter to agents.
    2. ```GenerateCapabilityName.py```: Generate a list of names of capability for agents to train.
    3. ```GenerateTemplateName.py```: Generate a list of names of templates for agents to train.
    4. ```LevelSelection.py```: Class that includes different strategies to select levels. For example, an agent may
       choose to go to the next level if it passes the current one, or only when it has played the current level for a
       predefined number of times.
    5. ```NDSparseMatrix.py```: Class to store converted symbolic representation in a sparse matrix to save memory
       usage.
    6. ```Parameters.py```: Training/testing parameters used to pass to the agent.
    7. ```PrepareTestConfig.py```: Script to generate config file for the game console to use for testing agents only.
    8. ```trajectory_planner.py```:  It calculates two possible trajectories given a directly reachable target point. It returns None if the target is non-reachable by the bird
8. ```demo.py```: A demo to showcase how to use the framework.
9. ```SBAgent.py```: Base class for all agents.
10. ```MultiAgentTestOnly.py```: To test python heuristic agents with running multiple instances on one particular template.
11. ```TestAgentOfflineWithinCapability.py```: Using the saved models in ```LearningAgents/saved_model``` to test agent's
    within capability performance on test set.
12. ```TestAgentOfflineWithinTemplate.py```: Using the saved models in ```LearningAgents/saved_model``` to test agent's
    within template performance on test set.
13. ```TrainLearningAgent.py```: Script to train DQN baseline agents on particular template with defined mode.
14. ```TestPythonHeuristicAgent.sh```: Bash Script to test heuristic agent's performance on all templates.
15. ```TrainLearningAgent.sh```: Bash Script to train DQN baseline agents to test both local and board generalization. 
16. ```OpenAI_StableBaseline_Train.py```: Python script to run OpenAI Stable Baseline 3 agents on particular template with defined mode..
17. ```TrainAndTestOpenAIStableBaselines.sh```: Bash script to run OpenAI Stable Baseline 3 agents to test both local and board generalization.
18. 

## 6. Framework<a name="Framework"></a>

### 6.1 The Game Environment<a name="Env"></a>

1. The coordination system
    - in the science birds game, the origin point (0,0) is the bottom-left corner, and the Y coordinate increases along
      the upwards direction, otherwise the same as above.
    - Coordinates ranging from (0,0) to (640,480).

### 6.2 Symbolic Representation Data Structure<a name="SymbolicRepresentation"></a>

1. Symbolic Representation data of game objects is stored in a Json object. The json object describes an array where each element
   describes a game object. Game object categories, and their properties are described below:
    - Ground: the lowest unbreakable flat support surface
        - property: id = 'object [i]'
        - property: type = 'Ground'
        - property: yindex = [the y coordinate of the ground line]
    - Platform: Unbreakable obstacles
        - property: id = 'object [i]'
        - property: type = 'Object'
        - property: vertices = [a list of ordered 2d points that represents the polygon shape of the object]
        - property: colormap = [a list of compressed 8-bit (RRRGGGBB) colour and their percentage in the object]
    - Trajectory: the dots that represent the trajectories of the birds
        - property: id = 'object [i]'
        - property: type = 'Trajectory'
        - property: location = [a list of 2d points that represents the trajectory dots]

    - Slingshot: Unbreakable slingshot for shooting the bird
        - property: id = 'object [i]'
        - property: type = 'Slingshot'
        - property: vertices = [a list of ordered 2d points that represents the polygon shape of the object]
        - property: colormap = [a list of compressed 8-bit (RRRGGGBB) colour and their percentage in the object]
    - Red Bird:
        - property: id = 'object [i]'
        - property: type = 'Object'
        - property: vertices = [a list of ordered 2d points that represents the polygon shape of the object]
        - property: colormap = [a list of compressed 8-bit (RRRGGGBB) colour and their percentage in the object]
    - all objects below have the same representation as red bird
    - Blue Bird:
    - Yellow Bird:
    - White Bird:
    - Black Bird:
    - Small Pig:
    - Medium Pig:
    - Big Pig:
    - TNT: an explosive block
    - Wood Block: Breakable wooden blocks
    - Ice Block: Breakable ice blocks
    - Stone Block: Breakable stone blocks
   
2. Round objects are also represented as polygons with a list of vertices
3. Symbolic Representation with noise
    - If noisy Symbolic Representation is requested, the noise will be applied to each point in vertices of the game objects except
      the **ground**, **all birds** and the **slingshot**
    - The noise for 'vertices' is applied to all vertices with the same amount within 5 pixels
    - The colour map has a noise of +/- 2%.
    - The colour is the colour map compresses 24 bit RGB colour into 8 bit
        - 3 bits for Red, 3 bits for Green and 2 bits for Blue
        - the percentage of the colour that accounts for the object is followed by colour
        - example: (127, 0.5) means 50% pixels in the objects are with colour 127
    - The noise is uniformly distributed
    - We will later offer more sophisticated and adjustable noise.

### 6.3 Communication Protocols<a name="Protocol"></a>

<table style="text-align:center;">
    <thead>
        <tr>
            <th>Message ID</th>
            <th>Request</th>
            <th>Format (byte[ ])</th>
			<th>Return</th>
			<th>Format (byte[ ])</th>
        </tr>
    </thead>
    <tbody>
		<tr>
			<td>1-10</td>
			<td colspan=4>Configuration Messages</td>			
		</tr>	
		<tr>
			<td>1</td>
			<td>Configure team ID<br /> Configure running mode</td>
			<td>[1][ID][Mode]<br />ID: 4 bytes<br />Mode: 1 byte<br/>
			COMPETITION = 0<br/>TRAINING = 1</td>
			<td> Four bytes array.<br />
			The first byte indicates the round;<br />
			the second specifies the time limit in minutes;<br />
			the third specifies the number of available levels<br /></td>
			<td>[round info][time limit][available levels]<br />
			Note: in training mode, the return will be [0][0][0].<br />
			As the round info is not used in training,<br />
			the time limit will be 600 hours, <br />
			and the number of levels needs to be requested via message ID 15 
			</td>	
		</tr>	
		<tr>
			<td>2</td>
			<td>Set simulation speed<br />speed$\in$[0.0, 50.0]
			<br />Note: this command can be sent at anytime during playing to change the simulation speed</td>
			<td>[2][speed]<br />speed: 4 bytes</td>
			<td>OK/ERR</td>
			<td>[1]/[0]</td>	
		</tr>	
		<tr>
			<td>11-30</td>
			<td colspan=4>Query Messages</td>		
		</tr>
		<tr>
			<td>11</td>
			<td>Do Screenshot</td>
			<td>[11]</td>
			<td>Width, height, image bytes<br/>
			Note: this command only returns screenshots without symbolic representation </td>
			<td>[width][height][image bytes]<br />width, height: 4 bytes</td>
		</tr>
		<tr>
			<td>12</td>
			<td>Get game state</td>
			<td>[12]</td>
			<td>One byte indicates the ordinal of the state</td>
			<td>[0]: UNKNOWN<br />
			[1] : MAIN_MENU<br />
			[2]: EPISODE_MENU<br />
			[3]: LEVEL_SELECTION<br />
			[4]: LOADING<br />
			[5]: PLAYING<br />
			[6]: WON<br />
			[7]: LOST</td>
		</tr>
		<tr>
			<td>14</td>
			<td>Get the current level</td>
			<td>[14]</td>
			<td>four bytes array indicates the index of the current level</td>
			<td>[level index]
		</tr>
		<tr>
			<td>15</td>
			<td>Get the number of levels</td>
			<td>[15]</td>
			<td>four bytes array indicates the number of available levels</td>
			<td>[number of level]</td>
		</tr>
		<tr>
			<td>23</td>
			<td>Get my score</td>
			<td>[23]</td>
			<td>A 4 bytes array indicating the number of levels <br/> followed by ([number_of_levels] * 4) bytes array with every four<br/> slots indicates a best score for the corresponding level</td>
			<td>[number_of_levels][score_level_1]....[score_level_n]<br/>
			Note: This should be used carefully for the training mode, <br/>
			because there may be large amount of levels used in the training.<br/>
			Instead, when the agent is in winning state,<br/>
			use message ID 65 to get the score of a single level at winning state</td>
		</tr>
		<tr>
			<td>31-50</td>
			<td colspan=4>In-Game Action Messages</td>		
		</tr>
		<tr>
			<td>31</td>
			<td>Shoot using the Cartesian coordinates [Safe mode*]<br\>
			</td>
			<td>[31][fx][fy][dx][dy][t1][t2]<br/>
			focus_x : the x coordinate of the focus point<br/>
			focus_y: the y coordinate of the focus point<br/>
			dx: the x coordinate of the release point minus focus_x<br/>
			dy: the y coordinate of the release point minus focus_y<br/>
			t1: the release time<br/>
			t2: the gap between the release time and the tap time.<br/>
			If t1 is set to 0, the server will execute the shot immediately.<br/>
			The length of each parameter is 4 bytes</td>
			<td>OK/ERR</td>
			<td>[1]/[0]</td>
		</tr>
		<tr>
			<td>32</td>
			<td>Shoot using Polar coordinates [Safe mode*]</td>
			<td>[32][fx][fy][theta][r][t1][t2]<br/>
			theta: release angle<br/>
			r: the radial coordinate<br/>
			The length of each parameter is 4 bytes</td>
			<td>OK/ERR</td>
			<td>[1]/[0]</td>
		</tr>
		<tr>
			<td>33</td>
			<td>Sequence of shots [Safe mode*]</td>
			<td>[33][shots length][shot message ID][Params]...[shot message ID][Params]<br/>
			Maximum sequence length: 16 shots</td>
			<td>An array with each slot indicates good/bad shot.<br/>
			The bad shots are those shots that are rejected by the server</td>
			<td>For example, the server received 5 shots, and the third one<br/> 
			was not executed due to some reason, then the server will return<br/>
			[1][1][0][1][1]</td>
		</tr>
		<tr>
			<td>41</td>
			<td>Shoot using the Cartesian coordinates [Fast mode**]<br\>
			</td>
			<td>[41][fx][fy][dx][dy][t1][t2]<br/>
			The length of each parameter is 4 bytes</td>
			<td>OK/ERR</td>
			<td>[1]/[0]</td>
		</tr>
		<tr>
			<td>42</td>
			<td>Shoot using Polar coordinates [Fast mode**]</td>
			<td>[42][fx][fy][theta][r][t1][t2]<br/>
			The length of each parameter is 4 bytes</td>
			<td>OK/ERR</td>
			<td>[1]/[0]</td>
		</tr>
		<tr>
			<td>43</td>
			<td>Sequence of shots [Fast mode**]</td>
			<td>[43][shots length][shot message ID][Params]...[shot message ID][Params]<br/>
			Maximum sequence length: 16 shots</td>
			<td>An array with each slot indicates good/bad shot.<br/>
			The bad shots are those shots that are rejected by the server</td>
			<td>For example, the server received 5 shots, and the third one<br/> 
			was not executed due to some reason, then the server will return<br/>
			[1][1][0][1][1]</td>
		</tr>
		<tr>
			<td>34</td>
			<td>Fully Zoom Out</td>
			<td>[34]</td>
			<td>OK/ERR</td>
			<td>[1]/[0]</td>
		</tr>
		<tr>
			<td>35</td>
			<td>Fully Zoom In</td>
			<td>[35]</td>
			<td>OK/ERR</td>
			<td>[1]/[0]</td>
		</tr>
		<tr>
			<td>51-60</td>
			<td colspan=4>Level Selection Messages</td>		
		</tr>
		<tr>
			<td>51</td>
			<td>Load a level</td>
			<td>[51][Level]<br/>
			Level: 4 bytes</td>
			<td>OK/ERR</td>
			<td>[1]/[0]</td>
		</tr>
		<tr>
			<td>52</td>
			<td>Restart a level</td>
			<td>[52]</td>
			<td>OK/ERR</td>
			<td>[1]/[0]</td>
		</tr>
		<tr>
			<td>61-70</td>
			<td colspan=4>Science Birds Specific Messages</td>		
		</tr>
		<tr>
			<td>61</td>
			<td>Get Symbolic Representation With Screenshot</td>
			<td>[61]</td>
			<td>Symbolic Representation and corresponding screenshot</td>
			<td>[symbolic representation byte array length][Symbolic Representation bytes][image width][image height][image bytes]<br/>
			symbolic representation byte array length: 4 bytes<br/>
			image width: 4 bytes
			image height: 4 bytes</td>
		</tr>
		<tr>
			<td>62</td>
			<td>Get Symbolic Representation Without Screenshot</td>
			<td>[62]</td>
			<td>Symbolic Representation</td>
			<td>[symbolic representation byte array length][Symbolic Representation bytes]</td>
		</tr>
		<tr>
			<td>63</td>
			<td>Get Noisy Symbolic Representation With Screenshot</td>
			<td>[63]</td>
			<td>noisy Symbolic Representation and corresponding screenshot</td>
			<td>[symbolic representation byte array length][Symbolic Representation bytes][image width][image height][image bytes]</td>
		</tr>
		<tr>
			<td>64</td>
			<td>Get Noisy Symbolic Representation Without Screenshot</td>
			<td>[64]</td>
			<td>noisy Symbolic Representation</td>
			<td>[symbolic representation byte array length][Symbolic Representation bytes]</td></tr>
		<tr>
			<td>65</td>
			<td>Get Current Level Score</td>
			<td>[65]</td>
			<td>current score<br/>
			Note: this score can be requested at any time at Playing/Won/Lost state<br/>
			This is used for agents that take intermediate score seriously during training/reasoning<br/>
			To get the winning score, please make sure to execute this command when the game state is "WON"</td>
			<td>[score]<br/>
			score: 4 bytes</td>
		</tr>
		<tr>
			<td colspan=5>* Safe Mode: The server will wait until the state is static after making a shot.</td>
		</tr>
		<tr>
			<td colspan=5>** Fast mode: The server will send back a confirmation once a shot is made. 
			The server will not do any check for the appearance of the won page.</td>
		</tr>

	</tbody>

</table>

## 7. Evaluation Data 
<a name="EvaluationData"/></a>
Evaluation data folder contains three zip files. ```adaptation_data.zip```, ```detection_data.zip```, and ```human_playdata.zip```. 

### 7.1 Adpatation Data
The ```adaptation_data.zip``` contains datasets for 11 agents. Each .csv file is for a single agent and the following are the columns. 
1.	LevelIndex: The index assigned to the task 
2.	Score: The score achieved in the task
3.	LevelStatus: The Pass/Fail status of the task
4.	birdsRemaining: Number of birds remaining at the end of the task
5.	pigsRemaining: Number of pigs remaining at the end of the task
6.	birdsAtStart: Number of birds at the start of the task
7.	pigsAtStart: Number of pigs at the start of the task
8.	trial: The trial the task belongs
9.	levelName: The name of the task
10.	informed: The informed/uninformed status of the task
11.	novelty: If the task is basic/novelty 
12.	index: An index assigned to the task (Negatives for basic and postives for novel)

### 7.2 Detection Data
The ```detection_data.zip``` contains datasets two zip files ```pre_assumed_moving_average.zip``` and ```simple_moving_average.zip```. The first is the detection calculted using pre-assumed moving average and the later is the detection calculated using simple moving average. 

There are 16 .csv files under ```pre_assumed_moving_average.zip``` and 32 .csv files under ```simple_moving_average.zip``` with variations of agents, window sizes, and detection thresholds. Each .csv file is named as "agent name - window size - detection threshold". The columns of a .csv file is as follows.
1.	trial: The trial index
2.	distribution_shift: The index where distribution shift occurs
3.	detected_level: The index where agent detected novelty
4.	detection_delay: The delay in dection calculated for a trial
5.	cdt: 1/0 to indicate if agent detected novelty or not
6.	novelty_type: The name of the novelty type 

### 7.1 Human Player Data
The human player data on NovPhy is given in ```human_playdata.zip```. This includes data collected from 48 players. Each .csv file is for a player and all the columns are same as what was collected for an agent with an additional column at the end "novelty_detected" to indicate if the player detected novelty.

