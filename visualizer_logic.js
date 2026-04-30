// PADI Sovereign Bureau - Visualizer Force Logic (v3.1)
const simulation = d3.forceSimulation(nodes)
    .force("link", d3.forceLink(links).id(d => d.id).distance(45))
    .force("charge", d3.forceManyBody().strength(-120))
    .force("center", d3.forceCenter(width / 2, height / 2))
    .force("collision", d3.forceCollide().radius(25))
    .on("tick", ticked);

function ticked() {
    link
        .attr("x1", d => d.source.x)
        .attr("y1", d => d.source.y)
        .attr("x2", d => d.target.x)
        .attr("y2", d => d.target.y);

    node
        // Deterministic Bounding Box logic to prevent screen drift
        .attr("cx", d => d.x = Math.max(20, Math.min(width - 20, d.x)))
        .attr("cy", d => d.y = Math.max(20, Math.min(height - 20, d.y)));

    labels
        .attr("x", d => d.x)
        .attr("y", d => d.y - 15);
}
