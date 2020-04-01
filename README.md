
## RyanairMultipleDeparturesArrivals



Get all the ticket fares in a date range for multiple departure and arrival airports.

Imagine a scenario where you have some airports at similar distances to you and you wanna flight to a place also with similar distances to many airports. Let's consider an example where you have 3 possible airports for departure and 3 for arrival, you have 3x3=9 possibilities to check. And when are you going to travel? Consider that you can travel between Friday and Monday, you don't care when, you just want the cheapest ticket. There are too many cases too compare, **3x3x4=36** (3 departures airports * 3 arrival airports * 4 possible travelling days). 36 is a lot!

How this works? Just insert the  [IATA](https://en.wikipedia.org/wiki/List_of_Ryanair_destinations)  codes for the departure and arrival airports, the date from which you want to travel and the range days you can travel. It will give you a file with all the possibilities you have, ordered by the price.

I am not responsible for any use of this code by third parties, regardless of the purpose.


André Rodrigues
December, 2017
