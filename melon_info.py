"""
melon_info.py - Prints out all the melons in our inventory

Right now, it only tracks a melon's name, if it has seeds and 
its price.  We'll want to add the ability to keep track of
the flesh color, rind color and average weight.

"""

from melons import melon_name, melon_seedless, melon_price, melon_flesh_color, melon_rind_color, melon_weight


def print_melon(name, seedless, price):
	hashasnot = 'have'
	if seedless:
		hashasnot = 'do not have'
	
	print "%ss %s seeds and are $%0.2f" % ( name, hashasnot, price)


def melon_descrip(name, flesh, rind, weight):
	print "The %s has %s flesh and %s rind color. Its weight is %s lbs." % (name, flesh, rind, weight)
	print ""

if __name__ == '__main__':
    for i in melon_name.keys():
        print_melon(melon_name[i], melon_seedless[i], melon_price[i])
        melon_descrip(melon_name[i], melon_flesh_color[i], melon_rind_color[i], melon_weight[i])