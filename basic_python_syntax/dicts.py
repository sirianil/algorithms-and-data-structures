def setup_map():
    capitals = {}
    capitals["india"] = "new delhi"
    capitals["usa"] = "washington dc"
    capitals["california"] = "saratoga"

    if "india" in capitals:
        print("capital of india is ", capitals["india"])
    
    for [place, capital] in capitals:
        print("Capital of ", place ," is ", capital)

def main():
    setup_map()

if __name__ == '__main__':
    main()