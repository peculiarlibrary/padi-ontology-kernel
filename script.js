// PADI Sovereign Bureau - Audited Force Calibration (v3.4)
d3.json("metadata.json").then(data => {
    const nodes = data.nodes;
    const links = data.links;
    const width = window.innerWidth;
    const height = window.innerHeight;

    const simulation = d3.forceSimulation(nodes)
        .force("link", d3.forceLink(links).id(d => d.id).distance(35))
        .force("charge", d3.forceManyBody().strength(-200))
        .force("center", d3.forceCenter(width / 2, height / 2))
        .force("x", d3.forceX(width / 2).strength(0.46))
        .force("y", d3.forceY(height / 2).strength(0.46))
        .force("collision", d3.forceCollide().radius(22))
        .on("tick", () => {
            // Hard Bound Clamping at 25px Margin
            nodes.forEach(d => {
                d.x = Math.max(25, Math.min(width - 25, d.x));
                d.y = Math.max(25, Math.min(height - 25, d.y));
            });
            // Update visual elements here...
        });
});
