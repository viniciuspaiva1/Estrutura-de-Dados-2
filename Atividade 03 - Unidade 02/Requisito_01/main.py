from operator import itemgetter
import networkx as nx
import wikipedia
import matplotlib.pyplot as plt

def graphBuilder(pageTitle):
    SEED = pageTitle.title()
    STOPS = ("International Standard Serial Number",
            "International Standard Book Number",
            "National Diet Library",
            "International Standard Name Identifier",
            "International Standard Book Number (Identifier)",
            "Pubmed Identifier",
            "Pubmed Central",
            "Digital Object Identifier",
            "Arxiv",
            "Proc Natl Acad Sci Usa",
            "Bibcode",
            "Library Of Congress Control Number",
            "Jstor",
            "Doi (Identifier)",
            "Isbn (Identifier)",
            "Pmid (Identifier)",
            "Arxiv (Identifier)",
            "Bibcode (Identifier)")

    todo_lst = [(0, SEED)]  # The SEED is in layer 0
    todo_set = set(SEED)  # The SEED itself
    done_set = set()  # Nothing is done yet

    g = nx.DiGraph()
    layer, page = todo_lst[0]

    while layer < 2:
        # Remove the name page of the current page from the todo_lst,
        # and add it to the set of processed pages.
        # If the script encounters this page again, it will skip over it.
        del todo_lst[0]
        done_set.add(page)

        # Show progress
        print(layer, page)

        # Attempt to download the selected page.
        try:
            wiki = wikipedia.page(page)  # Specify language as 'en' for English
        except wikipedia.exceptions.DisambiguationError as e:
            print(f"Ambiguous page: {page}. Skipping.")
            layer, page = todo_lst[0]
            continue
        except:
            print("Could not load", page)
            layer, page = todo_lst[0]
            continue

        for link in wiki.links:
            link = link.title()
            if link not in STOPS and not link.startswith("List Of"):
                if link not in todo_set and link not in done_set:
                    todo_lst.append((layer + 1, link))
                    todo_set.add(link)
                g.add_edge(page, link)
        layer, page = todo_lst[0]

    print("{} nodes, {} edges".format(len(g), nx.number_of_edges(g)))
    return g

graphAlbion = graphBuilder("Albion Online")
graphOutlast = graphBuilder("Outlast 2")
graphAge = graphBuilder("Alan Wake 2")
graphCities = graphBuilder("Cities: Skylines II")

composeAlbionOutlast = nx.compose(graphAlbion, graphOutlast)
composeAgeCities = nx.compose(graphAge, graphCities)

composeAll = nx.compose(composeAlbionOutlast, composeAgeCities)

print("{} nodes, {} edges".format(len(composeAll), nx.number_of_edges(composeAll)))

# make a copy of raw graph
original = composeAll.copy()
     

# remove self loops
composeAll.remove_edges_from(nx.selfloop_edges(composeAll))

# identify duplicates like that: 'network' and 'networks'
duplicates = [(node, node + "s")
              for node in composeAll if node + "s" in composeAll]

for dup in duplicates:
  # *dup is a technique named 'unpacking'
  composeAll = nx.contracted_nodes(composeAll, *dup, self_loops=False)

print(duplicates)

duplicates = [(x, y) for x, y in
              [(node, node.replace("-", " ")) for node in composeAll]
                if x != y and y in composeAll]
print(duplicates)

for dup in duplicates:
  composeAll = nx.contracted_nodes(composeAll, *dup, self_loops=False)

# nx.contracted creates a new node/edge attribute called contraction
# the value of the attribute is a dictionary, but GraphML
# does not support dictionary attributes
nx.set_node_attributes(composeAll, 0,"contraction")
nx.set_edge_attributes(composeAll, 0,"contraction")
     

print("{} nodes, {} edges".format(len(composeAll), nx.number_of_edges(composeAll)))

plt.style.use("default")
# degree sequence
degree_sequence = sorted([d for n, d in composeAll.degree()], reverse=True)

fig, ax = plt.subplots(1,2,figsize=(8,4))

# all_data has information about degree_sequence and the width of each bin
ax[0].hist(degree_sequence)
ax[1].hist(degree_sequence,bins=[1,2,3,4,5,6,7,8,9,10])

ax[0].set_title("Degree Histogram")
ax[0].set_ylabel("Count")
ax[0].set_xlabel("Degree")
ax[0].set_ylim(0,15000)

ax[1].set_title("Degree Histogram - Zoom")
ax[1].set_ylabel("Count")
ax[1].set_xlabel("Degree")
ax[1].set_xlim(0,10)
ax[1].set_ylim(0,15000)

plt.tight_layout()
plt.show()
     

# filter nodes with degree greater than or equal to 2
core = [node for node, deg in dict(composeAll.degree()).items() if deg >= 2]

# select a subgraph with 'core' nodes
gsub = nx.subgraph(composeAll, core)

print("{} nodes, {} edges".format(len(gsub), nx.number_of_edges(gsub)))

nx.write_graphml(gsub, "cna.graphml")
     

print("Nodes removed: {:.2f}%".format(100*(1 - 3420/13775)))
print("Edges removed: {:.2f}%".format(100*(1 - 14771/24856)))
print("Edges per nodes: {:.2f}".format(13775/3420))

top_indegree = sorted(dict(gsub.in_degree()).items(),
                      reverse=True, key=itemgetter(1))[:100]
print("\n".join(map(lambda t: "{} {}".format(*reversed(t)), top_indegree)))