# Poker Game

## Instructions

*To run* `python3 game.py`

## Testing

*Scenario 1:* User is prompted to place a bet and has an incorrect input (eg. input a word instead of number), the code will then throw a **ValueError** which will inform the user: *That is not a valid input, please input a number* and restart the program. 

*Scenario 2:* User is prompted to enter the number corresponding to the action they want to take (eg. 1 for Hit, etc.). and the user then inputs "Hit" instead of "1". This will throw a **ValueError** which will inform the user: *That is not a valid input, please input a number* and prompt the question again. 

*Scenario 3:* While calculating the value of the cards held by the user, the user is prompted to: *What is the value you wish to set for A in this instance ?*. An incorrect input (eg. "3" v/s "1") would throw a **ValueError** which will inform the user: *That is not a valid input, please input a number* and prompt the question again. 

*Scenario 4:* When the user tries to split pairs, for the cases of them having already split before (by design we only allow one split on the initial 2 cards), or if the user tries to split 2 unequal cards or at any point after they've already hit the cards, a **RuntimeError** would be thrown and the user will be informed of all 3 cases. 

**Module Testing:** All functions tested independently. 

## Rational 

### Design Decisions 

#### Language
I initially considered using Java for this project. But as I began development, I quickly discarded this idea, since the development time with Java would be far higher for no tangible gain, than Python. Based on prior experience with both languages, I could also identify tertiary development painpoints like installing external libraries, that a good package manager like *pip* handles very easily for Python but the Java equivalents could still require a bit of work. 

Thus, the development time cost both due to language design (you can do very powerful array manipulation in Python incredibly easily unlike Java) and tertiary development costs, factored into this decision. 

#### Data Structures
The primary data structure powering the game are *lists*. The decision to use these was made based on several key factors: 
1) The ability to access randomly generated values - O(1) access time
2) The ability to add easily - O(1) worst case

However, there is the concern about the cost of an O(n) remove cost for every time we remove from the deck and give the card to either the player or the dealer. However, since this is a known cost of 52, this can also be considered to be O(1). 
