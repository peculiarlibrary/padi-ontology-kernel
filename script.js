// PADI Sovereign Bureau - Audited Force Calibration (v3.4)
d3.json("metadata.json").then(data => {
    const width = window.innerWidth;
    const height = window.innerHeight;

    // 1. Initialize SVG Canvas
    const svg = d3.select("#viz").append("svg")
        .attr("width", width)
        .attr("height", height);

    // 2. Configure Simulation with Audited Gravity (0.46)
    const simulation = d3.forceSimulation(data.nodes)
        .force("link", d3.forceLink(data.links).id(d => d.id).distance(45))
        .force("charge", d3.forceManyBody().strength(-300))
        .force("center", d3.forceCenter(width / 2, height / 2))
        .force("x", d3.forceX(width / 2).strength(0.46))
        .force("y", d3.forceY(height / 2).strength(0.46))
        .force("collision", d3.forceCollide().radius(25));

    // 3. Render Link Elements
    const link = svg.append("g")
        .selectAll("line")
        .data(data.links)
        .enter().append("line")
        .attr("stroke", "#555")
        .attr("stroke-width", 1.5);

    // 4. Render Node Elements (Kernel vs Bureau Color Coding)
    const node = svg.append("g")
        .selectAll("circle")
        .data(data.nodes)
        .enter().append("circle")
        .attr("r", 10)
        .attr("fill", d => d.group === 1 ? "#ff9900" : "#0099ff")
        .attr("stroke", "#fff")
        .attr("stroke-width", 2)
        .call(d3.drag()
            .on("start", (event, d) => {
                if (!event.active) simulation.alphaTarget(0.3).restart();
                d.fx = d.x; d.fy = d.y;
            })
            .on("drag", (event, d) => { d.fx = event.x; d.fy = event.y; })
            .on("end", (event, d) => {
                if (!event.active) simulation.alphaTarget(0);
                d.fx = null; d.fy = null;
            }));

    // 5. Execute Tick Engine with 25px Boundary Clamping
    simulation.on("tick", () => {
        link
            .attr("x1", d => d.source.x)
            .attr("y1", d => d.source.y)
            .attr("x2", d => d.target.x)
            .attr("y2", d => d.target.y);

        node
            .attr("cx", d => d.x = Math.max(25, Math.min(width - 25, d.x)))
            .attr("cy", d => d.y = Math.max(25, Math.min(height - 25, d.y)));
    });
});
