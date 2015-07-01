"""
Cookie Clicker Simulator
"""

import simpleplot
import math
# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(50)

import poc_clicker_provided as provided

# Constants
SIM_TIME = 10000000000.0
#SIM_TIME = 10


class ClickerState:
    """
    Simple class to keep track of the game state.
    """

    def __init__(self):
        """
        total_cookies- The total number of cookies produced throughout the entire game
        current_cookies- The current number of cookies you have
        current_time- The current time (in seconds) of the game
        cps- The current CPS
        history_list- History list would be a list of tuples of the form:
                      (time, item, cost of item, total cookies)
        """
        self.total_cookies = 0.0
        self.current_cookies = 0.0
        self.current_time = 0.0
        self.cps = 1.0
        self.history_list = [(0.0, None, 0.0, 0.0)]

    def __str__(self):
        """
        Return human readable state
        """
        statement = "\nCurrent State\n"
        statement += "------------------------\n"

        statement += "Time:\t\t " + str(self.get_time())
        statement += "\nCurrent Cookies: " + str(self.get_cookies())
        statement += "\nCPS:\t\t " + str(self.get_cps())
        statement += "\nTotal Cookies:\t " + str(self.get_total_cookies())

        return statement

    def get_total_cookies(self):
        """
        Return total number of cookies

        Should return a float
        """
        return self.total_cookies

    def get_cookies(self):
        """
        Return current number of cookies
        (not total number of cookies)

        Should return a float
        """
        return self.current_cookies

    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self.cps

    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self.current_time

    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: [(0.0, None, 0.0, 0.0)]

        Should return a copy of any internal data structures,
        so that they will not be modified outside of the class.
        """
        return list(self.history_list)

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0.0 if you already have enough cookies)

        Should return a float with no fractional part
        """

        if self.get_cookies() >= cookies:
            return 0.0
        else:
            return math.ceil((cookies - self.get_cookies())/self.get_cps())



    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0.0
        """
        if time > 0.0:
            self.current_cookies += self.get_cps() * time
            self.total_cookies += self.get_cps() * time
            self.current_time += time
        else:
            return


    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """

        if cost <= self.get_cookies():
            self.history_list.append((self.get_time(), item_name, cost, self.get_total_cookies()))
            self.cps += additional_cps
            self.current_cookies -= cost
        else:
            return


def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """
    #print 'inside simulate_clicker'
    #print 'duration - ', duration

    build_info_clone = build_info.clone()
    state = ClickerState()

    while(state.get_time() <= duration):
        #print
        #print 'inside loop'
        # Check the current time and break out of the loop if the duration
        # has been passed.

        #print 'current_time - ', state.get_time()
        if state.get_time() > duration:
            break

        #print 'state before strategy function...'
        #print state
        #print 'calling strategy function'

        # Call the strategy function with the appropriate arguments to
        # determine which item to purchase next. If the strategy function
        # returns None, you should break out of the loop, as that means
        # no more items will be purchased.

        time_left = duration - state.get_time()

        item_to_buy = strategy(state.get_cookies(), state.get_cps(),
                                    state.get_history(), time_left,
                                    build_info_clone)

        #print 'item_to_buy- ', item_to_buy

        # End the simulation if strategy returned None
        if item_to_buy == None:
            #print 'nothing to buy'
            break

        # Get the cost of the item to purchase
        item_cost = build_info_clone.get_cost(item_to_buy)

        #print 'item_cost- ', item_cost
        # Determine how much time must elapse until it is possible to
        # purchase the item. If you would have to wait past the duration of
        # the simulation to purchase the item, you should end the simulation.
        time_to_wait = state.time_until(item_cost)

        #print 'time_to_wait- ', time_to_wait

        if time_to_wait > time_left:
            # Don't have enough time left. End the simulation
            break

        # Wait for time_to_wait
        state.wait(time_to_wait)

        # Purchase the item
        state.buy_item(item_to_buy, item_cost,
                        build_info_clone.get_cps(item_to_buy))

        # Update the build information.
        build_info_clone.update_item(item_to_buy)
        #print 'state after purchase function...'
        #print state

    #print 'outside loop'

    # Account for the premature termination of the loop
    # with some time still remaining

    if state.get_time() <= duration:
        time_left = duration - state.get_time()
        #print 'still there is time left - ', time_left
        #print 'utilizing that time....'
        state.current_cookies += state.get_cps() * time_left
        state.total_cookies += state.get_cps() * time_left
        state.current_time += time_left

    #print state.get_time()
    #print duration

    #print state.get_history()
    #print
    return state



def strategy_cursor_broken(cookies, cps, history, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic (and broken) strategy does not properly
    check whether it can actually buy a Cursor in the time left.  Your
    simulate_clicker function must be able to deal with such broken
    strategies.  Further, your strategy functions must correctly check
    if you can buy the item in the time left and return None if you
    can't.
    """
    return "Cursor"

