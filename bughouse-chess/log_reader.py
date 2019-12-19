import re 

def run_through():
    count = 0

    filename = "logs/play_14/play_14_depth4_eval1_2_blackB.txt"

    r = r"Current turn branching factor: (?P<num>[0-9\.]+)"
    builder = list()
    with open(filename, "r") as f:
        for line in f:
            # if count > 30:
            #     break
            count += 1
            m = re.match(r, line)
            # print(m)
            if m:
                # print(m.group("num"))
                builder.append(m.group("num"))
                builder.append(",")

    thing = "".join(builder)
    print(thing)



if __name__ == "__main__":
    run_through()