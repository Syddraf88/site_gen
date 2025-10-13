from textnode import TextType, TextNode

def split_nodes_delimiter(Old_nodes, delimiter, TextType):
    new_nodes = []
    text_list = []
    delimited_list = []

# parse old_nodes into list of delmited entries
    for node in Old_nodes:
        node_text = node.text
        del_index = node_text.find(delimiter)
        within_delimiter = False
        while node_text != "":
            if within_delimiter is False:
                if del_index == -1:
                    #did not find delimiter, grab remainder as final node
                    temp = "".join(node_text)
                else:
                    temp = "".join(node_text[:del_index]) #take string up to but not including delimiter
                text_list.append(temp)
                print(text_list)
                print(delimited_list)
                node_text = node_text[del_index:] #after grabbing everything upto the last delimiter, recalculate node text after delimiter
                del_index = node_text[1:].find(delimiter) #exclude previous delimiter
                within_delimiter = True
            elif within_delimiter is True:
                if del_index == -1:
                    temp = "".join(node_text)
                else:
                    temp = "".join(node_text[:del_index])
                delimited_list.append(temp)
                print(text_list)
                print(delimited_list)
                node_text = node_text[del_index:]
                within_delimiter = False
                del_index = node_text[1:].find(delimiter)
                
