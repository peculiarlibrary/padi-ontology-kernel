async function initializeBureau() {
    console.log("PADI A2UI: Initiating Handshake...");
    const assetList = document.getElementById('asset-list');
    const passportData = document.getElementById('passport-data');
    
    try {
        // Fetch the manifest and the broadcast signal
        const [manifestRes, broadcastRes] = await Promise.all([
            fetch('manifest.json'),
            fetch('broadcast.jsonld')
        ]);

        const manifest = await manifestRes.json();
        const broadcast = await broadcastRes.json();
        
        // 1. Render Identity from the Passport
        passportData.innerHTML = `
            <div class="identity-grid">
                <p><strong>Authority:</strong> Samuel M. Gitandu</p>
                <p><strong>Title:</strong> The Peculiar Librarian</p>
                <p><strong>Last Signal:</strong> ${new Date(broadcast.latest_update).toLocaleString()}</p>
                <p><strong>DOI:</strong> ${manifest.zenodo_doi || "10.5281/zenodo.18894084"}</p>
            </div>
        `;

        // 2. Render Knowledge Assets
        if (manifest.assets && manifest.assets.length > 0) {
            assetList.innerHTML = manifest.assets.map(asset => 
                `<li class="asset-item">
                    <strong>[${asset.type.toUpperCase()}]</strong> ${asset.name}
                 </li>`
            ).join('');
        } else {
            assetList.innerHTML = "<li>No assets indexed.</li>";
        }

        // Update Global Status
        document.getElementById('status-badge').innerText = "Status: Online & Fortified";

    } catch (error) {
        console.error("Handshake Failed:", error);
        passportData.innerHTML = "<p style='color: #f85149;'>Handshake Failed: Kernel unreachable.</p>";
    }
}

document.addEventListener('DOMContentLoaded', initializeBureau);
