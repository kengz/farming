# Farming [![CircleCI](https://circleci.com/gh/kengz/farming.svg?style=shield)](https://circleci.com/gh/kengz/farming)
Two engineers decide to become farmers

## Motivation

People eat, so farming is fundamental. Farmers don't compute, so farming is inefficient. That's why two engineers (John and I) decide to become farmers.

We see farming as a robotics and data science problem. It helps to define it as a function that consumes inputs (resources) to yield outputs (crops). Then, this project is to optimize such a function and the related physical processes.

The optimization aims to maximize the efficiency in resources usage as well as the output. We identify the problems and solutions for each resource.

Moreover, we wish to create a "farm in a box" - so it can be better studied, optimized, and used. This is aims to democratize farming.


## Resources - Problems and Solutions

### Land

**Problem:** Traditional farming is very 2 dimensional, and it takes up a lot of space. This poses a lot of limitations.

1. It limits how much you can farm. Land costs money, so that limits the area you can buy. Larger area is also hard to maintain as it is harder to cover it with tractors, piping, sprinklers etc.
2. It limits where you can farm. Typically it is where land is cheap, and that is far from urban areas. It is also not trivial to find a suitable terrain. The location also adds transportation costs and limits access to infrastructure.

**Solution:** Make farming 3 dimensional by using a deckered system and solve all the problems above. Each additional deck increases the efficiency of space usage by a factor, and enables farming closer to urban areas. Compactness also make the application of technology and infrastructure affordable. This is no news to hydroponic farming.


### Soil

**Problem:** Although soil is not a scarce resource, 2 dimensional farming utilizes only the top layer of the exposed soil, and the bottom layer is wasted. Suitable type of soil is needed for farming, and that limits where you can farm. After a farming cycle, the soil needs to be refertilized, and that is a very laborious task.

**Solution:** Extract the soil and spread it on a deckered system to the suitable depth, compactness, etc. We can also engineer the soil content as wanted. Soil is already seen as a commodity as they are already available for purchase. With the use of a deckered system, we can recycle un-fertilized soil or just switch it out very easily.


### Fertilizers, Pest and Weed Control

**Problem:** These are applied over a general area, therefore lacks accuracy and efficiency. It is laborious. There is little targetedness, and although there is portion and timing control done by human guess work or by experience, it is not closely monitored or optimized.

**Solution:** A compact deckered system makes it feasible for machine to perform these tasks and replace human labor. An automated monitoring system will monitor the effects of application, then learn and optimize it over time. The system will also do targeting to increase specificity and reduce waste.


### Water

**Problem:** Farming uses a lot of water. This faces a similar problem as above.

**Solution:** Same solution as above.


### Climate control

**Problem:** The same problem as what a greenhouse solves.

**Solution:** A smaller area means easiness to control the climate. This will be a deckered system inside a greenhouse, although it is optional by crop.


### Seeds

**Problem:** For small scale farming, seeds need to be ensured healthy. Typically this is done by human labor.

**Solution:** A machine can learn to pick and use only the healthy seeds.


### Farm in a box

If we can compactify and optimize farming as described above, we can pack it into a box, and make the system trivial to use. With the ease of distribution and usage, everyone can farm.

Note that the limits discussed above would also be radically reduced. Coupled with a robotics system, the farm in a box can scale to resemble a factory.


## Design

**Language:** Python for data science and most backend; whatever Arduino or the robotics system need; Nodejs for server and interface?

We divide the project into 3 main components.

### Data Science component

Starting with data, we need to define the observable variables and their possible relevance to the farming function. Then, we can collect, analyze, act on, and feedback from the information. 

The data will also determine what algorithms and optimizations we can perform. Only then can we start to define the farming function that optimizes. inputs to outputs.


#### v1

**Candidate data**

|variable|details|
|:--|:--|
|land dimensions|Spatial measurements including area, depth, spacing|
|soil dimensions|Measurements of soil type v.s. seed type, soil depth, weight, compactness|
|water usage|how much water v.s. soil, seed type, frequency, weight, target area size of application|
|plan growth|measurement of the output, i.e. how well is the farming function|
|yield weight|measurement of quality of output|

version 1 is simple, that is to define, collect and analyze data before any actions. The farming function for version 1 is defined as taking the variables, figuring out the manipulation of the input variables, and how that affects outputs. It is also data-building before we can go far.


### Robotics component

Robotics bridges the real world environment with the data science component. It encompasses the sensors for data collection, and robotic arms for actions (later versions).

#### v1

For the data above we need the corresponding sensors:

*needs to be expanded

|sensor|details|
|:--|:--|
|water sensor|visual inspection of the status of crop|
|camera|visual inspection of the status of crop|


### Farming component

This is the good ol' farming part, that involves the resources listed above.

#### v1

We stand with common crops:

|crop|details|
|:--|:--|
|potatoes|yums|
|tomatoes|yums|



## Installation and Setup

*What to get, how to setup from scratch.*

## Run

*The scientific procedure, the farming function. The strategy for iterations and improvements.*


## Roadmap

### v1.0 (current)

- data definition, collection, analyses
- set up simple robotics sensors
- set up simple farming component
- no actions yet

### v1.1

- select useful data variables, repeat v1.0 till data is good
- expand data set
- no actions yet
