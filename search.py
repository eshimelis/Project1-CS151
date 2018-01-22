# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """

    # create/initiate fringe and empty set
    fringe = util.Stack()
    fringe.push(problem.getStartState())

    explored = []

    directions = util.Stack()
    directions.push([])

    while True:

        if fringe.isEmpty():
            raise ValueError('Failure: fringe is empty.')

        currentState = fringe.pop()
        currentInstructions = directions.pop()

        if problem.isGoalState(currentState):
            return currentInstructions

        if currentState not in explored:
            explored.append(currentState)

            for successorState in problem.getSuccessors(currentState):
                if successorState not in explored:
                    fringe.push(successorState[0])
                    directions.push(currentInstructions + [successorState[1]])

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""

    # create/initiate frontier and empty set
    explored = []

    frontier = util.Queue()
    frontier.push([problem.getStartState(), [], 0])

    while True:

        if frontier.isEmpty():
            raise ValueError('Failure: fringe is empty.')

        node = frontier.pop()

        currentPosition = node[0]
        currentAction = node[1]
        stepCost = node[2]

        if problem.isGoalState(currentPosition):
            return currentAction

        if currentPosition not in explored:
            explored.append(currentPosition)

            # sort successors by cost function
            successors = problem.getSuccessors(currentPosition)
            successors.sort(key = lambda state: state[2])

            for successorState in successors:
                if successorState[0] not in explored:
                    state = successorState[0]
                    actions = currentAction + [successorState[1]]
                    cost = stepCost + successorState[2]

                    frontier.push([state, actions, cost])
                    # directions.push(currentInstructions + [successorState[1]])
                    # cost.push(stepCost + successorState[2])

def uniformCostSearch(problem):
    """Search the node of least total cost first."""

    # create/initiate fringe and empty set
    explored = []

    frontier = util.PriorityQueue()
    frontier.push(problem.getStartState(), 0)

    path = {}
    cost = {}

    while True:

        if frontier.isEmpty():
            raise ValueError('Failure: fringe is empty.')

        currentState = frontier.pop()

        if currentState in path.keys():
            currentPathCost = cost[currentState]
            currentPath = path[currentState]
        else:
            currentPathCost = 0
            currentPath = []

        if problem.isGoalState(currentState):
            print 'Frontier: ', frontier
            print 'Path Cost: ', currentPathCost
            return currentPath

        if currentState not in explored:
            explored.append(currentState)

        for successorState in problem.getSuccessors(currentState):

            [successor, action, stepCost] = successorState
            priority = currentPathCost + stepCost

            if successorState not in explored:
                frontier.push(successor, priority)

                # update action and cost
                path[successor] = currentPath + [action]
                cost[successor] = priority
            else:
                frontier.update(successor, priority)

                # update action and cost
                path[successor] = currentPath + [action]
                cost[successor] = priority



def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
