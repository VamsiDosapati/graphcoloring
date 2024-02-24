def graph_coloring(adjacency_map, available_colors):
    def is_safe(node, color, assignment):
        for neighbor in adjacency_map[node]:
            if neighbor in assignment and assignment[neighbor] == color:
                return False
        return True

    def backtrack(assignment, node):
        if node is None:
            return True  # All nodes are colored
        for color in available_colors:
            if is_safe(node, color, assignment):
                assignment[node] = color
                next_node = get_next_uncolored(assignment)
                if backtrack(assignment, next_node):
                    return True
                assignment[node] = None  # Backtrack
        return False

    def get_next_uncolored(assignment):
        for node in adjacency_map:
            if node not in assignment:
                return node
        return None

    assignment = {}
    start_node = list(adjacency_map.keys())[0]  # Start from the first node
    if backtrack(assignment, start_node):
        return assignment
    else:
        return None

if __name__ == "__main__":
    # Define the adjacency relationships between nodes
    adjacency_map = {
        'WA': ['ID', 'OR'],
        'ID': ['WA', 'MT', 'OR', 'NV', 'UT', 'WY'],
        'MT': ['ID', 'ND', 'SD', 'WY'],
        'ND': ['MT', 'SD', 'MN'],
        'SD': ['MT', 'ND', 'WY', 'NE', 'IA', 'MN'],
        'WY': ['ID', 'MT', 'SD', 'NE', 'CO', 'UT'],
        'NE': ['SD', 'WY', 'CO', 'KS', 'MO', 'IA'],
        'OR': ['WA', 'ID', 'CA', 'NV'],
        'NV': ['OR', 'ID', 'CA', 'AZ', 'UT'],
        'UT': ['ID', 'WY', 'CO','AZ', 'NV'],
        'CA': ['OR', 'NV', 'AZ'],
        'AZ': ['CA', 'NV', 'UT', 'NM'],
        'NM': ['AZ', 'CO', 'OK', 'TX'],
        'CO': ['WY', 'NE', 'KS', 'OK', 'NM', 'UT'],
        'KS': ['NE', 'MO', 'OK', 'CO'],
        'OK': ['KS', 'MO', 'AR', 'TX', 'NM', 'CO'],
        'TX': ['NM', 'OK', 'AR', 'LA'],
        'AR': ['MO', 'OK', 'TX', 'LA', 'MS', 'TN'],
        'LA': ['AR', 'TX', 'MS'],
        'MS': ['TN', 'AL', 'LA', 'AR'],
        'TN': ['KY', 'VA', 'NC', 'GA', 'AL', 'MS', 'AR', 'MO'],
        'AL': ['MS', 'TN', 'GA', 'FL'],
        'GA': ['AL', 'TN', 'NC', 'SC', 'FL'],
        'NC': ['VA', 'TN', 'GA', 'SC'],
        'SC': ['NC', 'GA'],
        'VA': ['MD', 'DC', 'WV', 'KY', 'NC', 'TN'],
        'WV': ['OH', 'PA', 'MD', 'VA', 'KY'],
        'MD': ['PA', 'DE', 'DC', 'VA', 'WV'],
        'DE': ['PA', 'MD', 'NJ'],
        'NJ': ['NY', 'DE', 'PA'],
        'PA': ['OH', 'WV', 'MD', 'DE', 'NJ', 'NY'],
        'OH': ['MI', 'IN', 'KY', 'WV', 'PA'],
        'MI': ['WI', 'IN', 'OH'],
        'WI': ['MN', 'IA', 'IL', 'MI'],
        'MN': ['ND', 'SD', 'IA', 'WI'],
        'IA': ['MN', 'SD', 'NE', 'MO', 'IL', 'WI'],
        'IL': ['WI', 'IA', 'MO', 'KY', 'IN'],
        'IN': ['IL', 'KY', 'OH', 'MI'],
        'KY': ['IL', 'IN', 'OH', 'WV', 'VA', 'TN', 'MO'],
        'MO': ['IA', 'IL', 'KY', 'TN', 'AR', 'OK', 'KS', 'NE'],
        'NY': ['VT', 'MA', 'CT', 'NJ', 'PA'],
        'VT': ['NH', 'MA', 'NY'],
        'NH': ['ME', 'VT', 'MA'],
        'ME': ['NH'],
        'MA': ['VT', 'NH', 'NY', 'CT', 'RI'],
        'CT': ['MA', 'NY', 'RI'],
        'RI': ['MA', 'CT'],
        'DC':['MD','VA'],
        'FL':['AL','GA']
    }

    colors = ['R', 'G', 'B', 'Y']
    node_colors = graph_coloring(adjacency_map, colors)

    if node_colors:
        print("Node   Color")
        for node, color in node_colors.items():
            print(f"{node:5} - {color}")
    else:
        print("No valid coloring found.")
