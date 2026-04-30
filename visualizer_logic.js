// PADI Sovereign Bureau - Audited Force Calibration (v3.4)
// Calculated Parameters: Gravity 0.46 | Safe Radius 428.49px
const simulation = d3.forceSimulation(nodes)
    .force("link", d3.forceLink(links).id(d => d.id).distance(35))
    .force("charge", d3.forceManyBody().strength(-200))
    .force("center", d3.forceCenter(width / 2, height / 2))
    // Apply Audited Gravity (0.46) to both axes
    .force("x", d3.forceX(width / 2).strength(0.46))
    .force("y", d3.forceY(height / 2).strength(0.46))
    .force("collision", d3.forceCollide().radius(22))
    .on("tick", ticked);

function ticked() {
    link
        .attr("x1", d => d.source.x)
        .attr("y1", d => d.source.y)
        .attr("x2", d => d.target.x)
        .attr("y2", d => d.target.y);

    node
        // Hard Bound Clamping at 25px Margin as per Audit
        .attr("cx", d => d.x = Math.max(25, Math.min(width - 25, d.x)))
        .attr("cy", d => d.y = Math.max(25, Math.min(height - 25, d.y)));

    labels
        .attr("x", d => d.x)
        .attr("y", d => d.y - 15);
}
