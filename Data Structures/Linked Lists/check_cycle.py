def check_cycle(lista):
    links = set()
    walk = lista.first

    while walk is not None:
        if walk in links:  # If node is already visited, cycle detected
            print("Cycle detected")
            return True
        
        links.add(walk)  # Store visited nodes
        walk = walk.next

    print("No Cycle")
    return False
