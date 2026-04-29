const METADATA_URL = 'https://raw.githubusercontent.com/peculiarlibrary/padi-ontology-kernel/main/metadata.json';

d3.json(METADATA_URL).then(data => {
    // CRITICAL FIX: Direct access to the nodes and links arrays
    const nodes = data.nodes;
    const links = data.links;

    const svg = d3.select("svg")
        .attr("width", window.innerWidth)
        .attr("height", window.innerHeight);

    const simulation = d3.forceSimulation(nodes)
        .force("link", d3.forceLink(links).id(d => d.id).distance(100))
        .force("charge", d3.forceManyBody().strength(-300))
        .force("center", d3.forceCenter(window.innerWidth / 2, window.innerHeight / 2));

    // Define the visual elements (circles and lines) here...
    console.log("Sovereign Data Linked:", nodes.length, "nodes active.");
}).catch(err => console.error("Bridge Error:", err));
