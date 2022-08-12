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

const bfsConnectedComponent = (start) => {
  let explored = []
  let queue = [start]

  while (queue) {
    const node = queue.shift()
    explored.push(node)
    node.neighbors.forEach(neighbor => {
      if (!explored.includes(explored)) {
        queue.push(neighbor)
      }
    })
  }
  return explored
}

console.log(bfsConnectedComponent(nodeA))