def strategy_none(cookies, cps, history, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that will never buy anything, but
    that you can use to help debug your simulate_clicker function.
    """
    return None

def strategy_cheap(cookies, cps, history, time_left, build_info):
    """
    Always buy the cheapest item you can afford in the time left.
    """
    #print 'inside strategy_cheap'

    #print 'cookies- ', cookies
    #print 'cps- ', cps
    #print 'history- ', history
    #print 'time_left- ', time_left
    #print 'build_info- ', build_info
    #print
    item_list = build_info.build_items()
    #print item_list
    cost_list = [build_info.get_cost(item) for item in item_list]
    #print cost_list

    # unable to create dictionary with list comprehension :(
    #items = { item: build_info.get_cost(item) for item in build_info.build_items() }

    # manually create the dictionary of items
    items = {}
    count = 0

    for cost in cost_list:
        items[cost] = item_list[count]
        count += 1

    #print 'items- '
    #print items


    cookies_available = cookies + cps * time_left
    affordable_item_costs = [cost for cost in items if cost <= cookies_available]
     #print 'affordable_item_costs- ',affordable_item_costs
    if len(affordable_item_costs) > 0:
        min_cost = min(affordable_item_costs)
        item = items[min_cost]
        #print 'min_cost- ', min_cost
        #print 'chosen item- ', item
        return item
    else:
        return None


def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    #print 'inside strategy_expensive'

    #print 'cookies- ', cookies
    #print 'cps- ', cps
    #print 'history- ', history
    #print 'time_left- ', time_left
    #print
    item_list = build_info.build_items()
    #print item_list
    cost_list = [build_info.get_cost(item) for item in build_info.build_items()]
    #print cost_list

    # unable to create dictionary with list comprehension :(
    #items = { item: build_info.get_cost(item) for item in build_info.build_items() }

    # manually create the dictionary of items
    items = {}
    count = 0

    for cost in cost_list:
        items[cost] = item_list[count]
        count += 1

    #print 'items- '
    #print items

    cookies_available = cookies + cps * time_left
    affordable_item_costs = [cost for cost in items if cost <= cookies_available]

    if len(affordable_item_costs) > 0:
        max_cost = max(affordable_item_costs)
        item = items[max_cost]
        #print 'affordable_item_costs- ',affordable_item_costs
        #print 'max_cost- ', max_cost
        #print 'chosen item- ', item
        return item
    else:
        return None

def strategy_best(cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    """
    #print 'inside strategy_best'

    #print 'cookies- ', cookies
    #print 'cps- ', cps
    #print 'history- ', history
    #print 'time_left- ', time_left
    #print
    item_list = build_info.build_items()
    #print item_list
    cost_list = [build_info.get_cost(item) for item in build_info.build_items()]
    #print cost_list

    # unable to create dictionary with list comprehension :(
    #items = { item: build_info.get_cost(item) for item in build_info.build_items() }

    # manually create the dictionary of items
    items = {}
    count = 0

    for cost in cost_list:
        items[cost] = item_list[count]
        count += 1

    #print 'items- '
    #print items


    affordable_item_costs = [cost for cost in items.keys() if cost < time_left]

    if len(affordable_item_costs) > 0:

        total = 0.0

        for cost in affordable_item_costs:
            total += cost

        avg_cost = total/len(affordable_item_costs)

        min_diff = avg_cost
        best_cost = 0.0

        for cost in items.keys():
            diff = abs(cost - avg_cost)
            if diff < min_diff:
                min_diff = diff
                best_cost = cost

        item = items[best_cost]
        #print 'affordable_item_costs- ',affordable_item_costs
        #print 'min_cost- ', min_cost
        #print 'chosen item- ', item
        return item
    else:
        return None

def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation for the given time with one strategy.
    """
    #print 'running the simulation.........'
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    #print 'finished running the simulation.....'
    print strategy_name, ":", state

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    history = state.get_history()
    #print history
    history = [(item[0], item[3]) for item in history]
    simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)

def run():
    """
    Run the simulator.
    """
    run_strategy("Cursor", SIM_TIME, strategy_cursor_broken)

    # Add calls to run_strategy to run additional strategies
    print
    run_strategy("Cheap", SIM_TIME, strategy_cheap)
    print
    run_strategy("Expensive", SIM_TIME, strategy_expensive)
    print
    run_strategy("Best", SIM_TIME, strategy_best)

run()

def test():
    state = ClickerState()
    print state
    print
    print 'time until 10 cookies- ', state.time_until(10), ' seconds'
    print
    print 'waiting 20 seconds......'
    state.wait(20)
    print state
    print
    print 'buying a grandma........'
    state.buy_item('grandma', 15, 5)
    print state
    print
    print 'history- ', state.get_history()
    print
    print 'time until 17 cookies- ', state.time_until(17), ' seconds'

def test2():

    #print strategy_cheap(500000.0, 1.0, [(0.0, None, 0.0, 0.0)], 5.0, provided.BuildInfo({'A': [5.0, 1.0], 'C': [50000.0, 3.0], 'B': [500.0, 2.0]}, 1.15))
    #print strategy_cheap(3.0, 100.0, [(0.0, None, 0.0, 0.0)], 600.0, provided.BuildInfo({'A': [5.0, 1.0], 'C': [50000.0, 3.0], 'B': [500.0, 2.0]}, 1.15))
    #print strategy_expensive(1.0, 3.0, [(0.0, None, 0.0, 0.0)], 17.0, provided.BuildInfo({'A': [5.0, 1.0], 'C': [50000.0, 3.0], 'B': [500.0, 2.0]}, 1.15))
    obj = ClickerState()
    print obj
    print 'waiting 78 sec'
    obj.wait(78.0)
    print obj
    print "buying ('item', 1.0, 1.0)"

    obj.buy_item('item', 1.0, 1.0)
    print obj
    print obj.time_until(22.0)
    print obj

#test2()

#test()
