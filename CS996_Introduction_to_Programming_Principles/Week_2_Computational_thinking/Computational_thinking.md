# Computational thinking

## Exercise

Design a computer program that describes the process of making a cup of tea with hot water and milk. The program should start with an empty kettle and a cup. The program should end with a cup that contains hot tea that is ready to drink.

Follow the example that is given in Section 2 and create a solution that includes steps, options, a flowchart and pseudocode. Use https://app.diagrams.net/ to create the flowchart.

## Solution

### Steps

* Fill the kettle with water
* Boil the water in the kettle
* Place a tea bag in the mug
* Choose whether to add milk or hot water first
    * If the user chooses to add the milk first then add that then the hot water
    * If the user chooses to add the hot water first then add that then the milk
* Steep the tea
* Remove the tea bag
* Add milk to the tea
* Stir the tea
* Cool down

### Options

* choice of mug
* amount of water to boil
* the amount of water to put in the mug
* the variety of tea bag to put in the mug
* how long to allow the tea bag to steep
* to squeeze the bag

### Flowchart

### Pseudocode

INPUT WaterNeeded
INPUT SteepingTimeNeeded
INPUT MilkAmount
INPUT AddMilkFirst  # Boolean to decide whether to add milk first or after water

FillKettle ()
WaterInKettle ← 0

WHILE WaterInKettle < WaterNeeded DO
    FillWithWater ()
    WaterInKettle ← WaterInKettle + 100  # Increment by 100 ml each time
ENDWHILE

BoilWater (WaterInKettle)

PlaceTeaBag ()

IF AddMilkFirst THEN
    AddMilk (MilkAmount)
END IF

PourWater (WaterInKettle)

IF NOT AddMilkFirst THEN
    AddMilk (MilkAmount)
END IF

SteepingTime ← 0

WHILE SteepingTime < SteepingTimeNeeded DO
    SteepTea ()
    SteepingTime ← SteepingTime + 1  # Increment by 1 minute each time
ENDWHILE

RemoveTeaBag ()
StirTea ()

TeaIsTooHot ← TRUE

WHILE TeaIsTooHot DO
    WaitToCool ()
    TeaIsTooHot ← CheckTemperature ()
ENDWHILE

TeaIsReady ← TRUE