async function initializeBureau() {
    const assetList = document.getElementById('asset-list');
    const passportData = document.getElementById('passport-data');
    const getPath = (file) => window.location.pathname.endsWith('/') ? file : `./${file}`;

    try {
        const [manifestRes, broadcastRes] = await Promise.all([
            fetch(getPath('manifest.json')),
            fetch(getPath('broadcast.jsonld'))
        ]);

        if (!manifestRes.ok || !broadcastRes.ok) throw new Error("Kernel Handshake Failed");

        const manifest = await manifestRes.json();
        const broadcast = await broadcastRes.json();
        
        // Render Identity & Signal Time
        passportData.innerHTML = `
            <div class="identity-grid">
                <p><strong>Authority:</strong> ${manifest.governing_architect}</p>
                <p><strong>Bureau Version:</strong> v${manifest.kernel_version}</p>
                <p><strong>Last Signal:</strong> ${new Date(broadcast.latest_update).toLocaleString()}</p>
                <p><strong>DOI:</strong> ${manifest.zenodo_doi}</p>
            </div>
        `;

        // Render Sealed Assets
        assetList.innerHTML = manifest.assets.map(asset => 
            `<li class="asset-item" style="margin-bottom: 15px;">
                <strong>[${asset.type.toUpperCase()}]</strong> ${asset.name}
                <br><code style="font-size: 0.75em; color: #238636; background: #0d1117; padding: 2px 5px; border-radius: 4px;">
                    SHA256: ${asset.sha256.substring(0, 24)}...
                </code>
             </li>`
        ).join('');

        document.getElementById('status-badge').innerText = "Status: Online & Fortified";

    } catch (error) {
        console.warn("Handshake Error:", error);
        passportData.innerHTML = "<p style='color: #f85149;'>Handshake Pending: Awaiting A2A Signal.</p>";
    }
}

document.addEventListener('DOMContentLoaded', initializeBureau);
