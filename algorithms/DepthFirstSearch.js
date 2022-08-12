class Node {
  constructor(value) {
    this.value = value
    this.neighbors = []
    this.path = []
  }
}

// initialize the graph
const nodeA = new Node('A')
const nodeB = new Node('B')
const nodeC = new Node('C')
const nodeD = new Node('D')
const nodeE = new Node('E')
const nodeF = new Node('F')
const nodeG = new Node('G')
nodeA.neighbors = [nodeB, nodeC, nodeE]
nodeB.neighbors = [nodeA, nodeD, nodeE]
nodeC.neighbors = [nodeA, nodeF, nodeG]
nodeD.neighbors = [nodeB]
nodeE.neighbors = [nodeA, nodeB, nodeD]
nodeF.neighbors = [nodeC]
nodeG.neighbors = [nodeC]

let visitedNodes = []

const dfs = (start, target, path = []) => {
  if (visitedNodes.includes(start)) {
    return null
  } else {
    visitedNodes.push(start)
  }

  path.push(start)
  start.path = path

  console.log("Visiting Node " + start.value)
  if (start.value == target) {
    console.log(`Found the node we're looking for, node ${target}`)
    return start.path
  }

  for (let i = 0; i < start.neighbors.length; i++) {
    const result = dfs(start.neighbors[i], target, start.path)
    if (result != null) {
      return result
    }
  }

  console.log("Went through all neighbors of " + start.value + ", returning to it's parent.");
  return null;
}

console.log(dfs(nodeG, "B"))
