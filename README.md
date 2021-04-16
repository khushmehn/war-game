# war-game

3 scenarios:

First Battle of Panipat: Babur VS Ibrahim Lodi
Babur's attacks:
Artillary: 30 point damage to opponent
Flank attack: 40 point damage to opponent
Cannon: 20 point damage to opponent
Lodi's attacks:
Artillary: 40 point damage to opponent
Onward March: 20 point damage to opponent
Cannon: 30 point damage to opponent
Cold War: Russia VS USA
Russia's attacks:
Proxy: 25 point damage to opponent
Nuclear Bomb: 50 point damage to opponent
Blockade: 20 point damage to opponent
USA's attacks:
Embargo: 25 point damage to opponent
Nuclear Bomb: 50 point damage to opponent
Proxy: 20 point damage to opponent
North Korea VS South Korea
North Korea's attacks:
Conventional attack: 35 point damage to opponent
Nuclear Bomb: 50 point damage to opponent
Propaganda: 10 point damage to opponent
South Korea's attacks:
Conventional Attack: 45 point damage to opponent
Call for US intervention: 60 point damage to opponent
Blocade: 10 point damage to opponent
In each of these scenarios, each of the two participants has an initial score of 100. Any of the two participants can surrender at any of their own turns

Imagine this to be a two person game where two people choose which of the 3 war game scenarios they want to participate in. They are then given a side each randomly, and take turns one by one. In these turns they get moves according to the moves allotted in the description above. Each of the moves has a corresponding damage value to it.

Your code should present the choice of 3 scenarios and ask the players to choose their scenario. It should then assign sides and commence the war game scenario by showing the attack options which are available (and the surrender option). At the end of each round (when both turns are done), it should show the current score.

The rounds should when either party has surrendered or when either party's score is negative. It should then present the winner, and then ask the participants if they want to end the game (i.e. exit) or choose a different war game scenario. If they choose a different war game scenario, the game should restart with that new war game scenario and go on.
Hint: You might want to use lists or list of lists to associate attacks with scores (instead of hard coding them). Also try and write code for one war game scenario and then see how can generalize it for 3 different war game scenarios without repeating any code.

Note: Your code should be user friendly and any print statements referring to the players during the war game should refer to the names in the scenario itself; for example, "Babur, your score is...X" or "Lodi", or "North Korea" or "South Korea"
