


from is_tree_graph_dict import*

def main():
    r = is_tree_graph_dict(
        {
            "a": {
                "b":{}
            },
            "b": {
                "a":{}
            }
        }
    )
    print(r == True)
    r = is_tree_graph_dict(
        {
            "a": {
                "a":""
            },
            "b": {
                "a":{}
            }
        }
    )
    print(r == False)
    r = is_tree_graph_dict(
        {
            "a": {
                "a":{}
            },
            "b": {
                "a":""
            }
        }
    )
    print(r == False)

main()
