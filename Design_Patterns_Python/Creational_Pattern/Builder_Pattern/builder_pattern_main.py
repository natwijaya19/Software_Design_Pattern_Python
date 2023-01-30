from builder_pattern1 import Director, ConcreteBuilder1

if __name__ == "__main__":
    """
    The client code creates a builder_instance object, passes it to the director and then
    initiates the construction process. The end result is retrieved from the
    builder_instance object.
    """
    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    print("Standard basic product")
    director.build_minimal_viable_product()
    builder.product.list_parts()

    print("\n")

    print("standard full featured product")
    director.build_full_featured_product()
    builder.product.list_parts()

    print("\n")

    # Remember, the Builder pattern can be used without a Director class.
    print("custom product")
    builder.produce_part_a()
    builder.produce_part_b()
    builder.product.list_parts()
