"""Module used for converting Verto heading tree data.

The Verto result object is a tuple containing NamedTuples, however this
must be converted to a dictionary to be stored in a HStoreField Postgres
database field.
"""


def convert_heading_tree_to_dict(heading_tree_tuples):
    """Convert tuple heading tree to dictionary.

    Args:
        heading_tree_tuples: The heading tree from a Verto conversion.

    Returns:
        Dictionary of heading tree, or None if None provided as tree.
    """
    if heading_tree_tuples is None:
        return None
    else:
        root_nodes = []
        for heading_node in heading_tree_tuples:
            root_nodes.append(convert_heading_node(heading_node))
        return root_nodes


def convert_heading_node(heading_node):
    """Convert a heading node to a dictionary.

    Args:
        heading_node: A tuple for a heading node.

    Returns:
        A dictionary of data for a heading node.
    """
    children = []
    for child in heading_node.children:
        children.append(convert_heading_node(child))
    heading_node_data = {
        "text": heading_node.title,
        "slug": heading_node.title_slug,
        "level": heading_node.level,
        "children": children,
    }
    return heading_node_data
