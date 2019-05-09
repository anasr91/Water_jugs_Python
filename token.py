import main
class playz(main.emptyandfill):
    def token(self, node):
        # get the list of pairings of traveler and location
        # each of them e.g. (’goat’, ’right’)

        pairs = list(node.items())
        # sort them (arbitrarily, but fixed), so that
        # the token does not depend on arbitrary
        # dictionary order
        pairs.sort()
        # make it immutable, turn it into tuple
        return tuple(pairs)