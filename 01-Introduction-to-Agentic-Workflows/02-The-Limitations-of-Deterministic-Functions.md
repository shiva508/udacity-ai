# The Limitations of Deterministic Functions
_In traditional programming, a deterministic function is one that, given a particular input, will always produce the same output. These functions operate on a predefined set of rules, often implemented through conditional logic such as if-else statements._

_Because it is **deterministic**, its output is defined by this logic._

_Consider a simple function designed to respond to user queries. If we want it to answer "What's the weather like?" or "Tell me a joke," we must program these specific cases._

* The function takes in the query, reads the prompt, and generates the output.
* It's very deterministic; you have to define each one of the cases for that input.
* If the function receives a query it hasn't been programmed for, it can only reply back with, "I cannot respond to that query; I don't have any information."