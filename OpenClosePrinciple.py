#OCP open for extension , closed for modifications
# when write class, shouldn't modify on it but extend it
# on top of the deign patterns is the enterprise patterns
# one popular pattern for enterprise patterns is specification

from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

#the ProductFilter calls will violates this concept
class ProductFilter:
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color: yield p

    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size: yield p

    def filter_by_size_and_color(self, products, size, color):
        for p in products:
            if p.color == color and p.size == size:
                yield p

    # state space explosion
    # 3 criteria
    # c s w cs sw cw csw = 7 methods

    # OCP = open for extension, closed for modification
    # estate space explosion

#Specification is enterprise pattern
class Specification:
    def is_satisfied(self, item):
        pass



    # and operator makes life easier
    def __and__(self, other):
        return AndSpecification(self, other)


class Filter:
    def filter(self, items, spec):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


# class AndSpecification(Specification):
#     def __init__(self, spec1, spec2):
#         self.spec2 = spec2
#         self.spec1 = spec1
#
#     def is_satisfied(self, item):
#         return self.spec1.is_satisfied(item) and \
#                self.spec2.is_satisfied(item)

class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        # print(self.args)
        return all(map(
            lambda spec: spec.is_satisfied(item), self.args))


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


apple = Product('Apple', Color.GREEN, Size.SMALL)
tree = Product('Tree', Color.GREEN, Size.LARGE)
house = Product('House', Color.BLUE, Size.LARGE)

products = [apple, tree, house]

pf = ProductFilter()
print('Green products (old):')
for p in pf.filter_by_color(products, Color.GREEN):
    print(f' - {p.name} is green')

# ^ BEFORE

# v AFTER
bf = BetterFilter()

large = SizeSpecification(size=Size.LARGE)
for p in bf.filter(products, large):
    print(f' - {p.name} is large')

green = ColorSpecification(Color.GREEN)

green_large = AndSpecification(green,large)
for p in bf.filter(products, green_large):
    print(f' - {p.name} is large and green')




                    #Enum
                #Specification (is_satisfied) generic
                #Filter   (filter) generic
                #Better Filter