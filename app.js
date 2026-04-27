async function initializeBureau() {
    const assetList = document.getElementById('asset-list');
    const passportData = document.getElementById('passport-data');
    
    // Helper to handle relative paths on GitHub Pages
    const getPath = (file) => window.location.pathname.endsWith('/') ? file : `./${file}`;

    try {
        const [manifestRes, broadcastRes] = await Promise.all([
            fetch(getPath('manifest.json')),
            fetch(getPath('broadcast.jsonld'))
        ]);

        if (!manifestRes.ok || !broadcastRes.ok) throw new Error("Kernel files missing");

        const manifest = await manifestRes.json();
        const broadcast = await broadcastRes.json();
        
        passportData.innerHTML = `
            <div class="identity-grid">
                <p><strong>Authority:</strong> Samuel Muriithi Gitandu</p>
                <p><strong>Title:</strong> The Peculiar Librarian</p>
                <p><strong>Last Signal:</strong> ${new Date(broadcast.latest_update).toLocaleString()}</p>
                <p><strong>DOI:</strong> ${manifest.zenodo_doi || "10.5281/zenodo.18894084"}</p>
            </div>
        `;

        assetList.innerHTML = manifest.assets.map(asset => 
            `<li class="asset-item"><strong>[${asset.type.toUpperCase()}]</strong> ${asset.name}</li>`
        ).join('');

        document.getElementById('status-badge').innerText = "Status: Online & Fortified";

    } catch (error) {
        console.warn("Handshake delay, retrying with manifest only...");
        // Fallback: Try to at least show the identity if broadcast fails
        passportData.innerHTML = `
            <p><strong>Architect:</strong> Samuel M. Gitandu</p>
            <p><strong>Status:</strong> Handshake Pending...</p>
            <p style="font-size: 0.8em; color: #8b949e;">Check GitHub Actions to ensure files are generated.</p>
        `;
    }
}

document.addEventListener('DOMContentLoaded', initializeBureau);
