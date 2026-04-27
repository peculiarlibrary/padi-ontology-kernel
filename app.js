async function initializeBureau() {
    const assetList = document.getElementById('asset-list');
    const passportData = document.getElementById('passport-data');
    
    // Auto-detect base path for GitHub Pages
    const baseUrl = window.location.origin + window.location.pathname.replace(/\/$/, "");
    
    async function fetchWithRetry(url, retries = 3) {
        for (let i = 0; i < retries; i++) {
            try {
                const response = await fetch(url + '?t=' + new Date().getTime()); // Cache buster
                if (response.ok) return await response.json();
            } catch (e) {
                console.warn(`Attempt ${i + 1} failed for ${url}`);
                await new Promise(r => setTimeout(r, 2000));
            }
        }
        throw new Error(`Failed to fetch ${url} after ${retries} attempts`);
    }

    try {
        console.log("PADI: Initiating Sovereign Handshake...");
        
        const [manifest, broadcast] = await Promise.all([
            fetchWithRetry(`${baseUrl}/manifest.json`),
            fetchWithRetry(`${baseUrl}/broadcast.jsonld`)
        ]);

        passportData.innerHTML = `
            <div class="identity-grid">
                <p><strong>Authority:</strong> ${manifest.governing_architect}</p>
                <p><strong>Status:</strong> Online & Verified</p>
                <p><strong>Last Signal:</strong> ${new Date(broadcast.latest_update).toLocaleString()}</p>
                <p><strong>DOI:</strong> ${manifest.zenodo_doi}</p>
            </div>
        `;

        assetList.innerHTML = manifest.assets.map(asset => 
            `<li class="asset-item">
                <strong>[${asset.type.toUpperCase()}]</strong> ${asset.name}
                <br><code style="font-size: 0.7em; color: #238636;">SHA256: ${asset.sha256.substring(0, 16)}...</code>
            </li>`
        ).join('');

        document.getElementById('status-badge').innerText = "Status: Online & Fortified";

    } catch (error) {
        console.error("Bureau Handshake Error:", error);
        passportData.innerHTML = `
            <p style="color: #f85149;"><strong>Handshake Offline</strong></p>
            <p style="font-size: 0.8em;">The Kernel is currently rebasing or the CDN is propagating. Check back in 60s.</p>
        `;
    }
}

document.addEventListener('DOMContentLoaded', initializeBureau);
