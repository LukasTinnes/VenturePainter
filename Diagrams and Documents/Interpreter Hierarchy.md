Interpreter gets a collection of Objects. It then builds a directional Graph from the root up, depending on 3 Cases.

Case 1: Object A and B do not share any Points. There is no path between each of the Nodes

Case 2: Object A and B are adjacent to one another. There is a path from A to B and from B to A.

Case 3: Object A lies in Object B. There is a path from B to A.
