import networkx as nx
from networkx.algorithms.community import greedy_modularity_communities

def create_social_network():
    """Membuat graf jaringan sosial dengan node dan edge."""
    G = nx.Graph()

    ## DATA 1
    # # node (pengguna)
    # G.add_nodes_from(["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah"])
    
    # # edge (hubungan antara pengguna)
    # G.add_edges_from([
    #     ("Alice", "Bob"), ("Alice", "Charlie"), ("Bob", "David"),
    #     ("Charlie", "David"), ("Eve", "Frank"), ("Frank", "Grace"),
    #     ("Grace", "Hannah"), ("Alice", "Eve")
    # ])

    ## DATA 2
    # Menambahkan 30 nodes
    nodes = [
        "Node1", "Node2", "Node3", "Node4", "Node5", "Node6", "Node7", "Node8", "Node9", "Node10",
        "Node11", "Node12", "Node13", "Node14", "Node15", "Node16", "Node17", "Node18", "Node19", "Node20",
        "Node21", "Node22", "Node23", "Node24", "Node25", "Node26", "Node27", "Node28", "Node29", "Node30"
    ]
    G.add_nodes_from(nodes)

    # Menambahkan edges (hubungan antar pengguna)
    edges = [
        ("Node1", "Node2"), ("Node1", "Node3"), ("Node2", "Node4"), ("Node3", "Node4"),
        ("Node5", "Node6"), ("Node6", "Node7"), ("Node7", "Node8"), ("Node1", "Node5"),
        ("Node9", "Node10"), ("Node10", "Node11"), ("Node11", "Node12"), ("Node12", "Node13"),
        ("Node13", "Node14"), ("Node14", "Node15"), ("Node9", "Node15"), ("Node16", "Node17"),
        ("Node17", "Node18"), ("Node18", "Node19"), ("Node19", "Node20"), ("Node20", "Node21"),
        ("Node21", "Node22"), ("Node22", "Node23"), ("Node23", "Node24"), ("Node24", "Node25"),
        ("Node25", "Node26"), ("Node26", "Node27"), ("Node27", "Node28"), ("Node28", "Node29"),
        ("Node29", "Node30"), ("Node1", "Node30")
    ]
    G.add_edges_from(edges)

    return G

def detect_communities(graph):
    """Mendeteksi komunitas dalam graf menggunakan algoritma modularitas."""
    communities = list(greedy_modularity_communities(graph))
    community_mapping = {node: f"Community {i + 1}" for i, community in enumerate(communities) for node in community}
    return community_mapping

def recommendation(graph, user):
    """Merekomendasikan teman berdasarkan koneksi teman dari teman."""
    if user not in graph:
        return f"User {user} tidak ditemukan dalam jaringan sosial."
    # teman dari user
    friends = set(graph.neighbors(user))
    
    # teman dari teman
    friends_of_friends = {fof for friend in friends for fof in graph.neighbors(friend)} - friends - {user}
    
    return list(friends_of_friends)

def main():
    # Membuat jaringan sosial
    G = create_social_network()
    
    # Deteksi komunitas
    communities = detect_communities(G)
    print("Komunitas yang terdeteksi:")
    for user, community in communities.items():
        print(f"{user} -> {community}")
    
    # Testing rekomendasi teman
    while True:
        user_to_test = input("\nMasukkan nama pengguna untuk merekomendasikan teman: ")
        if user_to_test in G:
            break
        print(f"User {user_to_test} tidak ditemukan dalam jaringan sosial.")
    
    recommendations = recommendation(G, user_to_test)
    print(f"\nRekomendasi teman untuk {user_to_test}: {recommendations}")
    
    # Visualisasi
    try:
        import matplotlib.pyplot as plt
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray", node_size=400, font_size=5)
        plt.show()
    except ImportError:
        print("Matplotlib tidak diinstal. Lewati visualisasi graf.")

if __name__ == "__main__":
    main()